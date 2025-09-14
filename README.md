# 💻 Laptop Price Predictor

A Python-based project that predicts the price of a laptop given its specifications using **Machine Learning**. This project leverages **data preprocessing**, **feature engineering**, and regression models to estimate realistic laptop prices.

---

## 📝 Project Overview

The Laptop Price Predictor takes key laptop specifications such as brand, processor, RAM, storage, GPU, and OS to predict the approximate market price. It is designed for **buyers, sellers, and tech enthusiasts** who want to make informed decisions.

---
## 📂 Dataset

The project uses a **laptop specifications dataset** to train the model. It contains features like brand, processor, RAM, storage, GPU, OS, and price.  

- **Dataset Link:** [Kaggle Laptop Price Dataset](https://www.kaggle.com/datasets/ganeshmohane/laptop-datacsv)  
- **Format:** CSV  
- **Size:** ~182 kb  
- **Columns:** Brand, Processor, RAM, Storage, GPU, OS, Screen Size, Price  

> ⚡ Note: Preprocessing (handling missing values, encoding categorical features) is required before training.

---
## ⚙️ Features

- Predict laptop prices based on specifications  
- Preprocessing of categorical and numerical features  
- Handles missing values and outliers  
- Model evaluation with key metrics like R², MSE, RMSE, and MAE  
- Interactive user input support (via CLI or GUI, depending on implementation)  
- Supports multiple regression models (Linear, Ridge, Random Forest)  
- Feature engineering for better accuracy (e.g., encoding, scaling)   
- Provides approximate price ranges for better market insight    
- Can be extended to a web application using Streamlit or Flask  
- Export predictions to CSV for further analysis  
- Modular code structure for easy maintenance and upgrades  

---


## 📊 Model Evaluation

The model was evaluated using the following metrics on the test dataset:

| Metric | Value |
|--------|-------|
| R² Score | 0.9012|
| Mean Squared Error (MSE) | 0.014 |
| Root Mean Squared Error (RMSE) | 0.118 |
| Mean Absolute Error (MAE) | 0.089 |

---

## 🛠️ Installation

1. Clone the repository:

```bash
git clone <repo-url>
cd laptop_price_predictor
