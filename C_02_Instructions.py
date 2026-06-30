# functions go here wowie
def statement_generator(statement,decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


# displays instructions
def instructions():
    statement_generator("Instructions", "-")

    print('''
    - Excuse me sir!
    - There must be someone you've confused me for,
    - If i could see someone who knew me, or someone in uniform!
    - fumo
    
    
    ''')


# Main Routine Here

# Display Instructions At Once When Requested By The Emperor
want_instructions = input("If you are capable, please interact with the key <Enter> or read the instructions "
                          "Or any other key to continue ")

if want_instructions == "":
    instructions()

print("Program continues")