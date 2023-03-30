#1.Write a Python function to find the Max of three numbers.

def max(n1,n2,n3):
    if n1 > n2 :
        if n1 > n3 :
            return n1
        else:
            return n3
    else:
        return n2

num1= int(input("Enter First number :"))
num2 = int(input("Enter Second number :"))
num3 = int(input("Enter Third number :"))

print("max of ",num1,", ",num2," and ",num3," is ",max(num1,num2,num3))

#2.Write a Python program to reverse a string(use functions).


def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str
 
s = input("Enter a string: ")
 
print("The original string is : ", s)
 
print("The reversed string is : ",reverse(s))


"""
3.Write a Python function that takes a number as a parameter and check
the number is prime or not. Note : A prime number (or a prime) is a natural
number greater than 1 and that has no positive divisors other than 1 and
itself.
"""


n = int(input("Enter a number: "))
flag = False

if n > 1:
    for i in range(2, n):
        if (n % i) == 0:
            flag = True
            break

if flag:
    print(n, " is not a prime number.")
else:
    print(n, " is a prime number.")
    
#4.Write a Python function to check whether a string is a palindrome or not

def reverse(s):
    str = ""
    for i in s:
        str = i + str
    return str

s = input("Enter a string: ")

if s == reverse(s):
    print(s," is palindrome.")
else:
    print(s," is not palindrome")

