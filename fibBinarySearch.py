def largestFIB(n, fib):
    left,right=0,len(fib)-1
    while left <= right:
        mid = (left + right) // 2
        if fib[mid] < n:
            result = fib[mid]
            left = mid + 1
        else:
            right = mid - 1
    return result

fib=[0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233] 
n=int(input("Enter a number between 0 t0 350:"))
ans=largestFIB(n,fib)
print("The largest Fibonacci number less than ",n," is ",ans)