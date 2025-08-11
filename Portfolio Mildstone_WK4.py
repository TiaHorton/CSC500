class ItemToPurchase:
    def __init__(self):
        self.item_name = "none"
        self.item_price = 0.0
        self.item_quantity = 0

    def print_item_cost(self):
        total_cost = self.item_price * self.item_quantity
        print(f"{self.item_name} {self.item_quantity} @ ${int(self.item_price)} = ${int(total_cost)}")


# Step 2: Prompt user for two items
print("Item 1")
item1 = ItemToPurchase()
item1.item_name = input("Product Type (Name):\n")
item1.item_price = float(input("Enter Price:\n"))
item1.item_quantity = int(input("Enter Quantity:\n"))

print("\nItem 2")
item2 = ItemToPurchase()
item2.item_name = input("Product Type (Name)e:\n")
item2.item_price = float(input("Enter Price:\n"))
item2.item_quantity = int(input("Enter Quantity:\n"))

# Step 3: Output total cost
print("\n----TOTAL COST----")
item1.print_item_cost()
item2.print_item_cost()

total = (item1.item_price * item1.item_quantity) + (item2.item_price * item2.item_quantity)
print(f"\nTotal: ${int(total)}")
