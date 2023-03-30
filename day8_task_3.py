"""
3.Write menu driven program to do addition, subtraction, multiplication,division and modulus operations of 2 numbers inputted by user. 

The program should do operations depending upon the user choice (hint: use if elif else statement).
"""
num1 = int(input("Enter First Number: "))
num2 = int(input("Enter Second Number: "))

print("Enter which operation would you like to perform?")
ch = input("Enter any of these char for specific operation +,-,*,/, %: ")

result = 0
if ch == '+':
    result = num1 + num2
elif ch == '-':
    result = num1 - num2
elif ch == '*':
    result = num1 * num2
elif ch == '/':
    result = num1 / num2
elif ch == '%':
    result = num1 % num2
else:
    print("Invalid Input!")

print(num1, ch , num2, " : ", result)