# 🚀 Supply Chain Inventory Optimizer Using AI

An AI-assisted web application that helps businesses monitor inventory health, detect stock risks, and support smarter supply-chain decisions using dataset-driven analytics.

This project provides a complete **inventory analysis dashboard** with intelligent product-status prediction based on required quantity and current stock levels.

Built using **Python, Flask, Pandas, SQLAlchemy, and Bootstrap UI**.

---

# 📌 Project Overview

Managing inventory efficiently is critical for any supply chain system. Poor inventory visibility leads to:

* Stock shortages
* Overstock losses
* Supplier delays
* Poor reorder planning

This project solves these issues using a smart decision engine that:

✔ analyzes uploaded inventory datasets
✔ detects low-stock & overstock risks
✔ evaluates supplier delay alerts
✔ checks product availability based on required quantity
✔ provides dashboard analytics & visualization
✔ allows configurable inventory thresholds via settings

---

# 🧠 Key Features

## 🔐 Authentication System

* User Registration
* Secure Login
* Logout functionality

---

## 📦 Inventory Dataset Analysis

Upload CSV dataset and automatically:

* calculate total products
* detect low-stock items
* detect overstock items
* detect supplier delay risks

---

## 📊 Smart Inventory Decision Engine

Users can enter:

```
Product Name + Required Quantity
```

System predicts:

* ❌ Stock Out
* ⚠ Low Stock
* 📦 Overstock Available
* ✅ Required Quantity Available

This simulates real supply-chain decision logic.

---

## 📈 Dashboard Analytics

Live statistics displayed:

* Total products
* Low stock count
* Overstock count
* Supplier delay alerts

---

## 📉 Visualization Module

Category-wise inventory insights using dataset grouping logic.

Helps managers understand inventory distribution quickly.

---

## ⚙ Settings Panel

Users can configure:

* Low stock threshold
* Default reorder quantity
* Email alert toggle
* Auto reorder suggestion toggle

These settings make the system customizable.

---

# 🏗 Project Structure

```
Supply-Chain-Inventory-Optimizer-Using-AI/

│
├── optimizer/
│   └── inventory_logic.py
│
├── templates/
│   ├── dashboard.html
│   ├── login.html
│   ├── register.html
│   ├── settings.html
│   ├── products.html
│   └── visuals.html
│
├── static/
│
├── models.py
├── app.py
├── config.py
├── inventory.csv
├── requirements.txt
└── README.md
```

---

# ⚙ Tech Stack

### Backend

* Python
* Flask
* SQLAlchemy

### Frontend

* HTML
* Bootstrap
* Jinja Templates

### Data Processing

* Pandas
* NumPy

### Database

* SQLite

---

# 📂 Dataset Used

The system uses:

```
inventory.csv
```

Dataset contains:

* product name
* stock quantity
* reorder level
* supplier lead time
* category

Used to generate analytics & predictions.

---

# 💻 Installation Guide

Follow these steps to run locally:

### Step 1: Clone Repository

```
git clone https://github.com/JYOTTIPODDAR/Supply-Chain-Inventory-Optimizer-Using-AI.git
```

### Step 2: Navigate into Folder

```
cd Supply-Chain-Inventory-Optimizer-Using-AI
```

### Step 3: Create Virtual Environment

```
python -m venv venv
```

Activate environment:

Windows:

```
venv\Scripts\activate
```

---

### Step 4: Install Dependencies

```
pip install -r requirements.txt
```

---

### Step 5: Run Application

```
python app.py
```

Open browser:

```
http://127.0.0.1:5000
```

---

# 🌐 Deployment Ready

Project supports deployment using:

* Render
* Gunicorn
* Flask production configuration

---

# 🎯 Future Improvements

Planned upgrades:

* Demand forecasting using ML
* Supplier recommendation engine
* Email alert automation
* REST API integration
* Cloud database support
* Role-based admin panel

---

# 👩‍💻 Author

Aryan kumar
Jyoti kumari

B.Tech CSE (AI & ML)
Aspiring AI Engineer 🚀

Deployed link:-https://supply-chain-inventory-optimizer-using-fljj.onrender.com
