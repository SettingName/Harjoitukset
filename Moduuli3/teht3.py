gender = (input("Enter biological gender (male/female): ")).lower()
hemoglob = float(input("Enter hemoglobin value (g/l): "))
if gender == "male" and hemoglob < 134 or gender == "female" and hemoglob < 117:
    print("Your hemoglobin is low.")
elif gender == "male" and hemoglob > 167 or gender == "female" and hemoglob > 155:
    print("Your hemoglobin is high.")
elif gender != "male" and gender != "female":
        print("Invalid gender.")
else:
    print("Your hemoglobin is normal.")