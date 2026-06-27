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

def string_checker(question, num_letters, valid_responses):
    error="please choose{} or {}".format(valid_responses[0],valid_responses[1])
    if num_letters == 1:
        short_version=1
    else:
        short_version=2

    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response == item[:short_version] or response == item:
                return item
        print(error)


Max_ticket=3
ticket_sold=0

yes_no_list = ["yes","no"]
payment_list = ["cash","credit"]

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

    payment_method = string_checker("Please choose a payment method (cash/credit): ",2,payment_list)
    print("Age: {}, ticket price: ${:.2f}".format(age, ticket_cost))  
    
    ticket_sold+=1
    
if ticket_sold==Max_ticket:
    print("Congratulations! You have sold all the tickets!")
else:
    print("You have sold {} tickets. There are {} tickets left.".format(ticket_sold, Max_ticket-ticket_sold))