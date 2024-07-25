def get(L,n):
 l,r=0,len(L)-1
 while l<=r:
    m=(l+r)//2
    if n>L[m]:
        l=m+1
    elif n<L[m]:
        r=m-1
    else:
        return m
 return r     

def fibonacci(x):
   f=[]
   a,b=1,1
   while a<=x:
      f.append(a)
      a,b=b,a+b
   return f

n=int(input("Enter a number : "))
L=fibonacci(n)
print(L)
while n>0:
  k=get(L,n)
  n-=L[k]
  print(k,",",L[k])