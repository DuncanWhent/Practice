import sys

def multiply(userinput):
    try:
        userinput = int(userinput)
    except ValueError:
        try: 
            userinput = float(userinput)
        except ValueError:
            sys.exit("Please enter a number.")
        else:
            return userinput * 3, userinput * 5, userinput * 10
    else:
        return userinput * 3, userinput * 5, userinput * 10

userinput = input("Choose any number to be multiplied by 3, 5 and 10:    ")
print("Your results are: {}".format(multiply(userinput)))