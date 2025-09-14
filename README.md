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
---
## ⚙️ Features

- Predicts laptop prices from specifications  
- Handles categorical/numerical preprocessing, missing values, and outliers  
- Supports multiple regression models (Linear, Ridge, Random Forest)  
- Includes feature engineering (encoding, scaling) for better accuracy  
- Provides approximate price ranges and CSV export  
- Can be extended to a web app (Streamlit/Flask)  
- Interactive user input via CLI or GUI  
---
## 🛠️ Technologies Used

- **Python**  
- **Pandas**, **NumPy**  
- **Matplotlib**, **Seaborn**  
- **Scikit-learn**
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
## 📊 Results  

- Achieved **~90% R² Score** with Random Forest Regressor.  
- Feature scaling and encoding improved model performance.  
- **RAM size, Processor type, and GPU presence** were among the most influential features.  
- Predicted prices were on average **±10% close to actual prices**.
---
## ✍️ Author

**Ashutosh Yadav**  
B.Tech CSE (AI) | Institute of Engineering & Technology, Lucknow  

📧 [ashutosh.iet26.student@gmail.com](mailto:ashutosh.iet26.student@gmail.com)  
🔗 [LinkedIn](https://www.linkedin.com/in/ashutosh-yadav-93b303263/)

