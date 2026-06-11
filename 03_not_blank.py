def not_blank(question):
    while True:
        response = input(question)
        if response=="":
            print("sorry, this can't be blank. Please try again.")
        else:
            return response
        

while True:
    name=not_blank("Please enter your name (or 'xxx' to quit): ")
    if name == "xxx":
        break
print("we are done.")