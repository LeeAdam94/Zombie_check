infected = 100
high_risk_symptoms = ["bloodshot", "drooling", "crazed"]
temp = int(input("What is your temperature?: "))

if temp >= infected:
    symptoms = input("Do you have any symptoms?: ")
    symptoms_list = symptoms.split(",")
    if any(symptom in high_risk_symptoms for symptom in symptoms_list):
        print("Put em down boys!")
    else:
        print("Infected, we can't let you in here. I'm very sorry")
else:
    print("Welcome to the safe zone!")
