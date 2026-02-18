# Flask Application
from flask import Flask, jsonify, request
import mlflow

# Loading models
price_model = mlflow.sklearn.load_model('models/price_prediction_model')
hotel_rec_model = mlflow.sklearn.load_model('models/hotel_recommendation_model')
gender_model = mlflow.sklearn.load_model('models/gender_classification_model') 

hotel_map ={0: 'Hotel A', 1: 'Hotel AF', 2: 'Hotel AU', 3: 'Hotel BD', 4: 'Hotel BP',
             5: 'Hotel BW', 6: 'Hotel CB', 7: 'Hotel K', 8: 'Hotel Z'}

app = Flask(__name__)


@app.route('/')
def home():
    message =f"""Welcome to the Flask API!,<br><br>
For Travel Price Prediction go to the endpoint: '/predict_price'<br>
input example: {price_model.input_example.iloc[0].to_dict()} <br><br>
For Hotel Recommendation go to the endpoint: '/recommend_hotel'<br>
input example: {hotel_rec_model.input_example.iloc[0].to_dict()} <br><br>
For Gender Classification go to the endpoint: '/classify_gender' <br>
input example: {gender_model.input_example.iloc[0].to_dict()} <br>
"""
    return message

@app.route('/predict_price', methods=['POST'])
def predict_price():
    try:
        data = request.get_json(force=True)
        price = price_model.predict(data)

        return jsonify({'predicted_price': price[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500



@app.route('/recommend_hotel', methods=['POST'])
def recommend_hotel():
    try:
        data = request.get_json(force=True)
        hotel = hotel_rec_model.predict(data)

        return jsonify({'recommended_hotel': hotel_map[hotel[0]]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/classify_gender', methods=['POST'])
def classify_gender():
    try:
        data = request.get_json(force=True)
        gender = gender_model.predict(data)

        return jsonify({'classified_gender': gender[0]})
    except Exception as e:
        return jsonify({'error': str(e)}), 500
    
if __name__ == '__main__':
    app.run(host="0.0.0.0",port=5000,debug=True)
