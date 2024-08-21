
import time
import pandas as pd


def num_checker(question, low, high):
    while True:
        error = f"Enter a valid option"
        try:
            user_response = int(input(question))
            if low <= user_response <= high:
                return user_response
            else:
                print(error)
        except ValueError:
            print(error)


def string_checker(question, valid_ans):
    error = f"Enter a valid option from {valid_ans}"
    while True:

        user_response = input(question).lower()
        for item in valid_ans:
            if item == user_response or user_response == item[0]:
                return item
        print(error)


def not_blank(question):
    error = "Please give a valid answer."
    while True:
        user_name = input(question)
        if user_name != '':
            return user_name
        else:
            print(error)

def pizza_size_checker(pizza_size):
    if pizza_size == "small":
        return 5
    elif pizza_size == "medium":
        return 9.99
    else:
        return 12


def drink_size_checker(drink_size):
    if drink_size == "can":
        return 3.3
    else:
        return 5


# uses pizza id and the size variable to assign the pizza name and the price
def pizza_selector(pizza):
    # Initialize variables with default values
    pizza_name = "The Lot"
    pizza_cost = 9.99

    if pizza == 1:
        pizza_name = "Lamb Kebab"

    elif pizza == 2:
        pizza_name = "Crispy BBQ Pork Belly"

    elif pizza == 3:
        pizza_name = "The Lot"

    elif pizza == 4:
        pizza_name = "Chicken and bacon aoli"

    elif pizza == 5:
        pizza_name = "Smokehouse Meat lover"

    elif pizza == 6:
        pizza_name = "Peri-Peri Chicken"

    elif pizza == 7:
        pizza_name = "Philly Cheese steak"

    elif pizza == 8:
        pizza_name = "Supreme"

    elif pizza == 9:
        pizza_name = "Double Bacon Cheeseburger"

    elif pizza == 10:
        pizza_name = "Butter Chicken"

    elif pizza == 11:
        pizza_name = "BBQ Meat lovers"

    elif pizza == 12:
        pizza_name = "Chicken Supreme"

    elif pizza == 13:
        pizza_name = "Cheesy Garlic Pizza"

    elif pizza == 14:
        pizza_name = "Pepperoni"

    elif pizza == 15:
        pizza_name = "Ham Cheese"

    elif pizza == 16:
        pizza_name = "Simply Cheese"

    elif pizza == 17:
        pizza_name = "Hawaiian"

    else:
        pizza_name = "Mega Pepperoni"

    return pizza_name

# uses drink id and the size variable to assign the drink name and the price
def drink_selector(drink, drink_size):
    # Initialize variables with default values
    drink_name = "Coke"
    drink_cost = 9.99

    if drink == 1:
            drink_name = "Coke"

    elif drink == 2:
            drink_name = "Fanta"

    elif drink == 3:
            drink_name = "Lift"

    elif drink == 4:
            drink_name = "Sprite"

    elif drink == 5:
            drink_name = "Coke Zero"

    elif drink == 6 :
            drink_name = "L & P"

    return drink_name, drink_cost

def calculate_price(pizza_order_size, drink_size, delivery):
    pizza_prices = {'small': 5, 'medium': 9.99, 'large': 12}
    drink_prices = {'bottle': 5, 'can': 3.30}

    # Calculate pizza cost
    pizza_cost = sum(pizza_prices[size] for size in pizza_order_size)

    # Calculate drink cost if drink_size is not 'none'
    drink_cost = 0
    if drink_size != 'none':
        drink_cost = drink_prices[drink_size]

    # Add $6 surcharge for delivery
    if delivery == "delivery":
        return pizza_cost + drink_cost + 6
    else:
        return pizza_cost + drink_cost


# set maximum number of tickets below
MAX_PIZZA = 5

# Variables
yes_no = ["yes", "no"]
deliv_option = ["delivery", "pick up"]
size_option = ["large", "medium", "small"]
size_drink = ["can", "bottle"]

pizza_order = []
pizza_order_size = []
drink_order = []
drink_size = 'none'  # Initialize with a placeholder value

# Welcome message
print("<---Welcome to Puppet Pizzaria--->")
print()

