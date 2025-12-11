## 🩺 Maternal Health Risk Prediction (ML Project)

This project predicts maternal health risk levels — Low, Medium, High — based on key clinical parameters such as Age, Blood Pressure, Heart Rate, Blood Sugar, and Body Temperature.
It uses a Machine Learning model trained on a real healthcare dataset and provides an interactive Streamlit web app for real-time predictions.

## 🔍 Project Overview

Maternal health risks can be identified early using ML models.
This project:

-Loads the dataset and processes important features
-Trains ML classification models
-Evaluates accuracy and performance
-Deploys a simple web app for prediction

## 🧠 Technologies Used

Python
Machine Learning (Scikit-learn)
Pandas & NumPy
Matplotlib / Seaborn
Jupyter Notebook
Streamlit
Git & GitHub

## 📁 Project Structure
Maternal-Health-Risk-Prediction/
│
├── train_model.py          # ML model training script
├── app.py                  # Streamlit app for prediction
├── Maternal Health Risk.csv # Dataset
├── Maternal Health Risk.ipynb # Notebook with analysis & training
├── model.pkl               # Saved ML model
└── README.md               # Project documentation

## 🚀 How to Run the Project
1️⃣ Create Virtual Environment
python -m venv venv

2️⃣ Activate Environment
venv\Scripts\activate

3️⃣ Install Requirements
pip install -r requirements.txt

4️⃣ Run Streamlit App
streamlit run app.py

| Parameter        | Description              |
| ---------------- | ------------------------ |
| Age              | Age of the mother        |
| Systolic_BP      | Systolic blood pressure  |
| Diastolic_BP     | Diastolic blood pressure |
| Blood Sugar      | Blood sugar level        |
| Body Temperature | Recorded temperature     |
| Heart Rate       | BPM                      |


## 🧪 Output

The model predicts Low, Medium, or High maternal health risk.

The Streamlit UI shows live prediction based on user input.

🌐 Live Demo:

https://3sqjismwjx3vbfukxfoc6u.streamlit.app/
