number = input("please enter a number")

sum = 0
for digit in (number):
    if digit.isdigit():
        sum += int(digit)

print(sum)