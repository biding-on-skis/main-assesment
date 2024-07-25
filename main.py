# function to check pizza type
def num_checker(question: object, low: object, high: object) -> object:
    while True:

        error = f"enter a valid option between {low} and {high}"

        try:

            user_response = int(input(question))

            # check if user response is a valid number between the low and high numbers
            if low <= user_response <= high:
                return user_response

            else:
                print(error)

        except ValueError:
            print(error)


# function to check for yes or no input
def string_checker(question, valid_ans):
    while True:

        error = f"enter a valid option from {valid_ans}"

        user_response = input(question).lower()

        for item in valid_ans:
            # check if user response is a valid answer
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()

# function to check for yes or no input
def size_checker(question, low, high, item=None):
    while True:

        error = f"enter a valid option from {low} and {high}"

        user_response = input(question).lower()

        if low <= user_response <= high:
            # check if user response is a valid answer
            if item == user_response:
                return item

            elif user_response == item[0]:
                return item

        print(error)
        print()

# function to check string is not empty
def not_blank(question):
    error = "Enter a name"
    while True:

        user_name = input(question)

        if user_name != '':
            return user_name
        else:
            print(error)
            
# function to check string is not empty
def numb_checker(question, valid_ans):
    while True:

        error = f"Enter a phone number {valid_ans}"

        user_name = int(input(question))

        if user_name != '':
            return user_name
        else:
            print(error)



# variables
yes_no = ["yes", "no"]
deliv_option = ["delivery", "pick up"]
pizza_num = "Please provide an id"
size_option = ["large", "medium", "small"]
phone_num = [f""]


# Welcome message
print("<---Welcome to Puppet Pizzaria--->")
print()
delivery = string_checker("Is this order to pick or delivery? ", deliv_option)

if delivery == "delivery":
    print("There is a $6 surcharge for delivery")

# Ask for name and details
name = not_blank("Enter your name: ")

print(f"Hello {name} ")

# Ask for phone number
phone_num = num_checker("Enter the pizza number: ", 1, 99999999999)

# Do you want the Menu?

print()
want_menu = string_checker("Would you like the menu? ", yes_no)

if want_menu == "yes":
    print('''\n
|------------MENU------------|  

----------------------------------------|                        
Gourmet:                         Num id |
Lamb Kebab                          1   |
Crispy BBQ Pork Belly               2   | 
Chicken Bacon & Aoli                3   |
Smokehouse Meat lover               4   |
Peri-Peri Chicken                   5   |
The Lot                             6   |
----------------------------------------|                                    
Traditional:                            |
Philly Cheese steak                 7   |
Supreme                             8   |
Double Bacon Cheeseburger           9   |
Butter Chicken                      10  |
BBQ Meat lovers                     11  |
Chicken Supreme                     12  |
----------------------------------------|
Value:                                  |
Cheesy Garlic Pizza                 13  |
Pepperoni                           14  |
Ham Cheese                          15  |
Simply Cheese                       16  |
Hawaiian                            17  |
Mega Pepperoni                      18  |
----------------------------------------|
Small | Medium | Large |
 $9   |   $12  |  $16  |
------|--------|-------|
''')

# pizza id question
pizza_num_id = num_checker("Enter the pizza number: ", 1, 18)

# Ask for size
size = size_checker("What Size | Small | Medium | Large |: ", size_option)

if size == "large":
    print(f"You chose a large {pizza_num_id}")

elif size == "medium":
    print(f"You chose a Medium {pizza_num_id}")

else:
    print(f"you chose a Small {pizza_num_id}")










