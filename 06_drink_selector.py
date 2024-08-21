def drink_selector(drink):
    drink_names = {
        1: "Coke", 2: "Fanta", 3: "Lift", 4: "Sprite",
        5: "Coke Zero", 6: "L & P"
    }
    drink_cost = 9.99  # Default cost if drink ID is not found
    return drink_names.get(drink, "Coke"), drink_cost

# Test for drink_selector
if __name__ == "__main__":
    print("Testing drink_selector function")
    drink_id = int(input("Enter drink ID (1-6): "))
    drink_name, drink_cost = drink_selector(drink_id)
    print(f"The drink selected is: {drink_name} with a cost of ${drink_cost:.2f}")