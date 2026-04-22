# Ask user for width and loop until they
# enter a number that is more than zero
def num_check(question):

    error = "Please enter a number that is more than zero\n"
    while True:

        try:
            # ask the user for a number
            response = float(input(question))

            # check that the number is more than zero
            if response > 0:
                return response
            else:
                print(error)
        except ValueError:
            print(error)


# Main route starts here...

keep_going = ""
while keep_going == "":
    # Get width and length
    width = num_check("Width: ")
    length = num_check("Length: ")
    cost = num_check("Cost: ")


    # Calculate perimeter and price for fence
    perimeter = 2 * (width + length)
    price = perimeter * cost

    # Output the area / perimeter
    print()
    print(f"Perimeter: {perimeter} meters ")
    print(f"Price: ${price:.2f}")

    # Ask user if they want to keep going
    keep_going = input("Press enter to keep going or any key to quit. ")
    print()

    print("I shall graciously and kindly thank you for using this super awesome and wonderful area / perimeter calculator!")
    print()