
#Selection function
def main():
    run = True
    while run:
        print("Press 1 to convert binary into numerical")
        print("Press 2 to convert numerical into binary")
        print("press 3 to quit")
        selection = input("Input your selection: ")
        selection = int(selection)
        try:
            if selection == 1:
                BTON() 
            elif selection == 2:
                NTOB()  
            elif selection == 3:
                print("Exiting the program.")
                run = False
            else: 
                print("Invalid selection. Please choose 1, 2, or 3.")
        except ValueError:
            print("Invalid input. Please enter a valid integer (0, 1 or 3).")


#Number to Binary Conversion Function
"""
num / by 2 = num with remainder 1 or 0
num / 2 = num with remainder 1 or 0
Repeats untill num is 0
Bianary num is reveresed list of remainder 
"""
def NTOB():
    while True:
        try:
            number = int(input("Enter your number: "))
            if number == 0:
                print("Binary: 0")
                continue

            binary = ""
            num = number
            while num > 0:
                remainder = num % 2 
                binary = str(remainder) + binary  #Append in reverse order
                num //= 2 

            print(f"Binary: {binary}")
            break

        except ValueError:
            print("Invalid input. Please enter a valid integer.")


#Binary to Number Conversion Function
"""
Multipkly by power of 2 for its x postion of the biuanary number
1101
postion 3 bit 1 = 1 * 2^3 = 8
postion 2 bit 1 = 1 * 2^2 = 4
postion 1 bit 0 = 0 * 2^1 = 0
postion 0 bit 1 = 1 * 2^0 = 1
Total = 8 + 4 + 0 + 1 = 13
"""
def BTON():
  while True:
    bianary = input("Enter your binary number: ")
    for digit in bianary:
        if digit not in "01":
            print("Invalid input. Please enter a valid binary number.")
            continue
    length = len(bianary)
    total = 0
    for i in range(length):
        if bianary[i] == '1':
            power = length - i - 1
            total += 2 ** power 
    print(f"Number: {total}")
    break

if __name__ == "__main__":
    main()

