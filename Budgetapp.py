
class Budget:

    def __init__ (self, name):
        self.name = name
        self.balance = 0

    def deposit(self, amount):
        self.balance = amount
        print("Transaction was successful")

        return f"your new balance is ${self.balance} in {self.name} budget"

    def withdraw(self, amount):
        if self.balance < amount:
            return "Error, insufficient funds"
        else:
            self.balance -= amount
            feedback = ("=============================\n")
            feedback += ("Transaction was successful \n")
            feedback += (f"your new balance is ${self.balance} in {self.name} budget")

            return feedback

    def compute_balance(self):
        feedback = f"your new balance is ${self.balance} in {self.name} budget"

        return feedback

    def transfer(self, amount, category):
        if self.name == category.name:
            feedback = "ERROR!!! \n"
            feedback += "You cannot transfer within the same category \n"

            return feedback

        elif self.balance < amount:
            return "Error, insufficient funds"
        else:
            self.balance -= amount
            category.balance += amount
            feedback = "=========================== \n"
            feedback += "Transaction was successful \n"
            feedback += f"The balance for {self.name} is ${self.balance} \n"
            feedback += f"The balance for {category.name} is ${category.balance} \n"

            return feedback




food = Budget("food")
clothing = Budget("clothing")
entertainment = Budget("entertainment")


print(f"{food.name} budget has ${food.balance}")
print(f"{clothing.name} budget has ${clothing.balance}")
print(f"{entertainment.name} budget has ${entertainment.balance}")
print("=================================")
print(food.deposit(3000))
print("=================================")
print(clothing.deposit(5000))
print("==================================")
print(entertainment.deposit(2000))



print(food.withdraw(1000))
print(clothing.withdraw(2000))
print(entertainment.withdraw(1500))



print("===================================")
print(food.compute_balance())
print("===================================")
print(clothing.compute_balance())
print("===================================")
print(entertainment.compute_balance())

print("===================================")
print(food.transfer(500, entertainment))
print(clothing.transfer(1500, food))
