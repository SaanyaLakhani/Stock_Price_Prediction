from flask import Flask, render_template, request, jsonify
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline

app = Flask(__name__)

# Generate synthetic stock data
np.random.seed(42)
X = np.random.rand(1000, 4) * 100  # Random Open, High, Low, Volume
y = X[:, 0] * 0.5 + X[:, 1] * 0.3 + X[:, 2] * 0.2  # Simulated Close Price

# Train model using a Pipeline
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

pipeline = Pipeline([
    ('scaler', StandardScaler()),   # Standardize features
    ('model', LinearRegression())   # Apply Linear Regression
])

pipeline.fit(X_train, y_train)  # Train the pipeline

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()  # Get JSON data from request
        stock = data["stock"]  # Get stock name from dropdown
        open_price = float(data["open"])
        high = float(data["high"])
        low = float(data["low"])
        volume = float(data["volume"])

        # Prepare input for model
        features = np.array([[open_price, high, low, volume]])
        predicted_close = pipeline.predict(features)[0]  # Use pipeline instead of model

        # Convert predicted close price to percentage change
        percentage_change = ((predicted_close - open_price) / open_price) * 100

        return jsonify({"stock": stock, "percentage_change": round(percentage_change, 2)})

    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

    

