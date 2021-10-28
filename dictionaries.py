# Add your code here
medical_costs = {}
medical_costs.update({"Marina": 6607.0, "Vinay": 3225.0})
medical_costs.update({"Connie": 8886.0, "Isaac": 16444.0, "Valentina": 6420.0})
#print(medical_costs)
medical_costs["Vinay"] = 3325.0
#print(medical_costs)
total_costs = 0
for values in medical_costs.values():
  total_costs += values
average_costs = total_costs / len(medical_costs)
#print("Average Insurance Cost: "+ str(average_costs)) 

names = ["Marina", "Vinay", "Connie", "Isaac"]
ages = [27,24,43,35]
zipped_ages = zip(names, ages)
names_to_ages = {keys:values for keys, values in zipped_ages}
#print(names_to_ages)
marina_age = names_to_ages.get("Marina", None)
#print("Marina's age is", marina_age)

medical_records = {}
medical_records["Marina"] = {"Age": 27, "Sex": "Female", "BMI": 31.1, "Children": 2, "Smoker": "Non-smoker", "Insurance_cost": 6607.0}
medical_records["Vinay"] = {"Age": 24, "Sex": "Male", "BMI": 26.9, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 3225.0}
medical_records["Connie"] = {"Age": 43, "Sex": "Female", "BMI": 23.3, "Children": 3, "Smoker": "Non-smoker", "Insurance_cost": 8886.0}
medical_records["Isaac"] = {"Age": 35, "Sex": "Male", "BMI": 20.6, "Children": 4, "Smoker": "Smoker", "Insurance_cost": 16444.0}
medical_records["Valentina"] = {"Age": 52, "Sex": "Female", "BMI": 18.7, "Children": 1, "Smoker": "Non-smoker", "Insurance_cost": 6420.0}
#print(medical_records)
#print("Connie's insurance cost is ", str(medical_records["Connie"]["Insurance_cost"]), "dollars.")
#print(medical_records)
medical_records.pop("Vinay")
#for name, values in medical_records.items():
  #print(str(name) +" is a "+ str(values.get("Age"))+" year old "+ str(values.get("Sex")) +" "+ str(values.get("Smoker"))+ " with a BMI of "+ str(values.get("BMI"))+ " and insurance cost of "+ str(values.get("Insurance_cost")))

def update_medical_records(name, data):
  new_medical_record = {}
  new_medical_record[name] = data
  medical_records.update(new_medical_record)
  print(medical_records)
update_medical_records("Meli", {"Age": 24, "Sex": "Female", "BMI": 20.0, "Children": 0, "Smoker": "Non-smoker", "Insurance_cost": 1500.0})
