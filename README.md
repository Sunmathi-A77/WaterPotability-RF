# 💧 Water Potability Prediction

## Project Overview

This project focuses on predicting whether water is **safe for drinking** based on its chemical properties. Using a **Random Forest Classifier**, we trained a model on the Water Potability dataset to detect potable water. The model also incorporates **threshold tuning** for better real-world performance.

The solution is deployed as a **Streamlit web application**, allowing users to input water quality parameters and get predictions instantly.

## 🔗 App Link

[Water Potability Predictor Web App](https://waterpotability-rf.streamlit.app/)  

## 📂 Dataset

The dataset used is the **Water Potability Dataset** from Kaggle:  
[Kaggle Water Potability Dataset](https://www.kaggle.com/adityakadiwal/water-potability)  

- Features include: `ph`, `Hardness`, `Solids`, `Chloramines`, `Sulfate`, `Conductivity`, `Organic_carbon`, `Trihalomethanes`, `Turbidity`.  
- Target: `Potability` (1 = Potable, 0 = Not Potable)

## 🛠 Installation Steps

1. Clone the repository:
   git clone
   cd
   
2. (Optional) Create a virtual environment:

python -m venv myvenv
myvenv\Scripts\activate   # Windows
source myvenv/bin/activate # macOS/Linux

3. Install dependencies:

pip install -r requirements.txt

4. Run the Streamlit app:

streamlit run app.py

## 📝 Steps Performed

Data Loading and Inspection

Loaded water_potability.csv and checked shape, info, null values, duplicates.

### Exploratory Data Analysis (EDA)

Filled missing values with median.

Checked skewness and visualized distributions using histograms.

Performed outlier analysis with boxplots.

Clipped outliers to reduce their effect.

### Correlation Analysis

Plotted correlation heatmap to understand feature relationships.

### Feature Selection

Separated features X and target y.

### Train-Test Split

Split dataset into training and testing sets with stratify to maintain class distribution.

### Balancing Classes

Used RandomOverSampler from imbalanced-learn to handle class imbalance.

### Model Training

Trained Random Forest Classifier with tuned hyperparameters.

Used class weights to handle imbalance.

### Prediction and Thresholding

Predicted probabilities and applied a threshold of 0.42 for potable detection.

### Evaluation

Calculated Accuracy, Confusion Matrix, and Classification Report.

Checked Feature Importance.

### Model Saving

Saved trained model as rf_water_model.pkl using pickle.

## 🛠 Libraries & Technologies Used

Python Libraries

pandas, numpy – Data manipulation

matplotlib, seaborn – Data visualization

scikit-learn – Model training and evaluation

imbalanced-learn – Handling imbalanced datasets

pickle – Model serialization

streamlit – Web app deployment

## 📈 Features & Functionality in App

User-friendly web interface to input water parameters.

Outputs potable or non-potable prediction along with probability.

Threshold tuning allows real-world sensitivity adjustment.

Visual cues for prediction: ✅ for safe, ❌ for unsafe water.
