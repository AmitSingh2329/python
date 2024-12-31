# Read position from user
position = input("Enter a chess position (e.g., e4): ")

# Extract the column and row from the position
column = position[0].lower()
row = int(position[1])

# Validate the input
if column in 'abcdefgh' and 1 <= row <= 8:
    # Use a list to map column letters to numbers
    columns = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    column_number = columns.index(column) + 1  # Get index and add 1

    # Determine color: even sum is black, odd sum is white
    color = 'Black' if (column_number + row) % 2 == 0 else 'White'
    print(f"The color of the square {position} is {color}.")
else:
    print("Invalid position")
