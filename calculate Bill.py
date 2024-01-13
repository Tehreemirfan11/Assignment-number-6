def calculate_total_bill(items, quantities, prices, discount_percent=0, tax_percent=0, split_with_friends=1):
    if len(items) != len(quantities) or len(items) != len(prices):
        return "Error: Number of items, quantities, and prices must be equal."

    total_cost = sum(quantity * price for quantity, price in zip(quantities, prices))
    discount_amount = total_cost * (discount_percent / 100)
    total_cost -= discount_amount
    tax_amount = total_cost * (tax_percent / 100)
    total_cost += tax_amount
    if split_with_friends > 1:
        total_cost /= split_with_friends

    return total_cost
items = ["Item1", "Item2", "Item3"]
quantities = [2, 1, 3]
prices = [90.99, 60.99, 100.5]

discount_percent = float(input("Enter discount percentage (0 for no discount): "))
tax_percent = float(input("Enter tax percentage (0 for no tax): "))
split_with_friends = int(input("Enter the number of friends to split the bill with (1 for no split): "))

total_bill = calculate_total_bill(items, quantities, prices, discount_percent, tax_percent, split_with_friends)
print(f'The total bill amount is: {total_bill:.2f}')