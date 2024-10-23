number = int(input("please enter a number "))
if number > 1:
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            print("it is not a prime number.")
            break
    else:
        print("it is a prime number.")