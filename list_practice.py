team = []
members = 1

prompt = str.upper(input("Hello, would you like to add a player to the team? (Yes/No)  "))

while prompt == "YES":
    team.append(input("Please enter the player's name:  "))
    prompt = str.upper(input("\nWould you like to add another player to the team? (Yes/No)  "))

print("\nThere are {} players on the team:".format(len(team)))

for person in team:
    print("Player {}: {}".format(members, person))
    members += 1

try:
    goalkeeper = int(input("\nPlease enter player number to asign to 'Goalkeeper' from 1 - {}:  ".format(len(team))))
except ValueError as gk_err:
    
    while ValueError:
        try:
            goalkeeper = int(input("\nERROR: Please enter a valid number to asign to 'Goalkeeper' from 1 - {}:  ".format(len(team))))
        except ValueError:
            continue
        else:
            break

finally:
    if goalkeeper:
        print("\nThe Goalkeeper is: {}!".format(team[goalkeeper - 1]))