#Problem 1
sec= int(input("enter seconds"))
h = (sec//3600)
m = (sec -(3600*h))//60
s = (sec-(3600*h)-(m*60))
print(h, m, s)

#Problem 2
p=int(input("Please enter deposit amount"))
F=int(input("Please enter future amount desired"))
r=float(input("please enter annual interest rate"))
n=int(input("please enter number of years"))
print(F/(1+r)**n)
