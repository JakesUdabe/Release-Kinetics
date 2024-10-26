# -*- coding: cp1252 -*-
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress

# Load the data
file_path = r'C:\Users\xxx\xxx\data.xlsx'  # Change this to your file path
data = pd.read_excel(file_path)

# Assuming time is in the first column and concentration is in the second
time = data.iloc[:, 0].values
concentration = data.iloc[:, 1].values

# Check concentration data for NaN or Inf values
print("Concentration NaNs:", np.isnan(concentration).any())
print("Concentration Infs:", np.isinf(concentration).any())

# Define the linearized forms of the kinetic models
def zero_order_linear(t, C0, k0):
    """ Zero-order kinetic model: C = C0 - k0 * t """
    return C0 - k0 * t

def first_order_linear(t, lnC0, k1):
    """ First-order kinetic model: ln(C) = ln(C0) - k1 * t """
    return lnC0 - k1 * t

def hixson_crowell_linear(t, C0, k):
    """ Hixson-Crowell kinetic model: C^(1/3) = C0^(1/3) - k * t """
    return C0**(1/3) - k * t

def baker_lonsdale_linear(t, C0, k):
    """ Baker-Lonsdale kinetic model: sqrt(C) = sqrt(C0) - k * sqrt(t) """
    return C0**(0.5) - k * np.sqrt(t)

def higuchi_linear(t, C0, k):
    """ Higuchi kinetic model: C = C0 - k * sqrt(t) """
    return C0 - k * np.sqrt(t)

# Perform linear regression and calculate R² for each model
def calculate_r_squared(x, y, model_name):
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    print(f'{model_name} Linear Fit -> Slope: {slope}, Intercept: {intercept}, R²: {r_value**2:.4f}')
    return r_value**2, slope, intercept

# Zero-order model (linear form: concentration = C0 - k0 * t)
r_squared_zero, slope_zero, intercept_zero = calculate_r_squared(time, concentration, 'Zero-order')

# First-order model (linear form: ln(concentration) = ln(C0) - k1 * t)
ln_concentration = np.log(concentration)
r_squared_first, slope_first, intercept_first = calculate_r_squared(time, ln_concentration, 'First-order')

# Hixson-Crowell model (linear form: C^(1/3) = C0^(1/3) - k * t)
cube_root_concentration = concentration**(1/3)
r_squared_hixson, slope_hixson, intercept_hixson = calculate_r_squared(time, cube_root_concentration, 'Hixson-Crowell')

# Baker-Lonsdale model (linear form: sqrt(concentration) = sqrt(C0) - k * sqrt(t))
sqrt_concentration = concentration**0.5
sqrt_time = np.sqrt(time)
r_squared_baker, slope_baker, intercept_baker = calculate_r_squared(sqrt_time, sqrt_concentration, 'Baker-Lonsdale')

# Higuchi model (linear form: concentration = C0 - k * sqrt(t))
r_squared_higuchi, slope_higuchi, intercept_higuchi = calculate_r_squared(sqrt_time, concentration, 'Higuchi')

# Store R² values
r_squared_values = {
    'Zero Order': r_squared_zero,
    'First Order': r_squared_first,
    'Hixson Crowell': r_squared_hixson,
    'Baker Lonsdale': r_squared_baker,
    'Higuchi': r_squared_higuchi
}

# Find the model with the highest R² value
best_model = max(r_squared_values, key=r_squared_values.get)
print(f"\nThe model with the highest R² value is: {best_model} with R² = {r_squared_values[best_model]:.4f}")

# Plot all fits
t_fit = np.linspace(0, max(time), 100)

plt.figure(figsize=(12, 8))
plt.scatter(time, concentration, label='Data', color='black', s=10)

# Plot Zero-order
plt.plot(t_fit, zero_order_linear(t_fit, intercept_zero, slope_zero), label='Zero Order', linestyle='--')

# Plot First-order
plt.plot(t_fit, np.exp(first_order_linear(t_fit, intercept_first, slope_first)), label='First Order', linestyle='--')

# Plot Hixson Crowell
plt.plot(t_fit, hixson_crowell_linear(t_fit, intercept_hixson, slope_hixson)**3, label='Hixson Crowell', linestyle='--')

# Plot Baker Lonsdale
plt.plot(t_fit, baker_lonsdale_linear(np.sqrt(t_fit), intercept_baker, slope_baker)**2, label='Baker Lonsdale', linestyle='--')

# Plot Higuchi
plt.plot(t_fit, higuchi_linear(np.sqrt(t_fit), intercept_higuchi, slope_higuchi), label='Higuchi', linestyle='--')

plt.xlabel('Time')
plt.ylabel('Concentration')
plt.title('Kinetic Models Fitting')
plt.legend()
plt.show()

# Wait for user input before closing
input("Press Enter to exit...")
