def right(a,x):
        l,r=0,len(a)-1
        result=-1
        while l<=r:
                mid=(l+r)//2
                if a[mid]==x:
                        result=mid
                        l=mid+1
                elif a[mid]>x:
                        r=mid-1
                else:
                        l=mid+1
        return result
n=input("Enter list elements separeted by space:")
a=[int(i) for i in  n.split()] 
print(a) 
x=int(input("enter a required element:")) 
k=right(a,x)
print(f"{x}'s right most occurance is {k}")

