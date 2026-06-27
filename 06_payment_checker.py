def cash_credit(question):
    
    while True:
        response = input(question).lower()
        if response == "cash" or response == "ca":
            return "cash"
        elif response == "credit" or response == "cr":
            return "credit"
        else:
            print("Please choose a valid payment method")


while True:
    payment_method = cash_credit("Please choose a payment method (cash/credit): ")
    print(f"You have chosen {payment_method} as your payment method.")
    print("Program continues...")
    print()