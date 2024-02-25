from src.FlightPricePrediction.pipelines.prediction_pipeline import CustomData, Predict_Pipeline

customclass = CustomData('SpiceJet','SG-8709','Delhi','Evening','zero','Night','Mumbai','Economy',2.17,1)

data = customclass.get_data_as_dataframe()

print(data)

pred = Predict_Pipeline()

predicted_value = pred.predict(data)

print("predicted value is:", predicted_value)



