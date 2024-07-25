def gcd(m,n):
    if n==0:
        return m
    elif m==0:
        return n
    else:
        return gcd(abs(m-n),min(m,n))

def get(n):
    a=0
    b=0
    sum=1
    for i in range(0,n):
        a=b
        b=sum
        sum=a+b
    return sum        

m=int(input("Enter 1st index :"))
n=int(input("Enter 2nd index :"))
res1=gcd(get(m),get(n))
x=gcd(m,n)
res2=get(x)
if res1==res2:
    print("Verified")
else:
    print("Not verified")