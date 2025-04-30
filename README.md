# Food_Recommendation_System

Personalized Food Recommendation System

FoodBuddy AI is a smart, ML-powered food recommendation system built with Django and Python. It helps users understand their daily nutritional needs and recommends foods based on their personal attributes like age, gender, weight, height, and activity level.

The goal is to bridge health awareness and machine intelligence using intuitive UI and efficient recommendations — all themed in a clean white and orange aesthetic.

---

## 📌 Features

- Calculates personalized daily calorie and nutrient requirements.
- Recommends top food items based on the user’s profile.
- Interactive UI built with Django templates.
- Industry-level visual design using HTML and CSS.
- Accurate recommendations using real food datasets.

---

## 🚀 Technology Stack

- **Frontend:** HTML5, CSS3, Bootstrap
- **Backend:** Python, Django
- **Others:** Pandas, Numpy, Scikit-learn

---

## 🤖 Machine Learning Algorithms Used

We used the following machine learning techniques and strategies in the backend for intelligent food matching:

- **K-Nearest Neighbors (KNN):**  
  To find foods closest in nutritional values to the user's ideal intake.
  
- **Feature Scaling (MinMaxScaler):**  
  Applied normalization for better accuracy in similarity comparisons.
  
- **Cosine Similarity / Euclidean Distance:**  
  Used for ranking food items based on their nutritional closeness to user needs.

---

## 🛠️ Installation & Setup

Follow the steps below to set up this project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/foodbuddy-ai.git
cd foodbuddy-ai
