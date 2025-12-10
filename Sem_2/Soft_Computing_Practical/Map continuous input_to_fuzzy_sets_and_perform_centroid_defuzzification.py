!pip install scikit-fuzzy
import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

x_temp = np.arange(0, 101, 1) # Create a temperature range from 0 to 100°C with step of 1
cold = fuzz.trimf(x_temp, [0, 0, 50]) # Cold peaks at 0 and decreases to 50
warm = fuzz.trimf(x_temp, [30, 50, 80]) # Warm is centered around 50
hot  = fuzz.trimf(x_temp, [60, 100, 100]) # Hot rises from 60 and peaks at 100
temp_input = 80 # Choose a specific temperature input for analysis

# Fuzzification: calculate degree of membership for the input temperature in each fuzzy set
mu_cold = fuzz.interp_membership(x_temp, cold, temp_input) # Membership in 'cold'
mu_warm = fuzz.interp_membership(x_temp, warm, temp_input) # Membership in 'warm'
mu_hot  = fuzz.interp_membership(x_temp, hot,  temp_input) # Membership in 'hot'

# Print fuzzy membership values for understanding how 80°C fits in cold/warm/hot sets
print("Temperature Input =", temp_input)
print("Cold =", mu_cold)
print("Warm =", mu_warm)
print("Hot  =", mu_hot)

# Create output variable range (0–100) and define fuzzy sets for Low, Medium, High output
x_output = np.arange(0, 101, 1)
low    = fuzz.trimf(x_output, [0, 0, 50]) # Low output
medium = fuzz.trimf(x_output, [25, 50, 75]) # Medium output
high   = fuzz.trimf(x_output, [50, 100, 100]) # High output

# Rule-based output combination: (If warm → medium, if cold → high, if hot → low)
fuzzy_output = np.fmax(mu_warm * medium, # Warm contributes to Medium output
               np.fmax(mu_cold * high, # Cold contributes to High output
                       mu_hot * low)) # Hot contributes to Low output

# Defuzzification using centroid method to convert fuzzy result → crisp output
crisp = fuzz.defuzz(x_output, fuzzy_output, 'centroid')
print("Centroid Defuzzified Output =", crisp)
