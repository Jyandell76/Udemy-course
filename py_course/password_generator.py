#Password Generator Project
# build a list then randomly sort and print it?.
#             steps
# 1 build list populated with x random letters. 
# 2 append x random numbers 
# 3 append x random symbals
# 4 for loop random cell from list then remove it until null

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
len_ = int(len(letters))
pos_ = random.randint(0, (len_ - 1))
alpha_rand =  letters[pos_]
a_list = []
for i in range(0, int(nr_letters)):
  pos_ = random.randint(0, (len_ - 1))
  alpha_rand = letters[pos_]
  a_list.append(f"{alpha_rand}")
  
nr_symbols = int(input(f"How many symbols would you like?\n"))
len_s = int(len(symbols))
pos_s = random.randint(0, (len_s - 1))
sym_rand = numbers[pos_s]
for i in range(0, int(nr_symbols)):
  pos_s = random.randint(0, (len_s - 1))
  sym_rand = symbols[pos_s]
  a_list.append(f"{sym_rand}")  
nr_numbers = int(input(f"How many numbers would you like?\n"))
len_n = int(len(numbers))
pos_n = random.randint(0, (len_n - 1))
num_rand = numbers[pos_n]
for i in range(0, int(nr_numbers)):
  pos_n = random.randint(0, (len_n - 1))
  num_rand = numbers[pos_n]
  a_list.append(f"{num_rand}")
nr_f = int(len(a_list))
pos_f = random.randint(0, (nr_f -1))
f_rand = a_list[pos_f]
answer = ""
for i in range(0, nr_f):
  pos_f = random.randint(0, (nr_f -1))
  f_rand = a_list[pos_f]
  answer = answer + answer.join(f_rand)
  a_list.remove(f"{f_rand}")
  nr_f -= 1
print(f"Your password is: {answer}")



  
  












#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P