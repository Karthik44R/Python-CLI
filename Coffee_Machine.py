
menu = {
    "Espresso": {
        "ingredients": {
            "water": 300,
            "coffee": 20,
        },
        "cost": 100
    },
    "Latte": {
        "ingredients": {
            "water": 230,
            "milk": 120,
            "coffee": 25,
        },
        "cost": 150
    },
    "Cappuccino": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 30,
        },
        "cost": 200
    }
}

profit = 0
resources = {
    "water": 5000,
    "milk": 2000,
    "coffee": 1000,
}

# To check ingredients available (or) not
def check_resources(order_ingredients):
    for item in order_ingredients:
        if order_ingredients[item] > resources[item]:
            print(f"Sorry there is not enough {item}")
            return False
    return True

# Money Insertion & calculation
def process_coins():
    print("Please insert Coins(₹5/₹10) / Notes(₹10/₹20): ")
    coins_5 = int(input("how many ₹5 coin: "))
    coins_10 = int(input("how many ₹10 coin: "))
    notes_10 = int(input("how many ₹10 notes: "))
    notes_20 = int(input("how many ₹20 notes: "))
    total = coins_5 * 5 + coins_10 * 10 + notes_10 * 10 + notes_20 * 20
    return total

# Printing the BILL
def is_payment_successful(money_received, coffee_cost):
    global profit
    if money_received >= coffee_cost:
        profit += coffee_cost
        change = money_received - coffee_cost
        print(f"Here is your ₹{change} in change")
        return True
    else:
        print("Sorry! that's not enough Money and your money will be Refunded")
        return False

# Start Coffee
def make_coffee(coffee_name, coffee_ingredient):
    for item in coffee_ingredient:
        resources[item] -= coffee_ingredient[item]
    print(f"here is your {coffee_name}☕.... Enjoy\nThankYou😊")

# While Loop runs continuously until typing off
is_on = True
while is_on:
    choice = input("What would you like to have \n1.Espresso\n2.Latte\n3.Cappuccino) : ").strip()
    if choice == '1':
        choice = 'Espresso'
    elif choice == '2':
        choice = 'Latte'
    elif choice == '3':
        choice = 'Cappuccino'

    if choice == 'off':
        is_on = False
        break
    elif choice == 'on':
        is_on = True
    elif choice == 'report':
        print(f"water={resources['water']}ml")
        print(f"milk={resources['milk']}ml")
        print(f"coffee={resources['coffee']}g")
        print(f"money=₹{profit}")
    if choice in menu:
        coffee_type = menu[choice]
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment, coffee_type['cost']):
                make_coffee(choice, coffee_type['ingredients'])
    else:
        print("Invalid Choice! Please choose 1 for Espresso, 2 for Latte, 3 for Cappuccino, 'report', or 'off'.\n")    

