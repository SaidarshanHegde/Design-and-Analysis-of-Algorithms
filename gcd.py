def gcd(m,n):
    if n==0:
        return m
    elif m==0:
        return n
    else:
        return gcd(abs(m-n),min(m,n))
m=int(input("m="))
n=int(input("n="))    
result=gcd(m,n)
print(result)