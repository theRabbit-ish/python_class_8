# Write a function pow(a,b). The function should return the value a raised to the power of b. (a^b)

def pow(a,b):

    return a**b


num_1 = int(input("Enter a number : "))
num_2 = int(input("Enter a second number : "))

result = pow(num_1, num_2)

print(f"The value of a^b is {result}")

