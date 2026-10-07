import joblib
import pandas as pd

# Load trained ML model
model = joblib.load(
    'yeast/dataset/yeast_biomass_model.pkl'
)

# Test different process conditions
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

print("Best Conditions:")
print(best_conditions)

print("Predicted Biomass:", round(best_prediction, 2), "g/L")