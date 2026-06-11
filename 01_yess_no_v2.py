def yes_no(question):
    while True:
        response = input(question).lower()
        if response == "yes" or response == "y":
            return True
        elif response == "no" or response == "n":
            return False
        else:
            print("Please enter yes or no.")



want_instructions = yes_no("Do you want to read the instructions? ")


if want_instructions:
    print("Instruction go here.")

print("We are done.")