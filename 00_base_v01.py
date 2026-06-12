def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Please enter yes or no.")


def not_blank(question):
    while True:
        response = input(question)
        if response=="":
            print("sorry, this can't be blank. Please try again.")
        else:
            return response
        

def num_check(question):
    while True:
        try:
            response=int(input(question))
            return response
        except ValueError:
            print("Please enter an integer.")



Max_ticket=3
ticket_sold=0

want_instructions = yes_no("Do you want to read the instructions? ")


if want_instructions=="yes":
    print("Instruction go here.")

print()
   


while ticket_sold<Max_ticket:
    name=not_blank("Please enter your name (or 'xxx' to quit): ")
    
    if name=="xxx":
        break
     
    age=num_check("Age: ")

    if 12<=age<=120:
        pass
    elif age<12:
        print("Sorry, you are too young for this movie.")
        continue
    else:
        print("That looks like a typo, please try again.")
        continue
    ticket_sold+=1
    
if ticket_sold==Max_ticket:
    print("You have sold all the tickets!")
else:
    print("You have sold {} tickets. There are {} tickets left.".format(ticket_sold, Max_ticket-ticket_sold))