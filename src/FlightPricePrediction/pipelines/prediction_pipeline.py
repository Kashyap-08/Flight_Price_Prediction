import sys
import os
import pandas as pd

from src.FlightPricePrediction.exception import CustomException
from src.FlightPricePrediction.logger import logging
from src.FlightPricePrediction.utils.utils import load_object

class Predict_Pipeline:
    def __init__(self):
        pass

    def predict(self, features):
        try:
            preprocessor_path = os.path.join("artifacts", "preprocessor.pkl")
            model_path = os.path.join("artifacts", "model.pkl")

            logging.info("reading the preprocessor and model object from artifacts")

            preprocessor_obj = load_object(preprocessor_path)
            model_obj = load_object(model_path)

            logging.info("transoforming the new data")

            scaled_data = preprocessor_obj.transform(features)

            logging.info("Predicting the price of the Flight")

            prediction = model_obj.predict(scaled_data)

            return prediction

        except Exception as e:
            logging.info("Exceptio while Predicing")
            raise CustomException(e, sys)


class CustomData:

    def __init__(self, airline, flight, source_city, departure_time, stops, arrival_time, destination_city, flight_class, duration, days_left):
        self.airline = airline
        self.flight=flight
        self.source_city=source_city
        self.departure_time=departure_time
        self.stops=stops
        self.arrival_time=arrival_time
        self.destination_city=destination_city
        self.flight_class=flight_class
        self.duration=duration
        self.days_left= days_left

    def get_data_as_dataframe(self):
        try:
            custom_data_input_dict = {
                'airline':[self.airline], 
                'flight':[self.flight], 
                'source_city':[self.source_city], 
                'departure_time':[self.departure_time], 
                'stops':[self.stops], 
                'arrival_time':[self.arrival_time], 
                'destination_city':[self.destination_city], 
                'class':[self.flight_class], 
                'duration':[self.duration], 
                'days_left':[self.days_left]
            }

            df = pd.DataFrame(custom_data_input_dict)
            logging.info("DataFrame Created from the new Data")

            return df
        
        except Exception as e:
            logging.info("Exception in get_data_as_dataframe()")
            raise CustomException(e, sys)
