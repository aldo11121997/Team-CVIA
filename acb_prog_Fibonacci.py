def Fibonacci(n):
    serie=[1]*n 
    for i in range(2,n):
         serie[i]=serie[i-2]+serie[i-1]
    return serie
def Suma(s):
    sum = 0
    for i in s:
        sum = sum + i
    return sum
print("Ingrese el número:")
num = int(input())
#print(Fibonacci(num))
print(Suma(Fibonacci(num))) 
