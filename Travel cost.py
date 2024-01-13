def estimate_travel_cost(destination, travel_style, duration):
    transportation_cost = calculate_transportation_cost(destination)
    accommodation_cost = calculate_accommodation_cost(destination, travel_style, duration)
    activities_cost = calculate_activities_cost(destination)

    total_cost = transportation_cost + accommodation_cost + activities_cost

    return total_cost

def calculate_transportation_cost(destination):
    return 100

def calculate_accommodation_cost(destination, travel_style, duration):
    daily_budget_cost = int(input ("Enter daily budget cost: "))
    daily_luxury_cost = int(input ("Enter daily Luxury Cost: "))

    if travel_style == "budget":
        accommodation_cost = daily_budget_cost * duration
    elif travel_style == "luxury":
        accommodation_cost = daily_luxury_cost * duration
    else:
        raise ValueError("Invalid travel style. Choose 'budget' or 'luxury'.")

    return accommodation_cost

def calculate_activities_cost(destination):
    return 50

destination = "Paris"
travel_style = "luxury"
duration = 7

estimated_cost = estimate_travel_cost(destination, travel_style, duration)
print(f"Estimated travel cost for {destination} ({travel_style} style, {duration} days): {estimated_cost}")