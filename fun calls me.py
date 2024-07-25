
def fibo(x,a,b,fib,count):
    if a<=x:
        fib.append(a)
        a,b=b,a+b
        count+=1
        return fibo(x,a,b,fib,count)
    return count,fib 
x=int(input("Enter a number: "))
a,b=1,1
fib=[]
count=0
print(fibo(x,a,b,fib,count))
