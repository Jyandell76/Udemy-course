# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
#Write your code below this row 👇
f_ = 0
sum_ = int(0)
for s in student_heights:
    sum_ += student_heights[f_]
    f_ += 1
avg_ = round(sum_ / f_)
print(f"{avg_}")    







