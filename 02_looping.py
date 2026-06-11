Max_ticket=3

ticket_sold=0

while ticket_sold<Max_ticket:
    name=input("Please enter your name or 'xxx' to quit: ")
    ticket_sold+=1
    if name=="xxx":
        break
    
if ticket_sold==Max_ticket:
    print("You have sold all the tickets!")
else:
    print("You have sold {} tickets. There are {} tickets left.".format(ticket_sold, Max_ticket-ticket_sold))