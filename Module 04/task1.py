user_input = int(input("Enter a number: "))
def fact(n):
    if(n==1 or n==0): #base condition
        return 1
    else:
        return n * fact(n-1)
factorial = fact(user_input)
print(f"Factorial of {user_input} is: {factorial}")

