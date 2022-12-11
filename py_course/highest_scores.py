# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
i = 0
highest_ = int(student_scores[i])
for high_ in student_scores:
    if highest_ >= int(student_scores[i]):
         i += 1
    else:
        highest_ = int(student_scores[i])
        i += 1           
print(f"{highest_}")        
    


# 78 65 89 86 55 91 64 89

