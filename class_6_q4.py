# Write a function to check if a number is reverse of the number i.e palindrome

def check_palindrome(a):
    temp = a
    result = 0
    while temp != 0:
        digit = temp % 10
        result = result * 10 + digit
        temp //= 10
    if num == result:
        print(f"{num} is a palindrome")
    else:
        print(f"{num} isn't a palindrome")


num = int(input("Enter a number : "))
check_palindrome(num)

