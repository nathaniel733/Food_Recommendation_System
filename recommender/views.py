from django.shortcuts import render
import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans

# Load data once globally
df1 = pd.read_csv('recommender/static/FOOD-DATA-GROUP1.csv')
df2 = pd.read_csv('recommender/static/FOOD-DATA-GROUP2.csv')
df3 = pd.read_csv('recommender/static/FOOD-DATA-GROUP3.csv')
df4 = pd.read_csv('recommender/static/FOOD-DATA-GROUP4.csv')
df5 = pd.read_csv('recommender/static/FOOD-DATA-GROUP5.csv')
df = pd.concat([df1, df2, df3, df4, df5], ignore_index=True)
df = df[['food', 'Caloric', 'Protein', 'Fat', 'Carbohydrates']].dropna()

# Cluster similar foods
scaler = StandardScaler()
X = scaler.fit_transform(df[['Caloric', 'Protein', 'Fat', 'Carbohydrates']])
kmeans = KMeans(n_clusters=5, random_state=42)
df['Cluster'] = kmeans.fit_predict(X)

def calculate_bmr(age, gender, height_cm, weight_kg):
    if gender.lower() == 'male':
        return 10 * weight_kg + 6.25 * height_cm - 5 * age + 5
    else:
        return 10 * weight_kg + 6.25 * height_cm - 5 * age - 161

def daily_needs(age, gender, height, weight, activity='moderate'):
    multiplier = {
        'sedentary': 1.2,
        'light': 1.375,
        'moderate': 1.55,
        'active': 1.725,
        'very active': 1.9
    }
    bmr = calculate_bmr(age, gender, height, weight)
    calories = bmr * multiplier.get(activity, 1.55)
    return {
        'Calories': round(calories),
        'Protein': round((0.2 * calories) / 4),
        'Fat': round((0.3 * calories) / 9),
        'Carbohydrates': round((0.5 * calories) / 4)
    }

def home(request):
    return render(request, 'recommender/home.html')

def recommend(request):
    if request.method == 'POST':
        age = int(request.POST['age'])
        gender = request.POST['gender']
        height = int(request.POST['height'])
        weight = int(request.POST['weight'])
        activity = request.POST['activity']
        
        needs = daily_needs(age, gender, height, weight, activity)

        df['score'] = (
            abs(df['Caloric'] - needs['Calories']/3) +
            abs(df['Protein'] - needs['Protein']/3) +
            abs(df['Fat'] - needs['Fat']/3) +
            abs(df['Carbohydrates'] - needs['Carbohydrates']/3)
            
        )

        top_foods = df.sort_values(by='score').head(10)
        return render(request, 'recommender/results.html', {
            'foods': top_foods.to_dict(orient='records'),
            'needs': needs
        })

    return render(request, 'recommender/home.html')

# Create your views here.
