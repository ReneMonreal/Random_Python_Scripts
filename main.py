import random
import time 

def grade(correct, incorrect):
    total = correct + incorrect
    print(f'You answered {total} questions...')
    percentage = (100/ total) * correct
    return percentage
    

def main():
    print("***********************************************************************")
    print("Welcome to Minute Math!")
    print("Goal: Answer as many math questions as you can before time runs out!")
    print("You can assume all nums are generated between 0 and 100.")

    t = 60 #Max seconds, "Minute Math thus set at 60"
    startTime = time.time()
    correct = 0
    incorect = 0

    print(f"You have {t} seconds to answer as many questions as you can!\n")
    print("GOOOO!!!!")
    while ((time.time() - startTime) <= t):
        result = 0
        answer = 0
        maxNum = 100
        minNum = 0
        print("Time Remaining: ", int((startTime - time.time()) + t) ," seconds...")
        #Generate nums, division num2 rules differ
        operator = random.choice(['+', '-', '*', '/'])
        if operator == '+' or operator == '*' or operator == '-':
            num1 = random.randint(minNum, maxNum)
            num2 = random.randint(minNum, maxNum)
        elif operator == '/':
            num1 = random.randint(minNum, maxNum)
            num2 = random.randint(num1, maxNum)

        #logic for operators
        if operator == '+':
            result = num1 + num2
        elif operator == '-':
            result = num1 - num2
        elif operator == '*':
            result = num1 * num2
        elif operator == '/':
            if num1 == 0:
                result = 0
            else:
                result = num2 // num1

        #Interaction
        print(f'What is {num1} {operator} {num2} ? ')
        answer = int(input())
        if answer == result:
            print("Correct!")
            correct += 1
        else:
            print("incorrect!")
            incorect += 1
            print(f"Answer was {result}")\
    
    score = grade(correct, incorect)
    print(f"Total Score: {score}%!!!")
    print(" ")
if __name__ == "__main__":
    main()