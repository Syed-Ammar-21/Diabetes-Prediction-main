🧠 DiabAI: Smart Diabetes Detection Using Deep Learning

[![Python](https://img.shields.io/badge/Python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-App-FF4B4B.svg)](https://streamlit.io)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)


This project demonstrates a machine learning solution for predicting diabetes based on user-provided health data. The application uses **Streamlit** for an interactive web interface and advanced interpretability tools like **SHAP** and **Permutation Importance** to explain model predictions.


> **⚠️ Disclaimer:** This project is for educational purposes only and is not a medical diagnostic tool.

![Home](./Home.jpg)

---




## Overview
This application allows users to enter health data and receive:
- **Diabetes Risk Prediction**: Real-time analysis of input data.
- **Probability Score**: Quantitative likelihood of diabetes.
- **XAI (Explainable AI)**: Detailed visualization of feature contributions using SHAP.

The model was developed based on the ROC AUC metric, while efforts were made to improve the **Recall** metric when selecting the threshold, as this decision was made due to the medical context and for experimental/testing purposes.


---

## Dataset

The dataset is sourced from the **National Institute of Diabetes and Digestive and Kidney Diseases**. It includes:

The dataset contains the following details:

### General Overview
- **Number of rows:** 768
- **Number of columns:** 9
- **Column names and data types:**
  - `Pregnancies` (int64): Number of times pregnant.
  - `Glucose` (int64):  Plasma glucose concentration a 2 hours in an oral glucose tolerance test.
  - `BloodPressure` (int64): Diastolic blood pressure (mm Hg).
  - `SkinThickness` (int64): Triceps skin fold thickness (mm).
  - `Insulin` (int64): 2-Hour serum insulin (mu U/ml).
  - `BMI` (float64): Body mass index (weight in kg/(height in m)^2).
  - `DiabetesPedigreeFunction` (float64): Diabetes pedigree function.
  - `Age` (int64): Age (years).
  - `Outcome` (int64): Class variable (0 or 1).

### Sample Data (First 5 Rows)
| Pregnancies | Glucose | BloodPressure | SkinThickness | Insulin |  BMI  | DiabetesPedigreeFunction | Age | Outcome |
|-------------|---------|---------------|---------------|---------|-------|---------------------------|-----|---------|
| 6           | 148     | 72            | 35            | 0       | 33.6  | 0.627                     | 50  | 1       |
| 1           | 85      | 66            | 29            | 0       | 26.6  | 0.351                     | 31  | 0       |
| 8           | 183     | 64            | 0             | 0       | 23.3  | 0.672                     | 32  | 1       |
| 1           | 89      | 66            | 23            | 94      | 28.1  | 0.167                     | 21  | 0       |
| 0           | 137     | 40            | 35            | 168     | 43.1  | 2.288                     | 33  | 1       |

### Statistical Summary
- **Pregnancies:** Mean = 3.85, Max = 17
- **Glucose:** Mean = 120.89, Min = 0 (possible missing values)
- **BloodPressure:** Mean = 69.11, Min = 0 (possible missing values)
- **SkinThickness:** Mean = 20.54, Min = 0 (possible missing values)
- **Insulin:** Mean = 79.80, Min = 0 (possible missing values)
- **BMI:** Mean = 31.99, Min = 0 (possible missing values)
- **DiabetesPedigreeFunction:** Mean = 0.47, Max = 2.42
- **Age:** Mean = 33.24, Max = 81
- **Outcome:** Proportion of `1` (positive diabetes) = 34.9%


#### We use only `Pregnancies`, `Glucose`, `BMI`, `Insulin`, `Age` for prediction.


---


## Model
You can learn more about the model in detail from [here](notebooks/Model.ipynb). The `RandomForestClassifier` model was chosen through experimentation and showed the best performance. The required hyperparameters were identified using the `optuna` optimizer. For the model to function, it needs `FeatureEngineering`, `WoEEncoding`, and `ColumnSelector` transformers, which are combined through a pipeline.
`Cross-validation` and `ROC AUC` were used for model selection because the number of observations was small, and splitting into test/train sets would have been inaccurate.


---

## Features

1. **Interactive Input**: Enter health parameters (Pregnancies, Glucose, Insulin, BMI, Age).
2. **Diabetes Prediction**: Real-time risk prediction with probability.
3. **SHAP Explanations**: Visualize individual prediction explanations using:
   - Waterfall Plot
   - Force Plot
4. **Permutation Importance**: Analyze which features most influence the predictions.
5. **Performance Metrics**:
   - Accuracy
   - Precision
   - Recall
   - F1 Score
   - ROC AUC
6. **Informational Section**: Learn about diabetes risk factors in the "About" section.

---

## Installation

### Prerequisites
- Python 3.10 or above
- Pip package manager

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/Syed-Ammar-21/DiabAI.git
   cd DiabAI
   ```

2. Install required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Run the application locally:
   ```bash
   python -m venv venv (on windows terminal )
   .\venv\Scripts\activate
python -m streamlit run main.py
  

---

## Project Structure

![Project Structure](./folder-structure.jpg)

---

## Model Performance

Performance metrics calculated:
- **Accuracy**: Percentage of correct predictions. (0.7857)
- **Precision**: Ratio of true positives to total positive predictions. (0.6296)
- **Recall**: Ratio of true positives to total actual positives. (0.9444)
- **F1 Score**: Harmonic mean of Precision and Recall. (0.7556)
- **ROC AUC**: Area under the ROC curve. (0.8367)

Metrics are displayed as donut charts in the application.

---

## Project Motivation

This project was developed to:
- Build knowledge in machine learning, especially in healthcare.
- Gain hands-on experience with model interpretability techniques like SHAP.
- Deploy an AI solution using **Streamlit**.

---

##  Deployment

---

## 📜 License
Distributed under the MIT License. See `LICENSE` for more information.



