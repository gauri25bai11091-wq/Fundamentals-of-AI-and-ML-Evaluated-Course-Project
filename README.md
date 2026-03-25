

# 💸 Smart Expense Tracker

## 1. Project Overview
The **Smart Expense Tracker** is a Python-based Streamlit application that allows users to **track, analyze, and predict daily expenses**, helping them make smarter financial decisions.  

**Key Goals:**
- Track daily spending by category and date  
- Summarize expenses via charts (monthly, category-wise)  
- Predict next expense using Machine Learning  
- Simulate savings with a What-If calculator  
- Provide quick financial tips using a rule-based chatbot  

This project demonstrates **Python, Streamlit, data analysis, and basic AIML concepts** in a practical application.

---

## 2. Features

| Feature | Description |
|---------|-------------|
| Add Expense | Enter date, category, amount, and description |
| View Expenses | Filter, delete last entry, or clear all expenses |
| Summary | Shows total, monthly, and category-wise spending charts |
| Expense Prediction | Predicts next expense using Linear Regression |
| What-If Calculator | Simulate future savings based on hypothetical inputs |
| Chatbot | Rule-based assistant providing financial tips |

---


## 4.🛠️ Tech Stack

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-learn

---

## 5.📂 Project Structure

Expense_tracker


├── README.md                  # Project overview, setup instructions, usage, deployment link


├── app.py                      # Main Streamlit app containing all features


├── requirements.txt            # Python dependencies for running the app


├── expenses.csv                # Optional sample CSV data for the app


├── project_report.pdf          # Detailed report for BYOP submission


---

## 6.⚙️ Setup Instructions

a) Clone the repository

git clone <https://github.com/gauri25bai11091-wq/Fundamentals-of-AI-and-ML-Evaluated-Course-Project>


cd <Expense_Tracker>

b) Create virtual environment

python -m venv venv
venv\Scripts\activate   # Windows

c) Install dependencies

pip install -r requirements.txt

---
 
## 7. Live Demo📍

The app is deployed on Streamlit Community Cloud. Access it here:

https://fundamentals-of-ai-and-ml-evaluated-course-project-jjzhsxpycny.streamlit.app/

Open Smart Expense Tracker Online

Any updates pushed to GitHub will automatically update the online app.

## Run Locally  (optional)

To run the app locally, open terminal in the project folder and run:
streamlit run app.py
> Note: This step is only needed if you want to run the app locally. The online demo works directly in your browser.

---

## 8.📊 How to Use

- Use sidebar to navigate:
  - Add Expense → add new data
  - View Expenses → see & filter
  - Summary → charts & prediction
  - Chatbot → financial tips

---

## 9.📌 Notes

- If no data exists, sample data is automatically loaded
- Data is stored locally in "expenses.csv"

---

## 10.📈 Future Improvements

- User authentication
- Cloud database integration
- Advanced ML predictions
- UI improvements

---

Prepared By: Gauri Gupta


Course: VIT BYOP (Bring Your Own Project)


GitHub Repository: https://github.com/gauri25bai11091-wq/Fundamentals-of-AI-and-ML-Evaluated-Course-Project


Streamlit Deployment: https://fundamentals-of-ai-and-ml-evaluated-course-project-jjzhsxpycny.streamlit.app/

