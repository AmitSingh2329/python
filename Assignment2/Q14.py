# Define room prices
room_prices = {
    'Standard': 100,
    'Deluxe': 150,
    'Suite': 250
}

# Get user inputs
room_type = input("Enter room type (Standard, Deluxe, Suite): ").capitalize()
length_of_stay = int(input("Enter length of stay (in nights): "))
season = input("Enter season (Peak, Off, Regular): ").lower()
loyalty_member = input("Are you a loyalty member? (yes/no): ").lower() == 'yes'

# Check if the room type is valid
if room_type not in room_prices:
    print("Invalid room type selected.")
else:
    # Calculate initial cost
    base_cost = room_prices[room_type] * length_of_stay

    # Apply length of stay discounts
    if length_of_stay > 7:
        base_cost *= 0.80  # 20% discount
    elif length_of_stay > 3:
        base_cost *= 0.90  # 10% discount

    # Apply season adjustments
    if season == 'peak':
        base_cost *= 1.20  # 20% increase
    elif season == 'off':
        base_cost *= 0.85  # 15% decrease

    # Apply loyalty member discount
    if loyalty_member:
        base_cost *= 0.95  # 5% discount

    # Output the final cost
    final_cost = round(base_cost, 2)
    print(f"The final cost of your booking is: ${base_cost:.2f}")
