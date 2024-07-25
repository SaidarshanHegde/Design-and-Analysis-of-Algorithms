def staircase(n):
    fib=[]
    a,b=1,1
    i=0
    while i<n+1:
        fib.append(a)
        a,b=b,a+b
        i+=1
    return fib
n=int(input("Enter the number of staircases:"))    
s=staircase(n)
print("Number of ways the staircases can be climbed is : ",s[-1])