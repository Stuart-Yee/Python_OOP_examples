# With OOP, we can organize our files in a way that's 
# easy to navigate. We'll use our Bank.py strictly to
# code our Classes and will make use of them on this
# Main.py file with an import statement:
from Bank import Customer, Bank_Account, Savings_Account

#let's container our app's logic in a "run function"
def run():
    #let's create a customer:
    joe = Customer("Joe", "Main Street", "555-55-5555", 1234)

    #let's use the our "getter for the name"
    name = joe.get_name()
    print(name)

    #he should have a last name too
    joe.set_name("Joe Smith")
    name = joe.get_name()
    print(name)

    # let's create another customer and we'll declare the parameters
    # in the constructor
    lucy = Customer(name="Lucy Jones", address="123 5th Ave", _TID="123-12-1234", _PIN=4567)
    print(lucy.get_name())

    #let's create a checking and a savings account for lucy
    checking_lucy = Bank_Account(lucy, 1000)
    print("Account number", checking_lucy) # If we didn't implement __str__() checking_lucy would show up as 
    # something like "<Bank.Bank_Account object at [bunch of numbers for memory address]>"
    savings_lucy = Savings_Account(customer=lucy, balance=2000, min=200, interest=.02)
    print("Account number", savings_lucy)

    # Let's make sure Lucy's accounts are there
    print(lucy.get_accounts())

    # Let's see how many accounts we have
    accounts = Bank_Account.get_num_accounts()
    print("Total",accounts)

    #TODO HOMEWORK!!!

    # 1) create a customer
    # 2) Lucy got married! Change her last name
    # 3) Start at least one account for Joe and the new customer
    # 4) Code some withdrawals using the withdraw() method
    #     a) See what happens when the PIN is incorrect
    #     b) See what happens if you try to withdraw more than is available
    #     c) Make an unsuccessful attempt to withdraw an amount below min for savings
    #     d) Make a successful attempt to withdraw below the min for a savings
    # 5) There's no way to add money to an account!! Add a method to deposit money
    # 6) Joe has come into some money! Deposit $10,0000 into his account



# If the namespace is "__main__", we can run this code
# This file will only run if it's selected to run directly
if __name__=="__main__":
    run()

#Cool beans!
#Branching