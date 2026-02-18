# Use an official lightweight Python image
FROM python:3.12-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY models/gender_classification_model ./models/gender_classification_model
COPY models/hotel_recommendation_model ./models/hotel_recommendation_model
COPY models/price_prediction_model ./models/price_prediction_model  
COPY app.py .

# Expose the port Flask runs on
EXPOSE 5000

# Run the Flask app
CMD ["python", "app.py"]
