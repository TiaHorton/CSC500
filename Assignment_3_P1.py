def calculate_bill(food_charge):
    tip_rate = 0.18
    tax_rate = 0.07

    tip = food_charge * tip_rate
    tax = food_charge * tax_rate 
    total = food_charge + tip + tax 

    return {
        "Food Charge": food_charge,
        "Tip (18%)": tip,
        "Tax (7%)": tax,
        "Total Bill": total 
    }  
#Ask user for the food charge 
# This script calculates the total bill including tip and tax based on the food charge provided by the user. 
try:
    user_input = input("Enter the food charge: $")
    food_charge = float(user_input) 

    if food_charge < 0:
        print("Please enter a valid food charge greater than or equal to 0.")
    else:
        bill = calculate_bill(food_charge)

        print("\n----- Bill Summary -----")

        for item, amount in bill.items():
            print(f"{item}: ${amount:.2f}")
        print("------------------------")

except ValueError:
    print("Invalid Entry. Please enter a valid number.")  