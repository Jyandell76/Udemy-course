# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

m_ = weight / (height * height)
if m_ > 35:
    print(f"Your BMI is {round(m_)} you are clinically obese.")
elif 35 > m_ > 30:
    print(f"Your BMI is {round(m_)}, you are obese.")
elif 30 > m_ > 25:
    print(f"Your BMI is {round(m_)}, you are slightly overweight.")
elif 25 > m_ > 18.5:
    print(f"Your BMI is {round(m_)}, you have a normal weight.")
else:
    print(f"Your BMI is {round(m_)}, you are underweight.")
