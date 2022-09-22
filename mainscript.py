import names as n # Pip install names
import random as r

# Creates a new class to base the file object off of
class csvfile():
    def __init__(self, filename):
        "Creates file on object."
        self.filename = filename
        with open(self.filename, "w") as file:
            file.write("TicketID, FirstName, LastName, PhoneNumber, prefText\n")
    def writeline(self, newline):
        "Writes a new line within the file."
        with open(self.filename, "a") as file:
            file.write(f"{newline}\n")

# Main function which will execute at the start of the application
def main():
    # Name and create a new file
    newfile = str(input("Please insert a name for a new file: "))
    mainfile = csvfile(f"{newfile}.txt")
    # Creates an index
    try:
        starting_number = input("Insert a number which you want to start the ID's: ")
        primary_index = int(starting_number)
    except:
        print("Try a whole number next time.")
    # Sets how many names application will create.
    try:
        how_many = input("How many unique names do you want? ")
        how_many = int(how_many)
    except:
        print("Try a whole number next time.")
    # Final ranges and loops to create the file.
    for n1 in range(0, how_many):
        line = f"'{fn()}', '{ln()}', '{de()}{da()}{da()}-{da()}{da()}{da()}-{da()}{da()}{da()}{da()}', '{r.randint(-1, 0)}'"
        rand1 = r.randint(1, 9)
        for n2 in range(0, rand1):
            finalline = f"'{primary_index}', {line}"
            mainfile.writeline(finalline)
            primary_index += 1

# Functions to create a first name and last name
def fn():
    "Creates and inserts first name."
    first_name = n.get_first_name()
    return first_name

def ln():
    "Creates and inserts last name."
    last_name = n.get_last_name()
    return last_name

# Functions to create digits
def de():
    "Generates and inserts a random digit between 0 and 1."
    digit = str(r.randint(0, 1))
    return digit

def da():
    "Generates and inserts a random digit between 0 and 9."
    digit = str(r.randint(0, 9))
    return digit

# Definition to only run the main function if it is initialized in the interpreter directly
if __name__ == "__main__":
    main()