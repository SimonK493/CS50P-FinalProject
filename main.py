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
        case 0:
            return False
        case _:
            print("This was an invalid action number, try again")


def add_exercise():


    def check_input():
        while True:
            try:
                name = input("Enter the name: ")
                weight = float(input("Enter your weight(in kg): "))
                repetitions = int(input("Enter the number of repetitions: "))
                return name, weight, repetitions
            except ValueError:
                print("Wrong input, try again")
                pass

    exercise_name, exercise_weight, exercise_repetitions = check_input()
    with open("exercises.csv", "a", newline = "") as file:
        writer = csv.DictWriter(file, fieldnames = ["name", "weight", "repetitions"])
        writer.writerow({"name": exercise_name, "weight": exercise_weight, "repetitions": exercise_repetitions})
    return f"The exercise {exercise_name} was created"



def change_exercise():
    see_exercises()
    change = int(input("Which exercise you want to change? "))

def see_exercises():
    ...



def actions_define():
    print("Actions:\n1: Add an exercise\n2: Change an existing Exercise\n3: Give out your exercises\n0: Stops the program")

def main():
    actions_define()
    while True:
        try:
            user_in = int(input("Action: "))
            action = choose_action(user_in)
        except ValueError:
            print("Please enter a valid number")
            pass
        if action:
            print(action)
        else:
            print("Goodbye")
            break



if __name__ == "__main__":
    print("Hello")
    time.sleep(1)
    main()