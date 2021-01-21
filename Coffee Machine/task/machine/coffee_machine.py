# Write your code here
# Write your code here
start = "Starting to make a coffee"
grind = "Grinding coffee beans"
boil = "Boiling water"
mixing = "Mixing boiled water with crushed coffee beans"
coffee = "Pouring coffee into the cup"
milk = "Pouring some milk into the cup"
ready = "Coffee is ready!"
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

print("Write how many cups of coffee you will need:")
number_coffees = int(input())
print("For", number_coffees, "cups of coffee you will need:")

for index in range(len(quantities)):
    print(quantities[index] * number_coffees, texts[index])
