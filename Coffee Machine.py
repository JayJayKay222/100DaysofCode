from main import MENU, resources

total_money = 0
# coffee details 
def coffee_details(coffee_type):
    return MENU.get(coffee_type)

# cost of the coffee
def coffee_cost_(coffee_type):
    coffee_info = coffee_details(coffee_type)
    return coffee_info["cost"]

# available resources for the coffee
def check_resources(coffee_type):
    coffee_info = coffee_details(coffee_type)
    if coffee_info:
        ingredients = coffee_info["ingredients"]
        return all(resources.get(ingredient, 0) >= size for ingredient, size in ingredients.items())

 # reduce ingredients
def reduce_resources(coffee_type):
    if check_resources(coffee_type):
        ingredients = coffee_details(coffee_type)["ingredients"]
        for ingredient, size in ingredients.items():
            resources[ingredient] -= size
        return True
    return False           

# ask and sell coffee to the user
def get_coffee():
    global total_money
    EndProgram = False
    while not EndProgram:
        user_coffee = input("What would you like? espresso/ latte/ cappuccino: ").lower()
        coffee_list = ["espresso", "latte", "cappuccino"]
        maintainance = ["off", "report"]
        
        if user_coffee in coffee_list:
            coffee_cost = coffee_cost_(user_coffee)
            if user_coffee is not None:
                print(f"Your cost is: ${coffee_cost}")
                # check resources sufficiency
                if check_resources(user_coffee):
                    print(f"Please insert coin.\n")
                    quarters = int(input("How many quarters? "))
                    dimes = int(input("How many dimes? "))
                    nickles = int(input("How many nickles? "))
                    pennies = int(input("How many pennies? "))

                    total = ((quarters*25) + (dimes*10) + (pennies*1)) / 100.0
                    change = total - coffee_cost

                    # check if money inserted is sufficient
                    if coffee_cost > total:
                        print("Sorry! Not enough money.\n Money refunded.")
                    else:
                        print(f"Here is your change ${change}.\n Have your {user_coffee.title()} and Enjoy.\n")
                        reduce_resources(user_coffee)
                        total_money += coffee_cost
                else:
                    print("Sorry! Not enough resources.")
            else:
                print("Invalid input")
        elif user_coffee in maintainance:
        # print report or switch off machine 
            if user_coffee == "report":
                for key, value in resources.items():
                    print(f"{key}: {value}")
                print(f"You've made ${total_money:.2f} so far.")    
            elif user_coffee == "off":
                EndProgram = True
get_coffee()                                        