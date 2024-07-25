def divide(a, b):
    quotient = 0
    remainder = a

    while remainder >= b:
        remainder -= b
        quotient += 1

    return quotient, remainder

a = int(input("Enter the value of a: "))
b = int(input("Enter the value of b: "))

quotient, remainder = divide(a, b)
print("The quotient is:",quotient)
print("The remainder is:", remainder)