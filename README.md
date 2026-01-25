# AI-Powered Garbage Detection for Water Body Protection

## 📖 Project Overview
This project is a Streamlit-based AI prototype designed to support cleanliness and environmental sustainability initiatives. The application analyzes images of streets or water bodies and provides garbage detection insights along with cleanup priority recommendations.

The system uses a simple, explainable rule-based AI approach to demonstrate decision-support logic for environmental monitoring.

---

## 🎯 Objectives
- Assist in identifying garbage in streets and water bodies
- Suggest cleanup priority and recommended actions
- Promote clean and sustainable environments
- Demonstrate AI-driven decision support using a web interface

---

## 🧠 AI Approach
- Rule-based AI logic (explainable and transparent)
- User-selected area type influences severity and action
- Designed as a prototype for future ML/DL integration

⚠️ Note: This project does not use a trained ML model yet. It focuses on logic-based AI decision support.

---

## 🖼️ Input
- User uploads an image (street / road / river / lake)
- Supported formats: JPG, JPEG, PNG
- User selects the area type:
  - Street / Road
  - Water Body (River / Lake)

---

## ⚙️ Application Workflow
1. User uploads an image
2. Image is displayed using Streamlit
3. Area type is selected
4. AI logic analyzes the input
5. Results are displayed:
   - Garbage detected
   - Area type
   - Severity level
   - Recommended cleanup action

---

## 📊 AI Decision Logic
- Default severity: **Moderate**
- If area type is **Water Body**:
  - Severity: **Severe**
  - Action: Immediate cleanup required (High Environmental Risk)

This logic ensures explainability and clarity for decision-makers.

---

## 🛠️ Technologies Used
- Python
- Streamlit
- PIL (Python Imaging Library)

---

## 🚀 How to Run the Project
```bash
git clone https://github.com/YaraAkshara/AI-Powered-Garbage-Detection-Water-Body-Protection-System.git
cd AI-Powered-Garbage-Detection-Water-Body-Protection-System
pip install streamlit pillow
streamlit run clean_india_project.py

