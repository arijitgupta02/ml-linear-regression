# Linear Regression on California Housing Dataset

Project Overview
-----------------
This project demonstrates an **end-to-end Machine Learning workflow** using **Linear Regression** to predict median house values based on socio-economic and geographical features from the California Housing dataset.

The project covers data loading, exploratory data analysis (EDA), model training, evaluation, and saving the trained model for future predictions.

---

Dataset
-------
- **Name:** California Housing Dataset
- **Source:** scikit-learn (built-in dataset)
- **Number of records:** 20,640
- **Number of features:** 8
- **Target variable:** Median House Value

Features
--------
- Median Income  
- House Age  
- Average Rooms  
- Average Bedrooms  
- Population  
- Average Occupancy  
- Latitude  
- Longitude  

---

Exploratory Data Analysis (EDA)
-------------------------------
The following EDA steps were performed:
- Checked dataset structure and data types
- Verified that there are **no missing values**
- Generated descriptive statistics
- Created a **correlation heatmap** to analyze relationships between features

Key Insight
------------
- Median income shows a strong positive correlation with house value.
- Some features show weak linear correlation, indicating non-linear patterns.

---

Model & Methodology
--------------------
- **Algorithm:** Linear Regression
- **Library:** scikit-learn
- **Train-Test Split:** 80% training, 20% testing
- **Reason for choosing Linear Regression:**  
  - Simple and interpretable  
  - Strong baseline model for regression problems

---

Model Evaluation
-----------------
The model was evaluated using standard regression metrics:

| Metric | Value |
|------|------|
| MAE | 0.53 |
| RMSE | 0.75 |
| R² Score | 0.58 |

---

Interpretation
---------------
- The model explains approximately **58% of the variance** in median house prices.
- RMSE being higher than MAE indicates the presence of some larger prediction errors.
- Performance is reasonable for a baseline linear model.

---

Visualizations
----------------
- Correlation heatmap
- Actual vs Predicted values plot
- Residuals plot

These visualizations help assess model behavior and error distribution.

---

Improvements & Future Work
---------------------------
- Feature scaling using StandardScaler
- Regularization techniques (Ridge, Lasso)
- Tree-based models (Random Forest, Gradient Boosting)
- Feature engineering and interaction terms

---

Repository Contents
--------------------
- `task1_ml_linear_regression.ipynb` – Jupyter Notebook containing code, plots, and comments
- `Linear_Regression_Report.pdf` – Short project report summarizing EDA, model, and results
- `linear_regression_model.pkl` – Saved trained model
- `predict_ui.py` – Simple CLI script to predict on new inputs

---

How to Run the Project
-----------------------

1> Install Dependencies
   - pip install -r requirements.txt

2️> Run Jupyter Notebook
   - jupyter notebook

3> (Optional) Run Prediction Script
   - python predict_ui.py

---

Tech Stack
------------

  -Python
  -NumPy
  -pandas
  -scikit-learn
  -matplotlib
  -seaborn
  -Jupyter Notebook

Author
-------
Arijit Gupta
