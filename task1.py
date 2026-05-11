patient_id = int(input("Enter Patient ID: "))
patient_name = input("Enter Patient Name: ")
age = int(input("Enter Age: "))
gender = input("Enter Gender: ") 
disease_name = input("Enter Disease Name: ")
doctor_name = input("Enter Doctor Name: ")
room_type = input("Enter Room Type: ")
number_of_days_admitted = int(input("Enter Number of Days: "))
daily_room_charge = int(input("Enter Daily Room Charge: "))
admission_status = input("Enter Admission Status: ")
category = ""

print("--Patient Details--")
print("Patinet ID:", patient_id)
print("Patient Name", patient_name)
print("Age:",age)
print("Gender:", gender)
print("Disease Name:",disease_name)
print("Doctor Name:",doctor_name)
print("Room Type:",room_type)
print("Admission Status:",admission_status)
    
print("\n----Dataype----")
print("Patient ID", type(patient_id))
print("Age:",type(age))
print("Daily Room Charges", type(daily_room_charge))
print("Admission Status", type(admission_status))

age_float = float(age)
patient_id_str = float(patient_id)
print("Age type:",type(age_float))
print("Patient Id type:",type(patient_id_str))
#print

email = patient_name.lower()+"@hospital.com"
print("\nGenerated Email:",email)

total_bill = number_of_days_admitted*daily_room_charge

if(age<12):
    category = "Child Patient"    
elif(age<=60):
    category = "Adult Patinet"
else:
    category = "Senior Citizen Patient"

print("Category:",category)

if total_bill > 50000:
    total_bill=total_bill*(0.8)
    print("Total Bill:",total_bill)
elif total_bill > 30000:
    total_bill=total_bill*(0.9)
    print("Total Bill:",total_bill)
else :
    print("No discount")

if admission_status == "Discharged":
    print("Generate Final Bill")
else:
    print("Patient Currently Admitted")


