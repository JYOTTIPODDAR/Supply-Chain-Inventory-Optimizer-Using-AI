📦 AI Supply Chain Inventory Optimizer

An AI-powered Supply Chain Inventory Optimization System that predicts product demand and helps businesses make smarter inventory decisions.

This project combines Machine Learning + Flask Web Development + Interactive Dashboard UI to build a practical real-world supply chain optimization system.

🚀 Project Overview

Efficient inventory management is critical in supply chain operations.

Poor inventory planning leads to:

📉 Stockouts → Lost sales

📦 Overstocking → High storage cost

This system solves the problem by:

✔ Predicting future demand using Machine Learning
✔ Comparing predicted demand with current inventory
✔ Recommending whether stock should be reordered
✔ Providing results through a Flask-based interactive dashboard

🧠 Key Features

🤖 Demand Forecasting using Machine Learning

📊 Interactive Inventory Dashboard

🔐 User Authentication (Login & Register)

📦 Reorder Decision System

🎨 Modern UI Dashboard

💾 SQLite Database Integration

🛠️ Tech Stack
Backend

Python

Flask

SQLite

Machine Learning

Scikit-learn

Pandas

NumPy

Frontend

HTML

CSS

JavaScript

Development Tools

Git

GitHub

VS Code

Jupyter Notebook

📂 Project Structure
Supply-Chain-Inventory-Optimizer-Using-AI
│
├── data/
│   └── retail_store_inventory.csv
│
├── model/
│   └── demand_model.pkl
│
├── notebooks/
│   └── model_training.ipynb
│
├── database/
│   └── database.db
│
├── static/
│   ├── style.css
│   └── script.js
│
├── templates/
│   ├── base.html
│   ├── login.html
│   ├── register.html
│   ├── dashboard.html
│
├── app.py
├── create_db.py
├── requirements.txt
└── README.md
⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/JYOTTIPODDAR/Supply-Chain-Inventory-Optimizer-Using-AI.git
cd Supply-Chain-Inventory-Optimizer-Using-AI
2️⃣ Create Virtual Environment
python -m venv venv

Activate:

Windows

venv\Scripts\activate
3️⃣ Install Dependencies
pip install -r requirements.txt
4️⃣ Create Database
python create_db.py
5️⃣ Run the Application
python app.py

Open browser:

http://127.0.0.1:5000
📊 How the System Works

1️⃣ User logs into the system
2️⃣ User enters current inventory stock
3️⃣ Machine Learning model predicts future demand
4️⃣ System compares:

Current Stock

Predicted Demand

5️⃣ System provides reorder decision

Example Output:

Predicted Demand : 820
Current Stock : 500
Reorder Status : YES
📈 Machine Learning Model

The demand prediction model is trained using historical retail inventory data.

Input Features include:

Current stock

Units ordered

Product price

Discount

Competitor pricing

Time-based features

Model Output:

Predicted Future Demand

The trained model is saved as:

model/demand_model.pkl
🔐 Authentication System

The system includes user authentication:

User Registration

Login System

Session Management

Secure Dashboard Access

🎨 UI Dashboard

The system provides an interactive dashboard displaying:

Predicted demand

Current inventory

Reorder recommendation

Future improvements include:

📊 Demand trend graphs

📦 Inventory analytics

📈 Forecast visualization

📌 Future Improvements

Add Chart.js analytics dashboard

Implement EOQ inventory optimization

Add supplier recommendation system

Deploy on cloud platforms (AWS / Render / Azure)

👩‍💻 Author

Jyoti kumari
Aryan kumar

B.Tech Computer Science (AI & ML)
Aspiring AI Engineer

GitHub:
https://github.com/JYOTTIPODDAR