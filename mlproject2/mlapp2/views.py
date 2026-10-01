import os
import joblib
from django.shortcuts import render, redirect
from django.conf import settings

BASE_DIR = settings.BASE_DIR
MODEL_PATH = os.path.join(BASE_DIR, 'mlmodel1.pkl')
SCALER_PATH = os.path.join(BASE_DIR, 'scalermodel1.pkl')


def home(request):
    return render(request, 'home.html')


def student_register(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'studentragister.html')


def signup(request):
    if request.method == 'POST':
        return redirect('login')
    return render(request, 'signup.html')


def login_view(request):
    if request.method == 'POST':
        return redirect('home')
    return render(request, 'login.html')


def predict(request):
    if request.method == 'POST':
        try:
            cgpa = float(request.POST.get('cgpa', 0))
            iq = int(request.POST.get('iq', 0))
            profile_score = int(request.POST.get('profile_score', 0))

            scaler = joblib.load(SCALER_PATH)
            model = joblib.load(MODEL_PATH)

            scaled_input = scaler.transform([[cgpa, iq, profile_score]])
            prediction = model.predict(scaled_input)[0]

            result_text = "Placed" if prediction == 1 else "Not Placed"

            context = {
                'cgpa': cgpa,
                'iq': iq,
                'profile_score': profile_score,
                'result': result_text,
                'prediction': prediction
            }
            return render(request, 'result.html', context)
        except Exception as e:
            return render(request, 'home.html', {'error': str(e)})

    return redirect('home')