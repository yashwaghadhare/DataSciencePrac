# Install scikit-fuzzy library
!pip install scikit-fuzzy

import numpy as np
import skfuzzy as fuzz
from skfuzzy import control as ctrl

# Define the input variable "temperature" from 0 to 100°C
temperature = ctrl.Antecedent(np.arange(0, 101, 1), 'temperature')

# Define the output variable "heater" from 0% to 100%
heater = ctrl.Consequent(np.arange(0, 101, 1), 'heater')

# Define fuzzy membership functions for temperature
temperature['cold'] = fuzz.trimf(temperature.universe, [0, 0, 50])   # Cold range
temperature['warm'] = fuzz.trimf(temperature.universe, [30, 50, 80]) # Warm range
temperature['hot']  = fuzz.trimf(temperature.universe, [60, 100, 100]) # Hot range

# Define membership functions for heater output
heater['low']    = fuzz.trimf(heater.universe, [0, 0, 50])    # Low heater power
heater['medium'] = fuzz.trimf(heater.universe, [25, 50, 75])  # Medium power
heater['high']   = fuzz.trimf(heater.universe, [50, 100, 100]) # High power

# Create fuzzy rules
rule1 = ctrl.Rule(temperature['cold'], heater['high'])   # If cold → high heat
rule2 = ctrl.Rule(temperature['warm'], heater['medium']) # If warm → medium heat
rule3 = ctrl.Rule(temperature['hot'],  heater['low'])    # If hot → low heat

# Build fuzzy control system
heater_ctrl = ctrl.ControlSystem([rule1, rule2, rule3])

# Create simulation object
heating = ctrl.ControlSystemSimulation(heater_ctrl)

# Provide an input temperature
input = heating.input['temperature'] = 80

# Process the fuzzy logic system
heating.compute()

# Print results
print("Temperature Input (°C) =", input)
print("Heater Output Power (%) =", heating.output['heater'])
