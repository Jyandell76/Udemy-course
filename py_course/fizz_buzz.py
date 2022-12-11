for x in range(1, 101):
    if (x % 3) == 0:
        print("fizz")
    elif (x % 5) == 0:
        print("buzz")
    elif (x % 15) == 0:
        print("FizzBuzz")
    else:
        print(x)