def num_check(question):
    while True:
        try:
            response=int(input(question))
            return response
        except ValueError:
            print("Please enter an integer.")
           

ticket_sold = 0

while True:
    name = input("Please enter your name (or 'xxx' to quit): ")
    if name == "xxx":
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

print("You have sold {} tickets.".format(ticket_sold))
        