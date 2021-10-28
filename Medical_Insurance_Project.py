#function to analyze for smoker status
def analyze_smoker(smoker_status):
  if (smoker_status == 1):
    print("If you stopped smoking, your Insurance Cost would be 24000 Dollars less.")
    return 24000
  else:
    print("Smoking is not an issue for you.")
    return 0
#function to analyze bmi and output on how much bmi to lose to land in healthy range
def analyze_bmi(bmi_value):
  if (bmi_value > 30):
    improvement = bmi_value - 24
    decrease_in_costs = round(improvement * 370, 1)
    print("Your BMI is in the obese range. In order to get to a healthy range, you need to lose at least " + str(round(improvement)) + " BMI-Points.")
    print("You would have to pay " + str(decrease_in_costs) + " dollars less.")
    return decrease_in_costs
  elif (bmi_value >= 25 and bmi_value <= 30):
    improvement = bmi_value - 24
    decrease_in_costs = round(improvement * 370, 1)
    print("Your BMI is in the overweight range. In order to get to a healthy range, you need to lose at least " + str(round(improvement)) + " BMI-Points.")
    print("You would have to pay " + str(decrease_in_costs) + " dollars less.")
    return decrease_in_costs
  elif (bmi_value >= 18.5 and bmi_value < 25):
    print("Your BMI is in a healthy range.")
    return 0
  else: 
    print("Your BMI is in the underweight range. Increasing your BMI will not help lower your cost, but it will help improve your health.")
    return 0

# Function to estimate insurance cost:
def estimate_insurance_cost(name, age, sex, bmi, num_of_children, smoker):  
  estimated_cost = 250*age - 128*sex + 370*bmi + 425*num_of_children + 24000*smoker - 12500
  print(name + "'s Estimated Insurance Cost: " + str(estimated_cost) + " dollars.")
  smoking_cost = analyze_smoker(smoker)
  bmi_cost = analyze_bmi(bmi)
  if (smoking_cost > 0 and bmi_cost > 0):
    print(name + "'s Estimated Insurance Cost while non-smoker and healthy bmi: " + str(estimated_cost - smoking_cost - bmi_cost) + " dollars.")
  elif(smoking_cost > 0 and bmi_cost == 0):
    print(name + "'s Estimated Insurance Cost while non-smoker: " + str(estimated_cost - smoking_cost) + " dollars.")
  elif(smoking_cost == 0 and bmi_cost > 0):
    print(name + "'s Estimated Insurance Cost while healthy bmi-range: " + str(estimated_cost - smoking_cost - bmi_cost) + " dollars.")
  else: 
    print("You are a healthy individual")

  return estimated_cost
 
# Estimate Keanu's insurance cost
keanu_insurance_cost = estimate_insurance_cost(name = 'Keanu', age = 25, sex = 1, bmi = 20, num_of_children = 0, smoker = 0)

# Estimate Maria's insurance cost
maria_insurance_cost = estimate_insurance_cost(name = 'Maria', age = 25, sex = 0, bmi = 20.0, num_of_children = 0, smoker = 0)
