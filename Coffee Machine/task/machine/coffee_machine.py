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

# Ingredientes de un café
water = 200 #
water_text = "ml of water"
milk = 50 #
milk_text = "ml of milk"
coffee_beams = 15 #
coffee_text = "g of coffee beans"

texts = [water_text, milk_text, coffee_text]
quantities = [water, milk, coffee_beams]

yes_can = "Yes, I can make that amount of coffee"

print(ask_water)
water_in_machine = int(input())
print(ask_milk)
milk_in_machine = int(input())
print(ask_coffee)
coffee_in_machine = int(input())

print(how_many)
number_coffees = int(input())

water_coffees = water_in_machine / water
milk_coffees = milk_in_machine / milk
coffee_coffees = coffee_in_machine / coffee_beams
capacidad = [water_coffees, milk_coffees, coffee_coffees]

capacidad_real = min(capacidad)

if capacidad_real >= number_coffees:
    extra = capacidad_real - number_coffees
    if extra > 1:
        print("Yes, I can make that amount of coffee (and even", int(extra),"more than that)")
    else:
        print("Yes, I can make that amount of coffee")
else:
    print("No, I can make only", int(capacidad_real), "cups of coffee")
#print("For", number_coffees, "cups of coffee you will need:")

# for index in range(len(quantities)):
#    print(quantities[index] * number_coffees, texts[index])
