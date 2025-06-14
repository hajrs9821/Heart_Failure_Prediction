# 🫀 Heart Failure Prediction with Machine Learning and Neural Network

This project predicts the risk of heart failure using clinical data such as `serum_creatinine`, `ejection_fraction`, and `time`. It includes both machine learning and neural network models to assist in early detection of heart failure. An interactive web app is also built using **Streamlit**.

---

## 📊 Features Used
- `time`: Duration of follow-up (in days)
- `serum_creatinine`: Level of serum creatinine in the blood
- `ejection_fraction`: Percentage of blood leaving the heart at each contraction

---

## 🧠 Models Applied
- K-Nearest Neighbors (KNN)
- Random Forest
- Support Vector Machine (SVM)
- Gradient Boosting
- Neural Network (using TensorFlow / Keras)

---

## 🚀 Web App (Streamlit)
The project includes a simple Streamlit web app where users can input patient data and get real-time predictions.

### Example inputs:
- `serum_creatinine`: 1.2
- `ejection_fraction`: 35
- `time`: 140

---

## 📁 Project Structure

Heart_Failure_Prediction/
│
├── app.py  # Streamlit app
├── heart-failure-prediction.ipynb  # Notebook for training & evaluation
├── scaler.pkl
├── KNNclassifier.pkl  # Saved ML model  best model
├── README.md # Project documentation     
├── requirements.txt   Dependencies
├── image_Streamlit/ 
│   ├── die.png
│   └── survive.png
---

## 🛠️ How to Run Locally

### 1. Clone the Repository
```bash
git clone https://github.com/hajrs9821/Heart_Failure_Prediction.git
cd Heart_Failure_Prediction

# Create a Virtual Environment (Optional but Recommended)
conda create -n heart_project python=3.10
conda activate heart_project
#Install Dependencies
pip install -r requirements.txt
#Run the Streamlit App
streamlit run app.py

🧪 Model Evaluation
Models were evaluated using:

Accuracy

Precision

Recall

F1 Score

Confusion Matrix

Classification Report

Graphs were plotted using Matplotlib and Seaborn.


🔗 GitHub Repository
This repository contains all code, models, and resources related to the Heart Failure Prediction project.

🔗 Chttps://github.com/hajrs9821/Heart_Failure_Prediction

📄 License
This project is licensed under the MIT License.

✨ Author
Made with ❤️ by Hagar Saeed



