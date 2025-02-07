# Self-Analysis-Mental-Health-Model-With-Integrated-LLM

This Repository is made to create a Mental Health Model which can analyse itself also having a integrated chatbot using LLM within it .

## Instructions:-

- Dataset used to train the mode is [Mental Health In Tech Survey](https://www.kaggle.com/datasets/osmi/mental-health-in-tech-survey)
- clone the repository and setup in your environment.
- Run the requirements.txt file . `pip install -r requirements.txt`
- Get into the Directory . `cd Mental_Health_Model`
- Run `streamlit run app.py`

## 📁 Project Directory Overview

| 📁 Directory | 📄 Files | 📝 Description |
|-------------|---------|---------------|
| **LLm/** | `llm.py`, `app.py`, `phi-2 model` | Contains the LLM model, and code base of chatbot and chatbot UI. |
| **mental_health_ui/** | `app.py`, `best_model.pkl`, `poly.pkl`, `scaler.pkl` | UI and pre-trained ML model files. |
| *(Root Folder)* | `Readme.md`, `predict_mental_health.py`, `requirements.txt`, `source_code.ipynb` | Documentation, main inference script, dependencies, and code notebook. |

Report can LLM Experimentation can be seen [Here](https://docs.google.com/document/d/1DXcLIiOPVwPwLUHLI4pOqboWF2w5g5ksls4l15v-1PQ/edit?usp=sharing)

