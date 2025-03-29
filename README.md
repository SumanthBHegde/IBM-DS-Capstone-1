# SpaceX Falcon 9 First Stage Landing Prediction

## Introduction

This project aims to predict the successful landing of SpaceX Falcon 9 first stages using data science techniques. Predicting landing outcomes is crucial for optimizing launch costs and improving the efficiency of space missions. This analysis leverages data from the SpaceX API, web scraping, and machine learning models to identify key factors influencing landing success.

## Business Understanding

SpaceX has revolutionized space exploration by making rocket reusability a reality. The first-stage booster of the Falcon 9 rocket plays a crucial role in this endeavor, as a successful landing enables cost savings and rapid turnaround for future missions. This project seeks to answer:

- How do payload mass, launch site, and orbit type affect first-stage landing success?
- Can we accurately predict Falcon 9 first-stage landing outcomes using machine learning models?
- What are the most influential factors driving successful landings?

## Data Understanding

The dataset consists of launch data obtained from multiple sources:

1. **SpaceX API**: Used to gather structured launch data.
2. **Web Scraping**: Employed BeautifulSoup to collect historical launch records from Wikipedia.
3. **CSV Dataset**: Processed and cleaned launch data stored in `spacex_launch_dash.csv`.

## Methodology

The project follows a comprehensive data science workflow:

### 1. Data Collection

- Used the SpaceX REST API to gather historical launch data.
- Scraped launch records from Wikipedia using BeautifulSoup.

### 2. Data Wrangling

- Handled missing values and cleaned inconsistencies.
- Created a binary "Class" label (1 for successful landing, 0 for failure).
- Transformed categorical variables using one-hot encoding.

### 3. Exploratory Data Analysis (EDA)

- Visualized relationships between features and landing outcomes using Seaborn and Matplotlib.
- Used SQL queries to extract targeted insights about launch sites, payload mass, and mission characteristics.
- Created interactive visualizations using Folium and Plotly Dash.

### 4. Machine Learning Model Development

- Implemented multiple classification models:
  - Logistic Regression
  - Support Vector Machine (SVM)
  - Decision Tree
  - K-Nearest Neighbors (KNN)
- Used GridSearchCV for hyperparameter tuning.
- Compared model accuracy and analyzed confusion matrices.

## Key Findings

- Launch success rates have improved over time.
- Launch site and orbit type significantly influence landing outcomes.
- Decision Tree showed slight advantage, but performance was generally consistent across models.
- Model performance is limited by dataset size and imbalanced class distribution.

## Repository Structure

This repository contains the following files:

```
|-- notebooks/
|   |-- 1_data_collection.ipynb         # SpaceX API data extraction
|   |-- 2_web_scraping.ipynb            # Web scraping launch data from Wikipedia
|   |-- 3_data_wrangling.ipynb          # Data preprocessing and feature engineering
|   |-- 4_exploratory_data_analysis.ipynb # EDA and data visualization
|   |-- 5_machine_learning.ipynb        # Machine learning model development
|
|-- spacex_launch_dash.csv              # Cleaned dataset for analysis
|-- spacex_dash_app.py                   # Plotly Dash dashboard script
|-- README.md                            # Project documentation
```

## Next Steps

To further enhance the project, future research could focus on:

- Expanding the dataset with additional features and data sources.
- Exploring advanced feature engineering techniques.
- Implementing more sophisticated machine learning models (e.g., XGBoost, Neural Networks).
- Developing a real-time dashboard for monitoring launch outcomes.

## Author

Sumanth Hegde
