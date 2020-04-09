# Input for user name and a printed response.
name = input("Please enter your name: ")
print("Hi there", name)

# Input for user number converted into an Integer.
number = int(input("Please enter a number: "))

# Variables defined by whether the user's previous number input is divisible by 3 or 5.
is_fizz = number % 3 == 0
is_buzz = number % 5 == 0

# Print confirming what number the user selected.
print(name, "selected number", number)

# If user number is divisible by both 3 and 5, then print string.
if(is_fizz and is_buzz):
    print(number, "is a FizzBuzz number.")

# If user number is divisible by 3, then print string.
elif(is_fizz):
    print(number, "is a Fizz number.")

# If user number is divisible by 5, then print string.
elif(is_buzz):
    print(number, "is a Buzz number.")

# If user number is divisible by neither 3 nor 5, then print string.
else:
    print(number, "is neither a fizzy or a buzzy number.")