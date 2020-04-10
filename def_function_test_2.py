def multiply(userinput):
    try:
        userinput = int(userinput)
    except ValueError:
        print("Type a number you dumbass...")
    else:
        print(userinput * 3, userinput * 5, userinput * 10)

userinput = input("Choose any number to be multiplied by 3, 5 and 10:    ")
multiply(userinput)