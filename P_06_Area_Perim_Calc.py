# Ask the user for the width and height
# assume they putin valid data
width = float(input("Width: "))
height = float(input("Height: "))

# calculate the area / perimeter
area = width * height
perimeter = 2 * (width + height)

# Output the area and perimeter
print()
print(f"Perimeter: {perimeter} units")
print(f"area: {area} square units")