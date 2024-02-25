from src.FlightPricePrediction.pipelines.prediction_pipeline import CustomData, Predict_Pipeline

from flask import Flask, request, render_template, jsonify
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home_page():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'GET':
        return render_template('form.html')
    
    else:
        travel_date = request.form.get('travel_date')
        travel_date = datetime.strptime(travel_date, '%Y-%m-%d')
        current_date = datetime.now()
        difference = travel_date - current_date
        days_left = difference.days


        custom_date = CustomData(
            airline = request.form.get('airline'),
            flight = request.form.get('flight'),
            source_city = request.form.get('source_city'),
            departure_time = request.form.get('departure_time'),
            stops = request.form.get('stops'),
            arrival_time = request.form.get('arrival_time'),
            destination_city = request.form.get('destination_city'),
            flight_class = request.form.get('class'),
            duration = request.form.get('duration'),
            days_left = days_left
        )

        df = custom_date.get_data_as_dataframe()

        predict_obj = Predict_Pipeline()
        predicted_value = predict_obj.predict(df)
        predicted_value = round(predicted_value[0], 0)
        return render_template('result.html', final_result = predicted_value)

if __name__ == "__main__":
    app.run(host = "0.0.0.0", port=8080,debug=True)