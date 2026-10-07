import pandas as pd

file_path = 'yeast/dataset/pdf1_yeast_biomass_cleaned.csv'

data = pd.read_csv(file_path)

X = data[['temperature_C', 'pH', 'sugar_g_L']]

y = data['observed_biomass_g_L']

print("Input Features (X):")
print(X)

print("\nTarget (y):")
print(y)

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("\nTraining data:")
print(X_train)

print("\nTesting data:")
print(X_test)

print("\nTraining target:")
print(y_train)

print("\nTesting target:")
print(y_test)

from sklearn.linear_model import LinearRegression

model = LinearRegression()

model.fit(X_train, y_train)

print("\nMachine Learning Model trained successfully.")
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

y_pred = model.predict(X_test)

mae = mean_absolute_error(y_test, y_pred)
rmse = mean_squared_error(y_test, y_pred) ** 0.5
r2 = r2_score(y_test, y_pred)

print("\nModel Evaluation:")
print("MAE:", mae)
print("RMSE:", rmse)
print("R2 Score:", r2)

import joblib

joblib.dump(model, 'yeast/dataset/yeast_biomass_model.pkl')

print("\nML model saved successfully.")