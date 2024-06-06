from django.shortcuts import render, redirect
import pandas as pd
import pickle
from .forms import FraudPredictionForm
from .models import Prediction


def load_model():
    with open('fraud_detection_model.pkl', 'rb') as file:
        model = pickle.load(file)
    return model


def welcome(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        return redirect('predict_fraud', first_name=first_name, last_name=last_name)
    return render(request, 'welcome.html')




def predict_fraud(request, first_name, last_name):
    if request.method == 'POST':
        form = FraudPredictionForm(request.POST)
        if form.is_valid():
            input_data = {
                'job': [form.cleaned_data['job']],
                'marital': [form.cleaned_data['marital']],
                'education': [form.cleaned_data['education']],
                'default': [form.cleaned_data['default']],
                'housing': [form.cleaned_data['housing']],
                'loan': [form.cleaned_data['loan']],
                'contact': [form.cleaned_data['contact']],
                'month': [form.cleaned_data['month']],
                'day_of_week': [form.cleaned_data['day_of_week']],
                'duration': [form.cleaned_data['duration']],
                'campaign': [form.cleaned_data['campaign']],
                'pdays': [form.cleaned_data['pdays']],
                'previous': [form.cleaned_data['previous']],
                'poutcome': [form.cleaned_data['poutcome']],
                'amount': [form.cleaned_data['amount']]
            }

            input_df = pd.DataFrame(input_data)
            input_df = pd.get_dummies(input_df)

            # Ensure the input_df has all the same columns as the training set
            model = load_model()
            model_columns = model.feature_names_in_
            for col in model_columns:
                if col not in input_df:
                    input_df[col] = 0

            input_df = input_df[model_columns]  # Ensure the columns are in the same order
            prediction = model.predict(input_df)
            prediction_result = "Muvaffaqiyatli emas"   if prediction[0] == 1 else "Muvaffiqiyatli"

            # Save the prediction to the database (if needed)
            Prediction.objects.create(prediction=prediction_result)

            context = {
                'first_name': first_name,
                'last_name': last_name,
                'prediction': prediction_result
            }

            return render(request, 'result.html', context)
    else:
        form = FraudPredictionForm()

    return render(request, 'prediction.html', {'first_name': first_name, 'last_name': last_name, 'form': form})
