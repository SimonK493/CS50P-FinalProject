from exercise import Exercise
import csv
import time

def choose_action(n):
    match n:
        case 1:
            return add_exercise()
        case 2:
            return change_exercise()
        case 3:
            return see_exercises()
        case _:
            print("This was an invalid action number, try again")


def add_exercise():
    exercise_name = input("Enter the name: ")
    exercise_weight = int(input("Enter your weight"))
    exercise_repetitions = int(input("Enter the number of repetitions: "))


def change_exercise():
    see_exercises()
    change = int(input("Which exercise you want to change? "))

def see_exercises():
    ...



def actions_define():
    print("Actions:\n1: Add an exercise\n2: Change an existing Exercise\n3: Give out your exercises")

def main():
    actions_define()
    while True:
        try:
            user_in = int(input("Action: "))
            action = choose_action(user_in)
        except ValueError:
            print("Please enter a valid number")
            pass
        print(action)



if __name__ == "__main__":
    print("Hello")
    time.sleep(1)
    main()