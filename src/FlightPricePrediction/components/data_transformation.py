import pandas as pd
import os 
import sys
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder


from src.FlightPricePrediction.exception import CustomException
from src.FlightPricePrediction.logger import logging
from src.FlightPricePrediction.utils.utils import save_object

class DataTransformationConfig:
    preprocessor_obj_file_path = os.path.join('artifacts', 'preprocessor.pkl')

class DataTransformation:
    def __init__(self):
        self.data_transformation_config = DataTransformationConfig()

    def get_data_transformation(self):
        try:
            logging.info("Initialize Data Transformation")

            categorical_col = ['airline', 'flight', 'source_city', 'departure_time', 'stops','arrival_time', 'destination_city', 'class']
            numericla_col = ['duration', 'days_left']

            logging.info("Pipeline Initiated")

            # Numerical Pipeline
            num_pipeline = Pipeline(
                steps=[('imputer', SimpleImputer(strategy='median')),
                       ('scaler', StandardScaler())
                       ])
            
            # Categorical Pipeline
            cat_pipeline = Pipeline(
                steps=[
                    ('imputer', SimpleImputer(strategy='most_frequent')),
                    ('onehot_encoding', OneHotEncoder(handle_unknown='ignore'))
                ]   
            )

            preprocess = ColumnTransformer([
                ('num_pipeline', num_pipeline, numericla_col),
                ('cat_pipeline', cat_pipeline, categorical_col)
            ])

            return preprocess

        except Exception as e:
            logging.info("Exception in get_data_transformation()")
            raise CustomException(e, sys)
        
    def initialize_data_transformation(self, train_path, test_path):
        try:
            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Train and Test Data Read: Mission Accomplished!")
            logging.info(f"Train DataFrame head: {train_df.head().to_string()}")
            logging.info(f"Test DataFrame head: {test_df.head().to_string()}")

            preprocess_obj = self.get_data_transformation()

            target_col_name = 'price'
            drop_col = [target_col_name, "Unnamed: 0"]

            train_input_feature = train_df.drop(drop_col, axis=1)
            target_train_feature = train_df[target_col_name]

            test_input_feature = test_df.drop(drop_col, axis=1)
            target_test_feature = test_df[target_col_name]

            train_input_feature_arr = preprocess_obj.fit_transform(train_input_feature)
            test_input_feature_arr = preprocess_obj.transform(test_input_feature)

            logging.info("Applying Preprocess on Train and Test dataset")

            save_object(
                file_path=self.data_transformation_config.preprocessor_obj_file_path,
                obj = preprocess_obj
            )

            logging.info("Preprocessor Pickel file stored")

            # # Use numpy.c_ to concatenate them horizontally
            # logging.info("Concate the transform data and target data")
            # target_arr = np.c_[train_input_feature_arr, np.array(target_train_feature)]
            # test_arr = np.c_[test_input_feature_arr, np.array(target_test_feature)]

            # logging.info("Retunr created train test arrays")
            # return (
            #     target_arr,
            #     test_arr
            # )

            return(
                train_input_feature_arr, 
                np.array(target_train_feature),
                test_input_feature_arr,
                np.array(target_test_feature)
            )
            

        except Exception as e:
            logging.info("exception in initialize_data_transformation()")
            raise CustomException(e, sys)