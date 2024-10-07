#This is the first version i created when i was learning how to code in python, please view "Updated Calculator" for the new method.

#Creating processes that run based on the answer
def add(a, b):
    answer = a + b
    print(str(a) + " + " + str(b) + " = " + str(answer) + "\n")

def sub(a, b):
    answer = a - b
    print(str(a) + " - " + str(b) + " = " + str(answer) + "\n")

def mul(a, b):
    answer = a + b
    print(str(a) + " * " + str(b) + " = " + str(answer) + "\n")

def div(a, b):
    answer = a / b
    print(str(a) + " / " + str(b) + " = " + str(answer) + "\n")
# Anserts that can be selected, more operators can be added but i will needed to create a new function for them
while True:
    print("A. Addition")
    print("B. Subtraction")
    print("C. Multiplication")
    print("D. Division")
    print("E. Exit")
    choice = input("Select what you would like to do: ")
#This is what reads the the inputs.
    if choice == "a" or choice == "A":
        print("Addition")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        add(a, b)
    elif choice == "b" or choice == "B":
        print("Subtraction")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        sub(a, b)
    elif choice == "c" or choice == "C":
        print("Multipliction")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        mul(a, b)
    elif choice == "d" or choice == "D":
        print("Division")
        a = int(input("input first number:"))
        b = int(input("input second number:"))
        div(a, b)
    elif choice == "e" or choice == "E":
        print("program ended")
        quit()
