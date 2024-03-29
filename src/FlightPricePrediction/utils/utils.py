from src.FlightPricePrediction.logger import logging
from src.FlightPricePrediction.exception import CustomException

import os
import pickle
import sys
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    try:
        dir_path = os.path.dirname(file_path)

        logging.info(f"Make Director named: {dir_path}")
        os.makedirs(dir_path, exist_ok=True)

        logging.info('Directory Created')

        with open(file_path, 'wb') as file_obj:
            pickle.dump(obj, file_obj)

        logging.info(f"Dumped Object in filepath: {file_path}")

    except Exception as e:
        logging.info("Exceptio in save_object() method")
        raise CustomException(e, sys)
    

def evaluate_model(X_train, y_train, X_test, y_test, models):
    try: 
        report = {}

        for i in range(len(models)):
            model = list(models.values())[i]

            model.fit(X_train, y_train)

            y_pred = model.predict(X_test)

            test_model_score = r2_score(y_test, y_pred)

            report[list(models.keys())[i]] = test_model_score

        return report
    
    except Exception as e:
        logging.info("Exception in evaluate_model()")
        raise CustomException(e, sys)
    

def load_object(path):
    try:
        with open(path, 'rb') as file_obj:
            return pickle.load(file_obj)
        
    except Exception as e:
        logging.info('Exception in load_object()')
        raise CustomException(e, sys)