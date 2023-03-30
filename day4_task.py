# 1. Write the code to input two integer values from the user and perform addition,subtraction,division and multiplication.

a = input("Input first number: ")
b = input("Input second number: ")
sum = float(a) + float(b)
sub = float(a) - float(b)
div = float(a) / float(b)
mul = float(a) * float(b)

#Display the addition, subtraction, division and multiplication

print('The sum of {0} and {1} is {2}'.format(a, b, sum))
print('The difference of {0} and {1} is {2}'.format(a, b, sub))
print('The division of {0} and {1} is {2}'.format(a, b, div))
print('The multiplication of {0} and {1} is {2}'.format(a, b, mul))

#2.Create a list having length 3 and it should contain cricket,badminton, hockey as its elements and print the list. 

list_1 =["cricket","badminton","hockey"]
print(list_1)

#3. Delete the element badminton from the list and print the list.

list_1.remove("badminton")
print(list_1)

#4.Add new element football to the list and print the list.

list_1.append("football")
print(list_1)