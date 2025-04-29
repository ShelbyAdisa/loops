def print_table(number, range_end=10):
    """Print multiplication table for a given number"""
    print(f"\nMultiplication Table for {number}:")
    print("-" * 25)
    
    for i in range(1, range_end + 1):
        print(f"{number} × {i} = {number * i}")


# Simple program to print multiplication table
print("Multiplication Tables Generator")
print("==============================")

# Get user input
number = int(input("number for multiplication table: "))
range_end = int(input("how many multiplications you want(default 10): ") or 10)

# Print the table
print_table(number, range_end)

print("\n")