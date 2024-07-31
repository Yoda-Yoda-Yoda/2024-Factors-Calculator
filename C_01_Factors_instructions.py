# Generates headings (eg: ---- Heading ----)
def statement_generator(statement, decoration):
    print(f"\n{decoration * 5} {statement} {decoration * 5}")


def instructions():
    statement_generator("Details and Instructions", "-")

    print('''
Instructions go here
- instruction 1
- instruction 2
- etc
    ''')


want_instructions = input("Press <enter> to read the instructions "
                          "or any key to continue")
if want_instructions == "":
    instructions()

print("program continues")
