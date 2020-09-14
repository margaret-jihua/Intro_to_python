class Sushi():
    def __init__(self, plate):
        self.plate = plate
        self.amount = 0

    def orderSushi(self, amount):
        self.amount += amount
        print("You ordered {} pices of sushi. Enjoy!".format(self.amount))

    def eatSushi(self, amount):
        self.amount -= amount
        print("You have {} pices of sushi left.".format(self.amount))

    def emptyPlate(self):
        self.amount = 0
        print("Your {} size plate is now finished.".format(self.plate))

my_sushi = Sushi("medium")
print("You ordered a {} size plate, taking your order now...".format(my_sushi.plate))

my_sushi.orderSushi(12)
my_sushi.eatSushi(5)
my_sushi.emptyPlate()