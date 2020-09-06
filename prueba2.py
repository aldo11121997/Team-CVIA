def Fibonacci(n): 
    if n<0: 
        print("Incorrect input") 
    elif n==1: 
        return 0
    elif n==2: 
        return 1
    else: 
        return Fibonacci(n-1)+Fibonacci(n-2) 
def serie(n):
    f=[]
    for i in range (2,n):
        f.append(Fibonacci(i))
    return f
def Suma(s):
    sum = 0
    for i in s:
        sum = sum + i
    return sum
print("Ingrese el número:")
num = int(input())
print(Fibonacci(num+1))
print(Suma(serie(num+1))) 