class ItemToPurchase:
    def __init__(self, name="none", price=0.0, quantity=0, description="none"):
        self.name = name
        self.price = price
        self.quantity = quantity
        self.description = description

    def print_item_cost(self):
        total = self.price * self.quantity
        print(f"{self.name} {self.quantity} @ ${self.price:.2f} = ${total:.2f}")

    def print_item_description(self):
        print(f"{self.name}: {self.description}")


class ShoppingCart:
    def __init__(self, customer_name="none", current_date="January 1, 2020"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item):
        self.cart_items.append(item)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.name.lower() == item_name.lower():
                self.cart_items.remove(item)
                found = True
                print(f"Removed: {item.name}")
                break
        if not found:
            print("Item not found in cart. Item not removed.")

    def modify_item(self, item_to_modify):
        found = False
        for item in self.cart_items:
            if item.name.lower() == item_to_modify.name.lower():
                found = True
                if item_to_modify.quantity != 0:
                    item.quantity = item_to_modify.quantity
                    print(f"Updated quantity for {item.name} to {item.quantity}")
                    break
        if not found:
            print("No items are in your cart. No modification(s).")

    def get_num_items_in_cart(self):
        return sum(item.quantity for item in self.cart_items)

    def get_cost_of_cart(self):
        return sum(item.price * item.quantity for item in self.cart_items)

    def print_total(self):
        print(f"\n{self.customer_name}'s Purchases - {self.current_date}")
        print(f"Number of Items: {self.get_num_items_in_cart()}")
        if not self.cart_items:
            print("NO ITEMS IN CART")
        else:
            for item in self.cart_items:
                item.print_item_cost()
            print(f"Total: ${self.get_cost_of_cart():.2f}")

    def print_descriptions(self):
        print(f"\n{self.customer_name}'s Purchases - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            item.print_item_description()


def print_menu(cart):
    while True:
        print("\nMENU")
        print("a - Add item to cart")
        print("r - Remove item from cart")
        print("c - Change item quantity")
        print("i - Output items' descriptions")
        print("o - Output shopping cart")
        print("q - Quit")
        option = input("Choose an option:\n").lower()

        if option == "a":
            print("\nADD ITEM TO CART")
            name = input("Enter the item name:\n")
            description = input("Enter the item description:\n")
            price = float(input("Enter the item price:\n"))
            quantity = int(input("Enter the item quantity:\n"))
            cart.add_item(ItemToPurchase(name, price, quantity, description))

        elif option == "r":
            print("\nREMOVE ITEM FROM CART")
            name = input("Enter name of item to remove:\n")
            cart.remove_item(name)

        elif option == "c":
            print("\nCHANGE ITEM QUANTITY")
            name = input("Enter the item name:\n")
            quantity = int(input("Enter the new quantity:\n"))
            cart.modify_item(ItemToPurchase(name=name, quantity=quantity))

        elif option == "i":
            cart.print_descriptions()

        elif option == "o":
            cart.print_total()

        elif option == "q":
            print("Exiting Menu. Goodbye!")
            break

        else:
            print("Invalid entry, try again.")


def main():
    customer_name = input("Enter customer's name:\n")
    current_date = input("Enter today's date:\n")
    print(f"\nCustomer name: {customer_name}")
    print(f"Today's date: {current_date}\n")

    cart = ShoppingCart(customer_name, current_date)

    # Step 2: Prompt user for two items BEFORE menu
    print("Item 1")
    name1 = input("Enter the item name:\n")
    description1 = input("Enter the item description:\n")   
    price1 = float(input("Enter the item price:\n"))
    quantity1 = int(input("Enter the item quantity:\n"))
    item1 = ItemToPurchase(name1, price1, quantity1)
    cart.add_item(item1)

    print("\nItem 2")
    name2 = input("Enter the item name:\n")
    description2 = input("Enter the item description:\n")   
    price2 = float(input("Enter the item price:\n"))
    quantity2 = int(input("Enter the item quantity:\n"))
    item2 = ItemToPurchase(name2, price2, quantity2)
    cart.add_item(item2)

    # Now launch the menu
    print_menu(cart)


if __name__ == "__main__":
    main()
