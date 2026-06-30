# asks uses for file type change (integer / image / text / xxx)
def get_filetype():

    while True:
        response = input("File type: ").lower()

        # check for 'i' or the exit code
        if response == "xxx" or response == "i":
            return response

        # check if it's an integer
        elif response in ['integer', 'int']:
            return "integer"

        # check for an image
        elif response in ['image', 'picture', 'img', 'p']:
            return "image"

        # check for text
        elif response in ["text", 'txt', 't']:
            return "text"

        # if the response type is invalid output an error
        else:
            print("Please answer an actually valid file type")


# main routine goes here
while True:
    file_type = get_filetype()

    # if user enters "i" ask if they meant integer or image
    if file_type == 'i':

        want_image = input("Press Enter for integer or any other key for image.")
        if want_image == "":
            file_type = "integer"
        else:
            file_type = "image"

    print(f"You chose {file_type}")

    if file_type == "xxx":
        break