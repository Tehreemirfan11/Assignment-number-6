def calculate_ticket_price(age, day, is_family=False, group_size=1):
    base_price = 200
    if age <= 12:  
        base_price *= 0.8
    elif age >= 65:
        base_price *= 0.9
    if day.lower() in ['saturday', 'sunday']:
        base_price *= 1.2 
    if is_family and group_size >= 3:
        base_price *= 0.9

    return base_price * group_size
age = int(input("Enter age: "))
day = input("Enter day of the week: ")
is_family = input("Is this a family/group booking? (yes/no): ").lower() == 'yes'

if is_family:
    group_size = int(input("Enter the group size: "))
    price = calculate_ticket_price(age, day, is_family=True, group_size=group_size)
else:
    price = calculate_ticket_price(age, day)

print(f'The ticket price is: {price:.2f} rupees')