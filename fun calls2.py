count=0
f=[]
def fibonacci(n):
    global count
    global f
    count+=1
    if n<=1:
        return 1
    else:
        fibonacci(n-1)+fibonacci(n-2)
    return count
n=int(input("Enter a number :"))
fibonacci(n)
print('The count is: ',count)
