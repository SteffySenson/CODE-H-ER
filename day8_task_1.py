#1.Write a program to print the series 10,20,30,40,50,60,70,80,90,100 using while loop.
factors = []
num = 1
while num <= 100: 
  num+=1 
  if num % 10 == 0: 
    factors.append(num)
print(factors)