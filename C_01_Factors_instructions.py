# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Details and Instructions", "-")

    print('''
To use this program simply enter an integer between 
1 and 200.  The program will show the factors of your
chosen integer.

it will also tell you if your chosen number...
- is a prime number (ie: it has two factors)
- is a perfect square

To exit the program, please type 'xxx' 
    ''')


want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue")
if want_instructions == "":
    instructions()

print("program continues")
