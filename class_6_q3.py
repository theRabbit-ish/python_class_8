# Write a function to test if a number entered by the user is Armstrong or not.

def check_armstrong(n):
    temp = n
    result = 0
    while temp != 0:
        rem = temp % 10
        result = result + rem ** 3
        temp = temp // 10
    return result


num = int(input("Enter a number : "))
sum = check_armstrong(num)
if num == sum:
    print(f"{num} is a armstrong number")
else:
    print(f"{num} isn't a armstrong number")
