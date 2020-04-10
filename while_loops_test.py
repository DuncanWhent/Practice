import sys

name = input("What's your name? ")
response = input("Hello {}, do you understand while loops? \n(Please enter 'YES' or 'NO')  ".format(name))
response_count = 1

while response.upper() != "YES":
    if response_count >= 5:
        sys.exit("That's okay, you can try searching online for a more in-depth explanation if you still do not understand!")
    else:
        print("Don't worry {}, 'while loops' are a function that repeats itself until a certain predefined boolean condition is met. \nIn this case, you will recieve this message until you reply YES, any other input will continue the loop.".format(name))
        response = input("Do you understand 'while loops' better now {}? \n(Please enter 'YES' or 'NO')  ".format(name))
    response_count += 1

sys.exit("Good job {}, keep up with your studies!".format(name))