import pandas as pd
import os
import sys
from dataclasses import dataclass

from sklearn.linear_model import LinearRegression, Lasso, Ridge, ElasticNet

from src.FlightPricePrediction.logger import logging
from src.FlightPricePrediction.exception import CustomException
from src.FlightPricePrediction.utils.utils import save_object, evaluate_model

@dataclass
class ModelTrainingConfig:
    training_model_file_path = os.path.join('artifacts', 'model.pkl')

class ModelTraner:
    def __init__(self):
        self.model_training_config = ModelTrainingConfig()

    def initiate_model_traner(train_array, test_array):
        try:
            logging.info('Spliting Dependent and Independent variables from train and test data')

            X_train, y_train, X_test, y_test = (
                train_array[:, :-1],
                train_array[:,-1],
                test_array[:, :-1],
                test_array[:,-1]
            )

            models = {
                'LinearRegression': LinearRegression(),
                'Lasso': Lasso(),
                'Ridge': Ridge(),
                'ElasticNet':ElasticNet()
            }

            model_report:dict = evaluate_model(X_train, y_train, X_test, y_test, models)
            logging.info(f"Model Report: {model_report}")

            # to get the best model score from dictionary
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[list(model_report.values()).index(best_model_score)]

            best_model = models[best_model_name]

            print(f"Best model found, Model Name: {best_model_name}, R2_Score: {best_model_score}")
            print("\n =========================================================== \n")
            logging.info(f"Best model found, Model Name: {best_model_name}, R2_Score: {best_model_score}")

            save_object(
                file_path = self.model_training_config.training_model_file_path,
                obj = best_model
            )

        except Exception as e:
            logging.info('Exception in initiate_model_trainer() method')
            raise CustomException(e, sys)