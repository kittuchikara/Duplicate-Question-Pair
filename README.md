# 🔥 Duplicate Question Detection Web App
A machine learning web application that predicts whether two questions have the same meaning using the Quora Question Pairs Kaggle dataset.

# Project Overview
This project tackles a real-world NLP challenge posed by Quora. The goal is to detect duplicate questions using machine learning techniques.

# 🧠 Model Overview
Algorithm: Random Forest, XGBoost
Preprocessing: Text cleaning, feature engineering (length difference, common words, longest common substring etc)
Text Representation: CountVectorizer
Libraries: scikit-learn, pandas, numpy, streamlit

# 💬 Input Features
This app takes the following as input:

Question 1

Question 2

# ✨ Features
🔍 Predict if two questions are duplicates
🧠 ML models trained from scratch using CountVectorizer and engineered features
🌐 Interactive Streamlit web app for local testing
🎨 Simple, user-friendly interface

# 🛠️ Tech Stack
Backend: Python
Machine Learning: scikit-learn, XGBoost, Pandas, Numpy
Frontend: Streamlit

# 🌟 Key Learnings & Insights
Efficient handling of large NLP datasets
Combining feature engineering with text vectorization improves semantic similarity detection
Random Forest outperforms other models in minimizing false positives (Type I errors)
Building a local interactive web interface for testing ML models

# 🧠 Future Improvements
💡 Experiment with deep learning models (LSTMs / Transformers)
🌐 Deploy online via Heroku, Render, or Streamlit Cloud
