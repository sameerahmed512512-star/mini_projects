#  Restaurant managment system
#  Menu
menu = {
    "pizza": 200,
    "pasta": 100,
    "burger": 99,
    "salad": 80,
    "coffee": 70
}

print(" Welcome to Our Restaurant")

order_total = 0
order_items = []


while True:

    choice = input("\nDo you want to order something? (yes/no): ")

    if choice == "no":
        break

    elif choice == "yes":

     
        print("-- MENU --")
        for item, price in menu.items():
            print(f"{item} : Rs {price}")

        item_name = input("\nEnter item name: ")

        if item_name in menu:
            qty = int(input("Enter quantity: "))
            price = menu[item_name] * qty

            order_total += price
            order_items.append((item_name, qty, price))

            print(f"{item_name} x{qty} added! Current total = Rs {order_total}")
        else:
            print("Item not available!")

    else:
        print("Please type yes or no")

# RECEIPT
print("\n ===== RESTAURANT RECEIPT =====")
print("----------------------------------")

for item, qty, price in order_items:
    print(f"{item:<10} x{qty:<2} = Rs {price}")

print("----------------------------------")
print(f"TOTAL BILL: Rs {order_total}")
print(" Thank you! Visit again")