import random

# Symbols
EMPTY = "⬜"  # White box
HIT = "🌟"
MISS = "❌"

# Create a 3x3 map filled with white boxes
grid = [[EMPTY for _ in range(3)] for _ in range(3)]

# Randomly choose a star position
star_row = random.randint(0, 2)
star_col = random.randint(0, 2)

# Display instructions
print("Welcome to the 3x3 Star Finder Game!")
print("The grid has coordinates from 0 to 2 for both row and column.")
print("You only have 3 chances to find the star! 🌟\n")

# Game loop
found = False
attempts = 0
max_attempts = 3

while not found and attempts < max_attempts:
    # Display the grid
    for row in grid:
        print(" ".join(row))
    
    try:
        # Get player guess
        guess_row = int(input("Enter row (0-2): "))
        guess_col = int(input("Enter column (0-2): "))
        
        # Validate input
        if guess_row not in range(3) or guess_col not in range(3):
            print("⚠️ Invalid coordinates. Please enter numbers from 0 to 2.\n")
            continue
        
        attempts += 1
        
        # Check if the guess is correct
        if guess_row == star_row and guess_col == star_col:
            print("\n🎉 You found the star in", attempts, "attempts!")
            grid[guess_row][guess_col] = HIT
            found = True
        else:
            print(f"❌ No star here. You have {max_attempts - attempts} chances left.\n")
            grid[guess_row][guess_col] = MISS
    
    except ValueError:
        print("⚠️ Please enter a valid number.\n")

# End of game
if not found:
    print("\n💀 Game Over! You ran out of chances.")
    grid[star_row][star_col] = HIT  # Reveal the star

# Final grid reveal
print("\nFinal Map:")
for row in grid:
    print(" ".join(row))
