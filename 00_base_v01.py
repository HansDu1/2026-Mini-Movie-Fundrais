import pandas
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

def currency(x):
    return "${:.2f}".format(x)



Max_ticket=5
ticket_sold=0

yes_no_list = ["yes","no"]
payment_list = ["cash","credit"]

all_names=[]
all_tickets_costs=[]
all_surcharges=[]

mini_movie_fundrais_dict = {
    "Name":all_names,
    "Ticket Price":all_tickets_costs,
    "Surcharge":all_surcharges
}

want_instructions = string_checker("Do you want to read the instructions? (y/n)",1,yes_no_list)


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

    pay_method = string_checker("Please choose a payment method (cash/credit): ",2,payment_list)
    if pay_method == "cash":
        surcharge = 0
    else:
        surcharge = ticket_cost * 0.05
    
    ticket_sold+=1
    
    all_names.append(name)
    all_tickets_costs.append(ticket_cost)
    all_surcharges.append(surcharge)


mini_movie_frame=pandas.DataFrame(mini_movie_fundrais_dict)
mini_movie_frame=mini_movie_frame.set_index("Name")

mini_movie_frame["Total"] = mini_movie_frame["Surcharge"] \
                            + mini_movie_frame["Ticket Price"]

mini_movie_frame['Profit'] = mini_movie_frame['Ticket Price'] - 5

total = mini_movie_frame['Total'].sum()
profit = mini_movie_frame['Profit'].sum()

add_dollars = ['Ticket Price','Surcharge','Total','Profit']
for var_item in add_dollars:
    mini_movie_frame[var_item] = mini_movie_frame[var_item].apply(currency)

print("---Ticket Data---")
print()
print(mini_movie_frame)
print()
print("Total Ticket Sales: ${:.2f}".format(total))
print("Total Profit: ${:.2f}".format(profit))
    
if ticket_sold==Max_ticket:
    print("Congratulations! You have sold all the tickets!")
else:
    print("You have sold {} tickets. There are {} tickets left.".format(ticket_sold, Max_ticket-ticket_sold))