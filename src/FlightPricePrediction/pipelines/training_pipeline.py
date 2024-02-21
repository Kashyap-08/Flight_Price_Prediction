from src.FlightPricePrediction.components.data_ingestion import DataIngestion
from src.FlightPricePrediction.components.data_transformation import DataTransformation
from src.FlightPricePrediction.components.model_training import ModelTraner

import pandas as pd
import os
import sys 
from src.FlightPricePrediction.logger import logging
from src.FlightPricePrediction.exception import CustomException

data_ingestio_obj = DataIngestion()

train_data_path, test_data_path = data_ingestio_obj.initiate_data_ingestion()

data_transformation_obj = DataTransformation()
X_train, y_train, X_test, y_test = data_transformation_obj.initialize_data_transformation(train_data_path, test_data_path)
# train_arr, test_arr = data_transformation_obj.initialize_data_transformation(train_data_path, test_data_path)

model_training_obj = ModelTraner()
model_training_obj.initiate_model_traner(X_train, y_train, X_test, y_test)
# model_training_obj.initiate_model_traner(train_arr, test_arr)
