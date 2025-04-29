# right angled triangle pattern using stars


height = int(input("height of the triangle: "))

# Outer loop per row
for i in range(1, height + 1):
    # Inner loop to print stars
    for j in range(i):
        print("*", end="")
    # Move to the next line after each row
    print()