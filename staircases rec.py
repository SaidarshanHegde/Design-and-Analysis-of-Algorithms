def stair(n):
    if n<=1:
        return 1
    else:
        return stair(n-1)+stair(n-2)
n=int(input("Enter a number of staircases :"))
s=[]
for i in range(n+1):
    s.append(stair(i))
print(s)
print("Number of ways the staircases can be climbed is : ",s[-1])    