# instructions question
want_instruc = string_checker("Would you like to read the instuctions: ", yes_no)

if want_instruc == "yes":
    print('''
|-----Instructions-----|
-When answering a question you can put the first letter of
 the word and it will go through as correct

-The code will ask for your name, phone number, address (if clicked delivery), 
 pizza flavour, size, drink and drink size.
    ''')

delivery = string_checker("Is this order pick up or delivery? ", deliv_option)

if delivery == "delivery":
    print("There is a $6 surcharge for delivery")

    # Ask for name and details
    print()
    name = not_blank("Enter your name: ")

    # Ask for phone number
    print()
    phone_num = num_checker("Enter your phone number: ", 9999999, 99999999999)

    # Ask for address
    print()
    address = not_blank("Enter your address: ")

else:
    # Ask for name and details
    name = not_blank("Enter your name: ")
    # Ask for phone number
    phone_num = num_checker("Enter your phone number: ", 9999999, 99999999999)

# Time wait
time.sleep(.5)

# Do you want the Menu?
print()
want_menu = string_checker(f"Hello {name}, would you like the menu? ", yes_no)

if want_menu == "yes":

    # Set display options for pandas

    all_names = ["Lamb Kebab", "Crispy BBQ Pork Belly", "The Lot", "Chicken Bacon & Aoli", "Smokehouse Meat lover",
                 "Peri-Peri chicken", "philly cheese steak", "supreme", "Double Bacon Cheeseburger", "Butter Chicken", "BBQ Meat lovers", "Chicken Supreme", "Cheesy Garlic Pizza", "Pepperoni", "Ham Cheese", "Simply Cheese", "Hawaiian", "Mega Pepperoni"]

    # all_names
    all_small_size = [5] * len(all_names)
    all_medium_size = [9.99] * len(all_names)
    all_large_size = [12] * len(all_names)


    df = pd.DataFrame({
        'Name': all_names,
        'Small Size Cost': all_small_size,
        'Medium Size Cost': all_medium_size,
        'large Size Cost': all_large_size

    })

    pd.set_option('display.max_columns', None)  # Show all columns
    pd.set_option('display.expand_frame_repr', False)  # Prevent wrapping
    pd.set_option('display.max_rows', None)  # Show all rows, if needed

    # Set index to start from 1
    df.index = range(1, len(df) + 1)

    print(df)

    keep_going = "yes"

    # While loop for user to keep adding to their pizza order
    while keep_going == "yes":
        # Pizza id question
        pizza_num_id = num_checker("Enter the pizza number: ", 1, 18)
        pizza_order.append(pizza_num_id)

        # Ask for size
        size = string_checker("What Size | Small | Medium | Large |: ", size_option)
        pizza_order_size.append(size)

        user_pizza_selection = pizza_selector(pizza_num_id)
        user_pizza_cost = pizza_size_checker(size)

        print(f"Great! You have selected a {user_pizza_selection}:  ${user_pizza_cost}")

        print()
        keep_going = string_checker("Do you want to order another pizza? ", yes_no)

    print(f"You have ordered the following: {pizza_order} with the sizes: {pizza_order_size}")

    # Price summary for food
    total_price = calculate_price(pizza_order_size, 'none', delivery)  # Use 'none' for initial calculation
    print(f"Your order so far costs = ${total_price:.2f} (including delivery)")

    # Time wait
    time.sleep(1)

    # Would you like the drink menu question
    want_menu = string_checker(f"{name}, would you like the drink menu? ", yes_no)

    if want_menu == "yes":
        # Set display options for pandas

        all_names = ["Coke", "Fanta", "Lift", "Sprite", "Coke Zero", "L & P"]

        # all_names
        all_CanmL_size = [3.3] * len(all_names)
        all_BottleLitre_size = [5] * len(all_names)


        df = pd.DataFrame({
            'Name': all_names,
            'Bottle (1.5L) Size Cost': all_CanmL_size,
            'Can (330mL) Cost': all_BottleLitre_size,

        })

        pd.set_option('display.max_columns', None)  # Show all columns
        pd.set_option('display.expand_frame_repr', False)  # Prevent wrapping
        pd.set_option('display.max_rows', None)  # Show all rows, if needed

        # Set index to start from 1
        df.index = range(1, len(df) + 1)

        print(df)

    keep_going = "yes"

    # While loop for user to keep adding to their drink order
    while keep_going == "yes":
        # Drink selection question
        drink_num_id = num_checker("Enter the drink number: ", 1, 6)
        drink_size = string_checker("What Size | Bottle (1.5L) | Can (330mL) |: ", size_drink)

        # Fetch drink name and cost using the selector function
        drink_name, drink_cost = drink_selector(drink_num_id, drink_size)

        print(f"Great! You have selected a {drink_name} ({drink_size})")

        # Add drink to order
        drink_order.append(drink_num_id)

        # loop question yes/no
        keep_going = string_checker("Do you want to order another drink? ", yes_no)

    # After finishing drink orders, display all selected drinks
    print(f"You have ordered the following drinks:")
    for drink_id in drink_order:
        drink_name, _ = drink_selector(drink_id, '330')  # assuming default size for display
        print(f"- {drink_name}")

    # Order price calculator (including drink if selected)
    total_price = calculate_price(pizza_order_size, drink_size, delivery)
    print(f"Your final order costs = ${total_price:.2f} (including delivery)")

    # Time wait
    time.sleep(2)

    # Order price calculator (including drink if selected)
    total_price = calculate_price(pizza_order_size, drink_size, delivery)
    print(f"Your final order costs = ${total_price:.2f} (including delivery)")

    # Time wait
    time.sleep(1)

    # pizza ready message
    print("Your pizza will be ready from 10 to 20 minutes")
    print("dont touch the keyboard")

    # Time wait
    time.sleep(3)

    # Loading bar simulation

    time.sleep(1)

    loading_steps = [

        "               ⣠⣤⣶⣶⣦⣄⣀",
        "⠀            ⢰⣿⣿⣿⣿⣿⣿⣿⣷⣦⡀",
        "⠀    ⠀       ⢠⣷⣤⠀⠈⠙⢿⣿⣿⣿⣿⣿⣦⡀⠀⠀⠀",
        "      ⠀   ⠀⠀⣠⣿⣿⣿⠆⠰⠶⠀⠘⢿⣿⣿⣿⣿⣿⣆⠀⠀⠀",
        "⠀ ⠀       ⢀⣼⣿⣿⣿⠏⠀⢀⣠⣤⣤⣀⠙⣿⣿⣿⣿⣿⣷⡀⠀",
        " ⠀     ⠀⡴⢡⣾⣿⣿⣷⠋⠁⣿⣿⣿⣿⣿⣿⣿⠃⠀⡻⣿⣿⣿⣿⡇",
        "⠀⠀    ⢀⠜⠁⠸⣿⣿⣿⠟⠀⠀⠘⠿⣿⣿⣿⡿⠋⠰⠖⠱⣽⠟⠋⠉⡇",
        "⠀⠀   ⡰⠉⠖⣀⠀⠀⢁⣀⠀⣴⣶⣦⠀⢴⡆⠀⠀⢀⣀⣀⣉⡽⠷⠶⠋⠀",
        "⠀  ⠀⡰⢡⣾⣿⣿⣿⡄⠛⠋⠘⣿⣿⡿⠀⠀⣐⣲⣤⣯⠞⠉⠁⠀⠀⠀⠀⠀",
        "  ⢀⠔⠁⣿⣿⣿⣿⣿⡟⠀⠀⠀⢀⣄⣀⡞⠉⠉⠉⠉⠁⠀⠀⠀⠀⠀",
        " ⠀⡜⠀⠀⠻⣿⣿⠿⣻⣥⣀⡀⢠⡟⠉⠉⠀⠀⠀⠀⠀",
        " ⢰⠁⠀⡤⠖⠺⢶⡾⠃⠀⠈⠙⠋⠀⠀⠀⠀⠀",
        " ⠈⠓⠾⠇⠀⠀⠀⠀"
    ]
    for step in loading_steps:
        print(step)
        time.sleep(1)

    # pizza ready message
    print("\nding!")
    time.sleep(1)
    print("Your pizza(s) is ready, enjoy")

    # Time wait
    time.sleep(2)