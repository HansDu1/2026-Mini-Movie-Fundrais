def string_checker(question,numletters,valid_responses):
    while True:
        response = input(question).lower()
        for item in valid_responses:
            if response == item[0] or response == item:
                return item
        print("Please choose a valid option.")

yes_no_list = ["yes""no"]
payment_list = ["cash","credit"]

for case in ["yes_no","payment"]:
    if case == "yes_no":
        response = string_checker("Do you want to read the instructions? (y/n)",1,yes_no_list)
    print("You chose, want_instructions")

