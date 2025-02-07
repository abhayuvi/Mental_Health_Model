# Self-Analysis-Mental-Health-Model-With-Integrated-LLM

This Repository is made to create a Mental Health Model which can analyse itself also having a integrated chatbot using LLM within it .

## Instructions:-

- Dataset used to train the mode is [Mental Health In Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)
- clone the repository and setup in your environment.
- Run the requirements.txt file . `pip install -r requirements.txt`
- Get into the Directory . `cd Mental_Health_Model`
- Run `streamlit run app.py`
- To Run inference script , Run `python predict_mental_health.py`
- Run `streamlit run app.py` to use web based UI.

## 📁 Project Directory Overview

| 📁 Directory | 📄 Files | 📝 Description |
|-------------|---------|---------------|
| **LLm/** | `llm.py`, `app.py`, `phi-2 model` | Contains the LLM model, and code base of chatbot and chatbot UI. |
| **mental_health_ui/** | `app.py`, `best_model.pkl`, `poly.pkl`, `scaler.pkl` | UI and pre-trained ML model files. |
| *(Root Folder)* | `Readme.md`, `predict_mental_health.py`, `requirements.txt`, `source_code.ipynb` | Documentation, main inference script, dependencies, and code notebook. |

#### Report on LLM Experimentation can be seen [Here](https://docs.google.com/document/d/1DXcLIiOPVwPwLUHLI4pOqboWF2w5g5ksls4l15v-1PQ/edit?usp=sharing)

### Preprocessing Steps
- Handling Missing Values - Missing data is imputed or removed.
- Encoding Categorical Variables - Categorical features are converted into numerical representations using label encoding.
- Feature Scaling - Standardization is applied to ensure uniformity across features.
- Feature Selection - Irrelevant or redundant features are removed to optimize performance.
- Train-Test Split - The dataset is split into training and testing subsets.

### Models Used
- The following models have been implemented and evaluated:

1. Logistic Regression
2. Random Forest Classifier
3. Neural Network
- Further we used Logistic Regression model after the Evaluation because it outperformed all the evaluation metrics.

### Model Evaluation
- Each model is evaluated using:

1. Accuracy
2. Precision, Recall, and F1-score
3. Confusion Matrix
4. ROC-AUC Score

- To enhance interpretability, Local Interpretable Model-agnostic Explanations (LIME) is used to provide insights into individual predictions.

  ### Video Demonstration of the Project walkthrough can be seen [Here](##)

