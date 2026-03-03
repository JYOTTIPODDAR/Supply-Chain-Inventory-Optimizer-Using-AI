📦 Supply Chain Inventory Optimizer Using AI

An AI-powered web application that predicts product demand and helps businesses optimize inventory decisions to reduce overstock and stockouts.

This project combines Machine Learning + Flask Web Development to build a practical real-world supply chain optimization system.

🚀 Project Overview

Efficient inventory management is crucial for supply chain operations. Overstocking increases holding costs, while understocking leads to lost sales.

This system:

Predicts future demand using a trained ML model

Compares predicted demand with current stock

Suggests whether inventory should be reordered

Provides results through a simple Flask-based web interface

🛠️ Tech Stack

Python

Flask

Scikit-learn

Pandas

NumPy

HTML/CSS

📂 Project Structure
Supply-Chain-Inventory-Optimizer-Using-AI/
│
├── data/                 # Dataset used for training
├── model/                # Trained ML model (.pkl file)
├── notebooks/            # Model training & experimentation
├── static/               # CSS and frontend assets
├── templates/            # HTML files for Flask
│
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
└── README.md             # Project documentation
🧠 How It Works

User enters current inventory details in the web form.

The Flask app loads the trained machine learning model.

The model predicts future demand.

The system compares:

Current Stock

Predicted Demand

Based on a reorder threshold, the system suggests:

✅ Reorder Required

❌ No Reorder Needed

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/JYOTTIPODDAR/Supply-Chain-Inventory-Optimizer-Using-AI.git
cd Supply-Chain-Inventory-Optimizer-Using-AI
2️⃣ Create Virtual Environment (Recommended)
python -m venv venv
venv\Scripts\activate   # Windows
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Run the Application
python app.py

Then open your browser and go to:

http://127.0.0.1:8000
📊 Model Details

The model is trained using historical inventory and demand data.

It uses supervised learning (Scikit-learn).

The trained model is stored as a .pkl file and loaded inside app.py.

Feature inputs include:

Current stock

Units ordered

Price

Discount

Competitor pricing

Date features

🎯 Key Features

✔ Demand Forecasting
✔ Inventory Optimization
✔ Reorder Decision Logic
✔ Clean Flask Web Interface
✔ Real-world Supply Chain Use Case

📌 Future Improvements

Add real-time dashboard visualization

Deploy on cloud (Render / AWS / Azure)

Add advanced models (XGBoost / LSTM)

Add database integration (PostgreSQL)

Add authentication system for multiple users
