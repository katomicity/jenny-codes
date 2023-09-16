#CALUCULATING BMI Weight/height**2
weight= float(input("Enter your weight in kgs: "))
height= float(input("Enter your weight in meters: "))
BMI= float(weight)/float(height**2)
BMI= round(BMI,2)
if BMI <=16.0 :
    print(f"Your BMI is {BMI} , You are Underweight and severely Thin ")
elif BMI <17.0 :
    print(f"Your BMI is {BMI} , You are Underweight and Moderately Thin ")
elif BMI <18.5 :
    print(f"Your BMI is {BMI} , You are Underweight and Mildly Thin ")
elif BMI <25.0 :
    print(f"Your BMI is {BMI} , You are Normal and keep it  up ")
elif BMI <30.0 :
    print(f"Your BMI is {BMI} , You are OverWeight ie: Pre-obese ")
elif BMI <35.0 :
    print(f"Your BMI is {BMI} , You are Midly Obese Class I ")
elif BMI <40.0 :
    print(f"Your BMI is {BMI} , You are Moderately Obese class II ")
elif BMI >=40.0 :
    print(f"Your BMI is {BMI} , You are Severely Obese class III ie severely ")

