#2.Write a program to calculate the sum of all numbers from 1 to a given number n using for loop.

number = int(input("Enter the Number: "))
sum = 0
for value in range(1, number + 1):
    sum = sum + value
print(sum)