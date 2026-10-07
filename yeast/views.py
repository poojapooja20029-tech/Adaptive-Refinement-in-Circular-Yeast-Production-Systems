from django.shortcuts import render, redirect
import joblib
import pandas as pd
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from .models import ProductionData


def home(request):
    return render(request, 'yeast/home.html')


@login_required
def dashboard(request):
    return render(request, 'yeast/dashboard.html')


def production_data(request):

    if request.method == 'POST':

        batch_id = request.POST.get('batch_id')
        temperature = request.POST.get('temperature')
        ph = request.POST.get('ph')
        nutrient_level = request.POST.get('nutrient_level')
        fermentation_time = request.POST.get('fermentation_time')
        initial_yeast_amount = request.POST.get('initial_yeast_amount')
        final_yield = request.POST.get('final_yield')

        ProductionData.objects.create(
            batch_id=batch_id,
            temperature=temperature,
            ph=ph,
            nutrient_level=nutrient_level,
            fermentation_time=fermentation_time,
            initial_yeast_amount=initial_yeast_amount,
            final_yield=final_yield
        )

        return redirect('production_data')

    data = ProductionData.objects.all().order_by('-id')

    return render(
        request,
        'yeast/production_data.html',
        {'data': data}
    )


def edit_production_data(request, id):

    data = ProductionData.objects.get(id=id)

    if request.method == 'POST':

        data.batch_id = request.POST.get('batch_id')
        data.temperature = request.POST.get('temperature')
        data.ph = request.POST.get('ph')
        data.nutrient_level = request.POST.get('nutrient_level')
        data.fermentation_time = request.POST.get('fermentation_time')
        data.initial_yeast_amount = request.POST.get('initial_yeast_amount')
        data.final_yield = request.POST.get('final_yield')

        data.save()

        return redirect('production_data')

    return render(
        request,
        'yeast/edit_production_data.html',
        {'data': data}
    )


def delete_production_data(request, id):

    data = ProductionData.objects.get(id=id)

    data.delete()

    return redirect('production_data')


def user_login(request):

    if request.method == 'POST':

        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(
            request,
            username=username,
            password=password
        )

        if user is not None:
            login(request, user)
            return redirect('dashboard')

        else:
            return render(
                request,
                'yeast/login.html',
                {'error': 'Invalid username or password'}
            )

    return render(request, 'yeast/login.html')


def predict_biomass(request):

    prediction = None

    if request.method == 'POST':

        temperature = float(request.POST.get('temperature'))
        ph = float(request.POST.get('ph'))
        sugar = float(request.POST.get('sugar'))

        model = joblib.load(
            'yeast/dataset/yeast_biomass_model.pkl'
        )

        prediction = model.predict(
            pd.DataFrame(
                [[temperature, ph, sugar]],
                columns=['temperature_C', 'pH', 'sugar_g_L']
            )
        )[0]

        prediction = round(prediction, 2)

    return render(
        request,
        'yeast/prediction.html',
        {'prediction': prediction}
    )


def process_optimization(request):

    model = joblib.load(
        'yeast/dataset/yeast_biomass_model.pkl'
    )

    temperatures = [29, 31, 33, 35, 37]
    ph_values = [4.5, 5.0, 5.5, 6.0, 6.5]
    sugar_values = [80, 100, 107.5, 120, 140]

    best_prediction = None
    best_conditions = None

    for temperature in temperatures:

        for ph in ph_values:

            for sugar in sugar_values:

                prediction = model.predict(
                    pd.DataFrame(
                        [[temperature, ph, sugar]],
                        columns=['temperature_C', 'pH', 'sugar_g_L']
                    )
                )[0]

                if best_prediction is None or prediction > best_prediction:

                    best_prediction = prediction

                    best_conditions = {
                        'temperature': temperature,
                        'ph': ph,
                        'sugar': sugar
                    }

    return render(
        request,
        'yeast/optimization.html',
        {
            'best_conditions': best_conditions,
            'best_prediction': round(best_prediction, 2)
        }
    )
def adaptive_refinement(request):

    current_prediction = None
    refined_prediction = None
    suggestion = None

    best_temperature = 29
    best_ph = 4.5
    best_sugar = 80

    if request.method == 'POST':

        temperature = float(request.POST.get('temperature'))
        ph = float(request.POST.get('ph'))
        sugar = float(request.POST.get('sugar'))

        model = joblib.load(
            'yeast/dataset/yeast_biomass_model.pkl'
        )

        current_prediction = model.predict(
            pd.DataFrame(
                [[temperature, ph, sugar]],
                columns=['temperature_C', 'pH', 'sugar_g_L']
            )
        )[0]

        current_prediction = round(current_prediction, 2)

        refined_prediction = model.predict(
            pd.DataFrame(
                [[best_temperature, best_ph, best_sugar]],
                columns=['temperature_C', 'pH', 'sugar_g_L']
            )
        )[0]

        refined_prediction = round(refined_prediction, 2)

        if refined_prediction > current_prediction:
            suggestion = "The refined conditions may improve the predicted biomass."
        else:
            suggestion = "The current conditions are already performing well."

    return render(
        request,
        'yeast/adaptive_refinement.html',
        {
            'current_prediction': current_prediction,
            'best_temperature': best_temperature,
            'best_ph': best_ph,
            'best_sugar': best_sugar,
            'refined_prediction': refined_prediction,
            'suggestion': suggestion
        }
    )