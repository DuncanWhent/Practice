import sys
import math

TICKET_PRICE = 3.50
tickets_remaining = 100
attempts = 0

while tickets_remaining:
    print("There are {} tickets remaining!".format(tickets_remaining))
    
    user_name = input("Welcome, please enter your name below. \n")

    try:
        num_tickets = int(input("Hello {}, how many tickets would you like to purchase? \n".format(user_name)))
    except ValueError:
        print("ERROR: Please enter a valid number.\n")
        continue

    try:
        total_price = math.ceil(num_tickets * TICKET_PRICE)
    except NameError:
        continue

    finally:
        if num_tickets <= tickets_remaining:
            confirm = str.upper(input("Confirm your purchase of {} tickets for £{}, {}?\nPlease enter Y/N: \n".format(num_tickets, total_price, user_name)))

            while confirm != "Y" or "N":
                attempts +=1
                if attempts > 3:
                    print("ERROR: Exhausted attempts, please try again.\n")
                    attempts = 0
                    break
                elif confirm == "Y":
                    # Gather purchase information and proceed.
                    tickets_remaining -= num_tickets
                    print("Thankyou for your purchase {}, have a nice day! \n".format(user_name))
                    break
                elif confirm == "N":
                    print("Purchase cancelled. Thankyou for using our app {}.\n".format(user_name))
                    break
                else:
                    confirm = input("Invalid input! \nPlease enter Y/N: \n")

        else:
            print("ERROR: Not enough tickets available.\n")
else:
    sys.exit("SOLD OUT!")