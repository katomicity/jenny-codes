#CALUCULATING BMI Weight/height**2
weight= float(input("Enter your weight in kgs: "))
height= float(input("Enter your weight in meters: "))
BMI= float(weight)/float(height**2)
BMI= round(BMI,2)
print("Your BMI is " + str(BMI) + "kg/m^2" + " \n Given: " + str(weight) +"kgs as weight" + "\n and: " + str(height) + "m as height")