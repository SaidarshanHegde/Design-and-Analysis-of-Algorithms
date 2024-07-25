def fibonacci(n):
    fib=[]
    a,b=1,1
    i=0
    while i<n:
        fib.append(a)
        a,b=b,a+b
        i+=1
    return fib
n=int(input("Enter the number of fib numbers to be printed:"))    
print(fibonacci(n))