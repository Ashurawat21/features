class ATM:
    def __init__ (self):
        self.pin = ""
        self.balance = 0
        self.menu()

    def menu(self):
        user_input = input("""Hello , how wold you like to proceed?
                           1.enter 1 to create pin
                           2.enter 2 to deposite
                           3.enter 3 to withraw
                           4.enter 4 to check balane
                           5.enter 5 to exit """)
        if user_input == "1":
            self.create_pin()
        elif user_input == "2":
            self.withraw()
        elif user_input == "3":
            self.deposit()
        elif user_input == "4":
            self.balance()
        else:
            print("bye")

    def create_pin(self):
        self.pin = input("enter the pin")
        print("pin set")
    def withraw(self):
        temp = input("enter the pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            if amount < self.balance:
                self.balance = self.balance - amount
                print("operation successfully")
            else:
                print("enter valid amount")
        else:
            print("not valid")
        print("pin set")
    def deposit(self):
        temp = input("enter the pin")
        if temp == self.pin:
            amount = int(input("enter the amount"))
            self.balance = self.balance+amount
            print("deposite successfully")
        else:
            print("pin is incorrect")
        print("pin set")
    def balance(self):
        temp = input("enter the pin")
        if temp == self.pin:
            print(self.balance)
        else:
            print("invalid pin")

         
obj = ATM()
new = obj("balance")
# print(new)





