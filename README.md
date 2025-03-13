📈 Stock Price Prediction
📌 Project Overview
The Stock Price Prediction system is a machine learning-based web application that predicts the percentage change in the closing price of a stock based on user input. It uses a linear regression model trained on synthetic data generated from random stock market features such as open price, high price, low price, and volume.

📊 Features
The application allows users to input the following stock market features:

Stock Name (dropdown) - Select from a list of popular stocks.

Open Price (float) - The opening price of the stock.

High Price (float) - The highest price of the stock during the trading day.

Low Price (float) - The lowest price of the stock during the trading day.

Volume (int) - The trading volume of the stock.

Based on these inputs, the application predicts the percentage change in the closing price of the selected stock.

🛠 Tech Stack
Machine Learning: Scikit-learn (Linear Regression)

Backend: Flask

Frontend: HTML, CSS, JavaScript

Deployment: Localhost (can be extended to cloud platforms like AWS, Heroku, etc.)

📂 Project Structure
Copy
stock-price-prediction/
│── static/                     # Contains static files like CSS, JS, and images
│   │── style.css               # CSS file for styling the web page
│   │── script.js               # JavaScript file for handling frontend logic
│   │── logo.jpg                # Logo image for the web application
│── templates/                  # Contains HTML files for UI
│   │── index.html              # Main HTML file for the web interface
│── app.py                      # Flask application file
│── requirements.txt            # Dependencies list
🔧 Installation & Setup
1️⃣ Clone the Repository
bash
Copy
git clone <repository_link>
cd stock-price-prediction
2️⃣ Install Dependencies
bash
Copy
pip install -r requirements.txt
3️⃣ Run Flask Application Locally
bash
Copy
python app.py
Open your browser and go to:

Copy
http://127.0.0.1:5000
🚀 Model Training
The model used in this project is a Linear Regression model trained on synthetic data. The data is generated randomly, and the model is trained using a pipeline that includes feature scaling and linear regression.

To train the model, the following steps are performed in app.py:

Generate synthetic stock data.

Split the data into training and testing sets.

Create a pipeline with StandardScaler and LinearRegression.

Train the pipeline on the training data.

🎯 Features
✅ User-friendly Web Interface
✅ Real-time Stock Price Prediction
✅ Linear Regression Model for Prediction
✅ Flask API Backend
✅ Responsive Design with Glassmorphism Effect

UI APP






📜 License
This project is open-source and free to use.
Let me know if you need further modifications! 🚀
