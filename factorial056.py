import math            
a=int(input())
b=[]
print("Factorial =",math.factorial(a))
for i in range(1,a+1):
    if a%i==0:
        b.append(i)
print("Number of factors :",len(b))
