from src.FlightPricePrediction.components.data_ingestion import DataIngestion
import pandas as pd
import os
import sys 
from src.FlightPricePrediction.logger import logging
from src.FlightPricePrediction.exception import CustomException

data_ingestio_obj = DataIngestion()

data_ingestio_obj.initiate_data_ingestion()