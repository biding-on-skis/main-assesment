def drink_size_checker(drink_size):
    if drink_size == "can":
        return 3.3
    else:
        return 5

# Test for drink_selector
if __name__ == "__main__":
    print("Testing drink_selector function")
    drink_id = int(input("Enter drink ID (1-6): "))
    drink_name, drink_cost = drink_size_checker(drink_id)
    print(f"The drink selected is: {drink_name} with a cost of ${drink_cost:.2f}")