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


def calc_ticket_price(var_age):
    if var_age<16:
        price = 7.5
    elif var_age<65:
        price = 10.5
    else:
        price = 6.5
    
    return price



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
        print("?? That looks like a typo, please try again.")
        continue
    
    
    ticket_cost = calc_ticket_price(age)
    print("Age: {}, ticket price: ${:.2f}".format(age, ticket_cost))
    
    ticket_sold+=1
    
if ticket_sold==Max_ticket:
    print("You have sold all the tickets!")
else:
    print("You have sold {} tickets. There are {} tickets left.".format(ticket_sold, Max_ticket-ticket_sold))