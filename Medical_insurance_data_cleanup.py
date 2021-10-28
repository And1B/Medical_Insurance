medical_data = \
"""Marina Allison   ,27   ,   31.1 , 
#7010.0   ;Markus Valdez   ,   30, 
22.4,   #4050.0 ;Connie Ballard ,43 
,   25.3 , #12060.0 ;Darnell Weber   
,   35   , 20.6   , #7500.0;
Sylvie Charles   ,22, 22.1 
,#3022.0   ;   Vinay Padilla,24,   
26.9 ,#4620.0 ;Meredith Santiago, 51   , 
29.3 ,#16330.0;   Andre Mccarty, 
19,22.7 , #2900.0 ; 
Lorena Hodson ,65, 33.1 , #19370.0; 
Isaac Vu ,34, 24.8,   #7045.0"""

#cleaning up the string here
updated_medical_data = medical_data.replace('#', '$')
num_records = 0

for record in updated_medical_data:
  if '$' in record:
    num_records += 1
medical_data_split = updated_medical_data.split(';')
medical_records = []

for record in medical_data_split:
  medical_records.append(record.split(','))
medical_records_clean = []

for record in medical_records:
  record_clean = []
  for item in record:
    record_clean.append(item.strip())
  medical_records_clean.append(record_clean)
#print(medical_records_clean)

#outputting names:
#for record in medical_records_clean:
  #print(record[0].upper())

names = []
ages = []
bmis = []
insurance_costs = []

for record in medical_records_clean:
  names.append(record[0])
  ages.append(record[1])
  bmis.append(record[2])
  insurance_costs.append(record[3])
print("Names: \n", names)
print("Ages: \n", ages)
print("BMI's: \n", bmis)
print("Insurance_Costs: \n", insurance_costs)

#Print sentences with information for all records
i = 0
while i < len(medical_records_clean):
  print(names[i], " is ", ages[i], " years old, with a BMI of ", bmis[i], " and an insurance cost of ", insurance_costs[i])
  i += 1

def average_bmi(bmis):
  total_bmi = 0
  for floats in bmis:
    total_bmi += float(floats)
  average_bmi = total_bmi / len(bmis)
  return average_bmi
print("Average BMI: ", average_bmi(bmis))

#remove $ from insurance_costs
tmp_insurance = []
for numbers in insurance_costs:
  tmp_insurance.append(numbers.replace('$', ''))
#print(tmp_insurance)
  
#calculate the average insurance_costs
def average_insurance(insurance_list):
  costs = 0
  for numbers in insurance_list:
    costs += float(numbers)
  average_costs = costs / len(insurance_list)
  return average_costs

print("Average Costs: ", average_insurance(tmp_insurance))

