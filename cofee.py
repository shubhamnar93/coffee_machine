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
did_machine_give_coffee=True


def making_coffee(coffee_type,element):
    global MENU
    global did_machine_give_coffee
    for coffees in MENU[coffee_type]["ingredients"]:
        if MENU[coffee_type]["ingredients"][coffees]>element[coffees]:
            print("insufficient ingredient")
            did_machine_give_coffee=False
            return
    print(f"cost: {MENU[coffee_type]["cost"]}")
    # 0.01
    penny=int(input("how many penny you want to give: "))
    #0.05
    nickel=int(input("how many nickel you want to give: "))
    #0.1
    dime=int(input("how many dime you want to give: "))
    #0.25
    quarter=int(input("how many quarter you want to give: "))
    total_amount_paid=(penny*0.01)+(nickel*0.05)+(dime*0.1)+(quarter*0.25)
    tip=total_amount_paid-MENU[coffee_type]["cost"]
    if total_amount_paid<MENU[coffee_type]["cost"]:
        print (f"insufficient balance machine has eaten your {total_amount_paid}")
        did_machine_give_coffee = False
        return
    print(f"thank you for the tip of {tip}")


while input("do you want to turn of machine: ")=="no":
    report_coffee = input("you want coffee or report: ")
    if report_coffee=="report":
        for items in resources:
            print(f"{items}: {resources[items]}")
        if input("do you want to add more quantity of all: ")=="yes":
            for items in resources:
                x=int(input(f"how much amount of {items} do you want to add: "))
                resources[items]+=x
    else:
        coffee_type=input("do you want espresso latte cappuccino: ")
        making_coffee(coffee_type,resources)
        if did_machine_give_coffee:
            for coffees in MENU[coffee_type]["ingredients"]:
                resources[coffees]-=MENU[coffee_type]["ingredients"][coffees]