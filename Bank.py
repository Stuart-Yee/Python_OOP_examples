"""
Object Oriented Programming (OOP) Basics

Object Oriented Programming (OOP) is a cornerstone
concept in modern programming

A Class in Python is the blueprint for an Object. 
When we say 'Class' we mean the blueprint that defines 
the object whereas an object is a specific instance of 
that class. For example, you may have a Car Class and 
Car objects mercedes and acura

Objects can have two different components, attributes
and methods. Attributes are variables for data 
within an object (such as height, account balance, etc.)
and methods are functions within Classes that define
something that object can do.

The Four Principles of OOP are 
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

Copyright 2022 Stuart Yee
"""

# Classes in Python often represent types of tangible real world
# objects like customers, cars or pets
class Customer():

    # ABSTRACTION: Attributes store data and methods store logic
    # inside the Class as listed below

    #class attribute
    country = "USA"

    #constructor - Python uses a special 'dunder' method called
    # __init__()
    # you can declare parameters to take in arguments
    # as in any other function
    # the constructor and every other standard method always
    # takes in the self parameter
    def __init__(self, name, address, _TID, _PIN):
        # the __init__() establishes object instance 
        # attributes which are preceded by self. 
        # coders often assign beginning values from the 
        # constructor arguments or with a default value
        self.name = name
        self.address = address

        # ENCAPSULATION: attributes are typically concealed
        # from outside the object and used internally 
        # when needed. Python does not offer 'Private'
        # attributes or methods, so attributes or methods
        # that would be private are preceded by an underscore

        self._PIN = _PIN
        self._TID =_TID
        self._accounts = []

    # it's common to have 'getters' and 'setters' for
    # a Class's attributes. This way external code does
    # not access the object's attributes directly    

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_accounts(self):
        return self._accounts

    # Since the PIN is sensitive data and we don't want it to be accessed externally, 
    # we're going to write a grant_access() method instead of a "getter" for the PIN

    def grant_access(self, PIN_entry):
        # since this object and others have several "private" attributes 
        # indicated by a preceeding underscore, getters are not
        # simply going to return a value, we're going to authenticate
        # by having the user enter a PIN
        if PIN_entry == self._PIN:
            # in a real world scenario involving an actual bank,
            # there'd likely be more sophisticated authentication
            # logic using hashes and salts-- that's another topic 
            # though!
            return True
        else:
            return None

    def add_account(self, account):
        self._accounts.append(account) # when we create new accounts, we can add them
        # to the list of accounts for this customer   
        # since we've delcared an empty list for the _accounts
        # attribute, we can use .append() to add the new account.
        # This might not be the first time using this method so
        # there might already be one or more accounts when this
        # code runs     

# Sometimes we use Classes to represent things that aren't tangible in the real world
# like bank accounts, insurance policies, orders, etc. Sometimes classes are used
# to create even more abstract objects like authenticators, API connectors, or 
# query sets for a database

class Bank_Account():

    #class attribute
    bank_name = "Best Bank Ever"
    _accounts = 0

    def __init__(self, customer, balance):
        self.customer = customer
        self._balance = balance
        self._account_number = Bank_Account._accounts + 1 # cls is a shortcut to access the class
        Bank_Account._accounts += 1 # advance the number of total accounts
        customer.add_account(self) # add this account to that customer's list of accounts

    def get_acct_num(self, PIN_entry): # self argument automatically passed in
        if self.customer.grant_access(PIN_entry):
            return self._account_number
        else:
            return None
    
    def get_balance(self, PIN_entry):
        if self.customer.grant_access(PIN_entry): 
            return self._balance
        else:
            return None

    def withdraw(self, PIN_entry, amount): # generally it's a good practice to name methods as a verb
        if self.customer.grant_access(PIN_entry):
            if amount <= self.balance:
                self.balance -= amount
                return f"You have withdrawn ${amount} and your new balance is ${self.balance}"
            else:
                return "Insufficient funds"
        else:
            return "Incorrect PIN"     

    def __str__(self): # This is another "dunder" or double underscore method
        return str(self._account_number)

    @classmethod # This is a decorator! It let's us know this is a "class method"
    def get_num_accounts(cls): #instead of self, cls is automatically passed in since this is a class method
        return str(cls._accounts)

# INHERITANCE - we can create "child" class that inherit from the "super" class

class Savings_Account(Bank_Account):

    # Child classes can inherit the same constructors or 
    # you can write modified versions
    def __init__(self, customer, balance, min, interest): 
        super().__init__(customer, balance) # calling the __init__() of the super class
        self.interest = interest
        self.min = min # savings accounts have a minimum balance to earn interest

    # Add method to earn interest
    def earn_interest(self):
        self._balance += 1.0 + self._balance*self.interest

    # POLYMORPHISM: By default, the child class inherits all the methods of the parent
    # class. But you can override how a given method it inherits is implemented

    def withdraw(self, PIN_entry, amount, override): # we're overriding how the withdraw() method is implemented
        # through inheritance!
        if self.customer.grant_access(PIN_entry): 
            if amount <= self.balance and (amount <= self.balance + self.min or override == True):
                self.balance -= amount
                return f"You have withdrawn ${amount} and your new balance is ${self.balance}"
            elif amount > self.balance:
                return "Insufficient funds"
            else:
                return "The amount you requested will reduce your balance below the minimum " \
                "for this account and you won't earn interest"
        else:
            return "Incorrect PIN"

"""
Recap on the four principles of OOP and how the above example employees them

ABSTRACTION: By creating a class which includes attributes and methods, we can reuse that code
without having to worry about what's going on inside. Anytime we call .get_balance() and pass a PIN
as an argument (i.e. my_account.get_balance(1234)), we don't have to worry about how it's checking
the PIN as that logic is enclosed in the class

ENCAPSULATION: As a practice, we don't want to access an object's attributes directly. Unlike languages like
Java, there's no way to prevent this programmatically in Python so as a habit we use "getters" and "setters".
Sometimes for attributes and even methods that are particularly "private", we precede them with an underscore
as we did with _PIN and _TID

INHERITANCE: We created the the Bank_Account Class with the intention that it would have all the attributes
and methods any type of Bank Account would need. By creating the Savings_Account as a child of Bank_Account,
a Savings_Account object has all the attributes and methods of the Bank_Account Class. This is
convenient as it saves us from rewriting code!

POLYMORPHISM: This is tricky to define but it's the general idea child classes can do the same thing
as parent classes but in a slightly different way. Both the Bank_Account Class and Savings_Account class
have the withdraw() method, but the Savings_Account Class implements it differently.

"""
        
