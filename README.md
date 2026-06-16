# 📊 Retail Customer Churn Prediction

[![Live Demo](https://img.shields.io/badge/Live-Demo-green)](https://retail-customer-churn-prediction-model.onrender.com)

## Project Overview

Customer churn is one of the most important business challenges in the retail industry. Retaining existing customers is often more cost-effective than acquiring new ones.

This project develops a Machine Learning-based churn prediction system that identifies customers who are likely to discontinue their engagement with a retail business. The trained model is integrated into a Streamlit application, allowing users to generate churn predictions through an interactive web interface.

---

## Business Problem

Retail companies collect large amounts of customer transaction and engagement data. Understanding which customers are likely to churn helps businesses:

* Improve customer retention strategies
* Reduce revenue loss
* Target high-risk customers proactively
* Optimize marketing campaigns

The objective of this project is to predict whether a customer is likely to churn based on behavioral and transactional attributes.

---

## Dataset Features

The model utilizes various customer behavior metrics including:

* Purchase Frequency
* Average Order Value
* Total Spending
* Recency Days
* Website Visits
* Discount Usage Rate
* Email Open Rate
* Product Return Rate
* Customer Satisfaction Score
* Customer Segment Information

Target Variable:

* **Churn Flag**

  * 0 → Active Customer
  * 1 → Churned Customer

---

## Project Workflow

### 1. Data Preprocessing

The dataset was cleaned and prepared before model training.

Steps performed:

* Removed unnecessary columns
* Checked duplicate records
* Handled categorical variables using One-Hot Encoding
* Standardized numerical features using StandardScaler
* Created preprocessing pipelines using ColumnTransformer

---

### 2. Exploratory Data Analysis (EDA)

Several visualizations were created to understand customer behavior:

* Churn distribution analysis
* Numerical feature distributions
* Correlation heatmap
* Customer engagement patterns

These analyses helped identify the factors influencing customer churn.

---

### 3. Model Development

Multiple machine learning algorithms were trained and compared:

| Model                  |
| ---------------------- |
| Logistic Regression    |
| Random Forest          |
| Gradient Boosting      |
| Extra Trees Classifier |

A Scikit-Learn Pipeline was used to combine preprocessing and model training into a single workflow.

---

### 4. Cross Validation

To improve model reliability, Stratified K-Fold Cross Validation was applied:

* 5 Folds
* Stratified sampling
* Consistent class distribution across folds

This ensured robust model evaluation and reduced overfitting risk.

---

### 5. Model Evaluation

The models were evaluated using:

* Accuracy
* Precision
* Recall
* F1 Score
* ROC-AUC Score
* Confusion Matrix

After comparison, the best-performing model was selected and saved for deployment.

---

### 6. Model Explainability

To improve transparency and interpretability:

#### Feature Importance Analysis

The most influential features affecting churn prediction were identified and visualized.

#### SHAP (SHapley Additive exPlanations)

SHAP was used to explain:

* Individual predictions
* Global feature impact
* Customer-level churn drivers

This helps business users understand why a customer is predicted to churn.

---

## Application Development

The trained model was integrated into a Streamlit application.

### Features

* Interactive prediction interface
* Real-time churn prediction
* About Page
* User Feedback Page
* Responsive dashboard design

---

## Project Structure

```text
Retail-Customer-Churn-Prediction/
│
├── Retail Customer Churn Prediction.ipynb
├── retail_customer_churn_100k (1).csv
├── churn_prediction_app.py
├── churn_prediction.pkl
├── requirements.txt
├── Dockerfile
├── README.md
│
├── assets/
│   ├── images
│   └── styles
│
├── pages/
    ├── about.py
    └── feedback.py
```

---

## Running the Streamlit Application

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Start the Application

```bash
streamlit run churn_prediction_app.py
```

The application will launch locally in your browser.

---

## Docker Deployment

### Build Docker Image

```bash
docker build -t churn-prediction-app .
```

### Run Docker Container

```bash
docker run -p 8501:8501 churn-prediction-app
```

Open:

```text
http://localhost:8501
```

to access the application.

---

## Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Visualization

* Matplotlib
* Seaborn

### Machine Learning

* Scikit-Learn

### Explainable AI

* SHAP

### Deployment

* Streamlit
* Docker

---

## Future Enhancements

* Hyperparameter tuning
* Model monitoring
* Cloud deployment (AWS/Azure/GCP)
* Automated retraining pipeline
* Real-time customer churn tracking

---

## Author

**Vimal Raj R**

Data Science | Machine Learning | Predictive Analytics
