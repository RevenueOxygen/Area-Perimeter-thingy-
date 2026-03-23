# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Brotato chip please enter a number that is more than zero\n"
    while True:

        try:
            response = float(input(question))

            if response > 0:
                return response
            else:
                print(error)

        except ValueError:
            print(error)

#Main

keep_going = ""
while keep_going == "":

    # Get width and height
    width = num_check("Width: ")
    height = num_check("Height: ")

    # Calculate area / perimeter
    area = width * height
    perimeter = 2 * (width + height)

    # Display count
    print()
    print(f"Perimeter: {perimeter} units")
    print(f"area: {area} square units")

    # Ask user  if they want to keep going
    keep_going = input("Press Enter to continue or press any other key to quit.")
    print()

print("thank you for using this area & perimeter calculator!!")


