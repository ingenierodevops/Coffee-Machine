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
# print(start)
# print(grind)
# print(boil)
# print(mixing)
# print(coffee)
# print(milk)
# print(ready)

# initial status
status = "The coffee machine has:"

water_status = 400
water_status_text = "of water"

milk_status = 540
milk_status_text = "of milk"

coffee_status = 120
coffee_status_text = "of coffee beans"

cup_status = 9
cup_status_text = "of disposable cups"

money_status = 550
money_status_text = "of money"

machine_status = [water_status, milk_status, coffee_status, cup_status, money_status]
coffe_quantities = [[250, 0, 16, 1, -4],[350, 75, 20, 1, -7],[200, 100, 12, 1, -6]]

def print_status(stat_mach):
    print(status)
    print(stat_mach[0], water_status_text)
    print(stat_mach[1], milk_status_text)
    print(stat_mach[2], coffee_status_text)
    print(stat_mach[3], cup_status_text)
    print(stat_mach[4], money_status_text)

def menu():
    print("Write action(buy, fill, take):")
    return input()

def analize_action(action):
    if action == "buy":
        tipo_cafe = choose_coffee()
        make_coffee(tipo_cafe)
    elif action == "fill":
        fill_machine()
    elif action == "take":
        take_money()

def choose_coffee():
    print("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino:")
    return input()


def make_coffee(c_type):
    global machine_status
    tipo_number = 0
    if c_type == "1":
        tipo_number = 0
    elif c_type == "2":
        tipo_number = 1
    elif c_type == "3":
        tipo_number = 2
    index = 0
    for state in machine_status:
        state = state - coffe_quantities[tipo_number][index]
        machine_status[index] = state
        index += 1

def fill_machine():
    global machine_status
    print("Write how many ml of water do you want to add:")
    machine_status[0] += int(input())
    print("Write how many ml of milk do you want to add:")
    machine_status[1] += int(input())
    print("Write how many grams of coffee beans do you want to add:")
    machine_status[2] += int(input())
    print("Write how many disposable cups of coffee do you want to add:")
    machine_status[3] += int(input())


def take_money():
    global machine_status
    money_gave = machine_status[4]
    machine_status[4] = 0
    print("I gave you $" + str(money_gave))

print_status(machine_status)
print()
action = menu()
analize_action(action)
print()
print_status(machine_status)

#  Ingredientes de un café
#  water = 200 #
#  water_text = "ml of water"
#  milk = 50 #
#  milk_text = "ml of milk"
#  coffee_beams = 15 #
#  coffee_text = "g of coffee beans"

#  texts = [water_text, milk_text, coffee_text]
#  quantities = [water, milk, coffee_beams]

#  yes_can = "Yes, I can make that amount of coffee"

#  print(ask_water)
#  water_in_machine = int(input())
#  print(ask_milk)
#  milk_in_machine = int(input())
#  print(ask_coffee)
#  coffee_in_machine = int(input())

#  print(how_many)
#  number_coffees = int(input())

#  water_coffees = water_in_machine / water
#  milk_coffees = milk_in_machine / milk
#  coffee_coffees = coffee_in_machine / coffee_beams
#  capacidad = [water_coffees, milk_coffees, coffee_coffees]

#  capacidad_real = min(capacidad)

#  if capacidad_real >= number_coffees:
    #      extra = capacidad_real - number_coffees
    #  if extra > 1:
    #          print("Yes, I can make that amount of coffee (and even", int(extra),"more than that)")
    #  else:
#          print("Yes, I can make that amount of coffee")
#  else:
#      print("No, I can make only", int(capacidad_real), "cups of coffee")
#print("For", number_coffees, "cups of coffee you will need:")

# for index in range(len(quantities)):
#    print(quantities[index] * number_coffees, texts[index])
