# Write your code here
# Write your code here
start = "Starting to make a coffee"
grind = "Grinding coffee beans"
boil = "Boiling water"
mixing = "Mixing boiled water with crushed coffee beans"
coffee = "Pouring coffee into the cup"
milk = "Pouring some milk into the cup"
ready = "Coffee is ready!"

ask_water = "Write how many ml of water the coffee machine has:"
ask_milk = "Write how many ml of milk the coffee machine has:"
ask_coffee = "Write how many grams of coffee beans the coffee machine has:"

how_many = "Write how many cups of coffee you will need:"


# initial status
status = "The coffee machine has:"

water_status_text = " of water"
milk_status_text = " of milk"
coffee_status_text = " of coffee beans"
cup_status_text = " of disposable cups"
money_status_text = " of money"

coffe_quantities = [[250, 0, 16, 1, -4],[350, 75, 20, 1, -7],[200, 100, 12, 1, -6]]

class CoffeeMachine:
    def __init__(self, water_status, milk_status, coffee_status, cup_status, money_status):
        self.machine_status = [water_status, milk_status, coffee_status, cup_status, money_status]
        self.machine_state = "waiting"

    def __str__(self):
        texto = status
        texto = texto + '\n' + str(self.machine_status[0]) + water_status_text
        texto = texto + '\n' + str(self.machine_status[1]) + milk_status_text
        texto = texto + '\n' + str(self.machine_status[2]) + coffee_status_text
        texto = texto + '\n' + str(self.machine_status[3]) + cup_status_text
        texto = texto + '\n' + str(self.machine_status[4]) + money_status_text + '\n'
        return texto

    def fill_machine(self):
        # todo this method must be called for every inputed string not reading input here

        if self.machine_state == "waiting":  # waiting for instructions
            print("Write how many ml of water do you want to add:")
            self.machine_status[0] += int(input())
            print("Write how many ml of milk do you want to add:")
            self.machine_status[1] += int(input())
            print("Write how many grams of coffee beans do you want to add:")
            self.machine_status[2] += int(input())
            print("Write how many disposable cups of coffee do you want to add:")
            self.machine_status[3] += int(input())

    def check_coffee(self, c_type):
        tipo_number = 0
        if c_type == "1":
            tipo_number = 0
        elif c_type == "2":
            tipo_number = 1
        elif c_type == "3":
            tipo_number = 2
        index = 0
        puedo = True
        for state in self.machine_status:
            state = state - coffe_quantities[tipo_number][index]
            if state < 0:
                puedo = False
            index += 1
        if puedo == True:
            print("I have enough resources, making you a coffee!")
            return False
        else:
            print("I can't make a cup of coffee")
            return True

    def make_coffee(self, c_type):
        tipo_number = 0
        if c_type == "1":
            tipo_number = 0
        elif c_type == "2":
            tipo_number = 1
        elif c_type == "3":
            tipo_number = 2
        index = 0
        for state in self.machine_status:
            state = state - coffe_quantities[tipo_number][index]
            self.machine_status[index] = state
            index += 1

    def take_money(self):
        money_gave = self.machine_status[4]
        self.machine_status[4] = 0
        print("I gave you $" + str(money_gave))




def analize_action(action, coffee_machine):
    print()
    if action == "buy":
        print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
        tipo_cafe = input()
        if tipo_cafe != "back":
            if not coffee_machine.check_coffee(tipo_cafe):
                coffee_machine.make_coffee(tipo_cafe)
    elif action == "fill":
        coffee_machine.fill_machine()
    elif action == "take":
        coffee_machine.take_money()
    elif action == "remaining":
        print(coffee_machine)
    elif action == "exit":
        return False
    return True


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

sigue = True
while sigue:
    print("Write action(buy, fill, take, remaining, exit):")
    action = input()
    sigue = analize_action(action, coffee_machine)
