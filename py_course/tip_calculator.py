#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇1
total_ = input("How much was the  bill? ")
total_int = float(total_)
tip_ = input("What percentage would you like to tip? 10, 12, or 15? ")
tip_int = float(tip_)
tip_calc = tip_int / 100
tip_calc += 1 
people_ = input("How many Party Members to split the check? ")
people_int = int(people_)
math_ = (total_int / people_int) * tip_calc  
print(f"Each party member should pay: ${math_:.2f}")