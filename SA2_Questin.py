print("Available Menu!")
print("1. Sandwich - P35")
print("2. Burger - P50")
print("3. Pasta - P30")
print("4. Fried Chicken - P50")

choice = int(input("Select Food Item: "))

if choice == 1:
    item_name = "Sandwich"
    price = 35.00
elif choice == 2:
    item_name = "Burger"
    price = 50.00
elif choice == 3:
    item_name = "Pasta"
    price = 30.00
elif choice == 4:
    item_name = "Fried Chicken"
    price = 50.00
else:
    print("That isnt on the Menu")
    
quantity = int(input(f"Enter Quantity for {item_name}: "))

total_cost = price * quantity

discount = 0.0

subtotal = price * quantity
    
if subtotal >= 200:
    discount = subtotal * 0.10
    final_total = subtotal - discount
    has_discount = True
else:
    discount = 0.0
    final_total = subtotal
    has_discount = False

print("\n" + "="*20 + " ORDER SUMMARY " + "="*20)
print(f"Item: {item_name}")
print(f"Price: P{price:.2f}")
print(f"Quantity: {quantity}")
print(f"Subtotal: P{subtotal:.2f}")
    
if has_discount:
    print(f"Discount: -P{discount:.2f}")
    print(f"Final Total: P{final_total:.2f}")
else:
    print(f"Final Total: P{final_total:.2f}")