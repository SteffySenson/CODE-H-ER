"""
#1. Wrtite a Python program to print the Fibonacci series of limit 10.

def recur_fibo(n):
   if n <= 1:
       return n
   else:
       return(recur_fibo(n-1) + recur_fibo(n-2))
limit = 10
print("Fibonacci sequence:")
for i in range(limit):
    print(recur_fibo(i))

"""
#2. Write a menu driven program to perform addition subtraction, multiplication and division of two numbers given by user.

def add(n1, n2):
    return n1+n2
 
def sub(n1, n2): 
    return n1 - n2
 
def mul(n1, n2):  
    return n1 * n2
 
def div(n1, n2):
    return n1 / n2

num1= int(input("Enter First number :"))
num2 = int(input("Enter Second number :"))

print("Addition")
print(num1,"+" ,num2,"=", add(num1,num2))
print("Substraction")
print(num1,"-" ,num2,"=", sub(num1, num2))
print("Multiplication")
print(num1,"*" ,num2,"=",mul(num1, num2))
print("Division")
print(num1,"/", num2,"=",div(num1, num2))
