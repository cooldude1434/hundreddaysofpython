MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

# TODO: first get input

machine_on = True


def generate_report():
    print(f"Water: {resources['water']} ml")
    print(f"Milk:  {resources['milk']} ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${money}")


def check_resources(drink):
    if resources['water'] >= MENU[drink]['ingredients']['water']:
        if resources['coffee'] >= MENU[drink]['ingredients']['coffee']:
            if drink == 'espresso':
                return 'available'
            elif resources['milk'] >= MENU[drink]['ingredients']['milk']:
                return 'available'
            else:
                return 'milk'
        else:
            return 'coffee'
    else:
        return 'water'


def make_drink(choosed):
    resources["water"] = resources["water"] - MENU[choosed]['ingredients']['water']
    resources["coffee"] = resources["coffee"] - MENU[choosed]['ingredients']['coffee']
    if choosed == 'latte' or choosed == 'cappuccino':
        resources["milk"] = resources["milk"] - MENU[choosed]['ingredients']['milk']


def get_coins_count():
    print("Insert coins")
    quarter = int(input("How many Quarters: "))
    dimes = int(input("How many dimes: "))
    nickel = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))

    return round(((quarter * 0.25) + (dimes * 0.1) + (nickel * 0.05) + (pennies * 0.01)), 2)


def check_price(choice, coins):
    if coins == MENU[choice]['cost']:
        return 0
    elif coins < MENU[choice]['cost']:
        return -1
    elif coins > MENU[choice]['cost']:
        return coins - MENU[choice]['cost']


money = 0

while machine_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ").lower()

    if choice == 'off':
        machine_on = False
    elif choice == 'report':
        generate_report()
    else:
        stock_check = check_resources(choice)
        coins = get_coins_count()
        enough = check_price(choice, coins)
        if stock_check == 'available':

            if enough == -1:
                print("sorry not enough coins")
            else:
                make_drink(choice)
                money = money + MENU[choice]['cost']
                money = round(money, 2)

                if enough != 0:
                    print(f"Here is ${enough} in change")
                print(f"Here is your {choice}, . Enjoy")

        else:
            print(f"Sorry, {stock_check} not sufficient for {choice}, money will be returned")

    # if choice == 'latte' or choice == 'espresso' or choice == 'cappuccino':

# TODO: do loop
