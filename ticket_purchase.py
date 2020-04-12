import sys
import math

TICKET_PRICE = 10
SERVICE_CHARGE = 2

tickets_remaining = 100
attempts = 0

def total_price():
    return math.ceil((num_tickets * TICKET_PRICE) + SERVICE_CHARGE)

while tickets_remaining:
    print("There are {} tickets remaining!".format(tickets_remaining))
    user_name = input("Welcome, please enter your name below. \n")
    try:
        num_tickets = int(input("Hello {}, how many tickets would you like to purchase? \n".format(user_name)))
    except ValueError as tickets_err:
        print("ERROR: Please enter a valid number.\n")
        continue
    else:
        while num_tickets <= tickets_remaining:
            if attempts >= 3:
                print("ERROR: Exhausted attempts, please try again.\n")
                attempts = 0
                break
            else:
                confirm = str.upper(input("Confirm your purchase of {} tickets for £{}, {}?\nPlease enter Y/N: \n".format(num_tickets, total_price(), user_name)))
                if confirm == "Y":
                    # Gather purchase information and proceed.
                    tickets_remaining -= num_tickets
                    print("Thankyou for your purchase {}, have a nice day!\n".format(user_name))
                    attempts = 0
                    break
                elif confirm == "N":
                    print("Purchase cancelled. Thankyou for using our app {}.\n".format(user_name))
                    attempts = 0
                    break
                else:
                    print("ERROR: Invalid input, please try again.\n")
                    attempts += 1
        else:
            print("ERROR: Not enough tickets available.\n")
else:
    sys.exit("SOLD OUT!\n")