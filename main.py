from exercise import Exercise
import csv
import time

def choose_action(n):
    match n:
        case 1:
            print(add_exercise())
            return True
        case 2:
            print(change_exercise())
            return True
        case 3:
            see_exercises()
            return True
        case 0:
            return False
        case _:
            print("This was an invalid action number, try again")

def add_exercise():

    def create(name):
        try:
            with open("exercises.csv", "r") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["name"] == name:
                        return False
                    else:
                        continue
                return True
        except FileNotFoundError:
            with open("exercises.csv", "a", newline = "") as file:
                writer = csv.DictWriter(file, fieldnames = ["name", "weight", "repetitions"])
                writer.writeheader()
            return True



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
    if create(exercise_name):
        with open("exercises.csv", "a", newline = "") as file:
            writer = csv.DictWriter(file, fieldnames = ["name", "weight", "repetitions"])
            writer.writerow({"name": exercise_name, "weight": exercise_weight, "repetitions": exercise_repetitions})
        return f"The exercise {exercise_name} was created"
    else:
        return f"The exercise with the name {exercise_name} was already created, you can change it by pressing 2"

def change_exercise():
    see_exercises()
    change = int(input("Which exercise you want to change? "))

def see_exercises():
    try:
        with open("exercises.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                print(f"{row['name']}: {row['weight']}kg x {row['repetitions']} repetitions")
    except FileNotFoundError:
        return "You have no exercise defined yet"
    
    user_input = input("if you want to go on press enter")

def actions_define():
    print("Actions:\n1: Add an exercise\n2: Change an existing Exercise\n3: Give out your exercises\n0: Stops the program")

def csv_to_class():
    file_exists = exists("exercise.csv")
    if not file_exists:
        return True
    else:
        with open("exercise.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["name"] = Exercise(row["name"], row["weight"], row["repetitions"])

def choose_action(n):
    match n:
        case 1:
            return add_exercise()
        case 2:
            return change_exercise()
        case 3:
            return see_exercises()
        case _:
            print("This was an invalid Action number, try again")

def add_exercise():
    ...

def change_exercise():
    ...

def see_exercises():
    ...



def actions_define():
    print("Actions:\n1: Add an exercise\n2: Change an existing Exercise\n3: Give out your exercises")


def main():
    while True:
        try:
            user_in = int(input("Action: "))
            if not choose_action(user_in):
                break
            else:
                time.sleep(0.7)
                actions_define()
                pass
        except ValueError:
            print("Please enter a number")
            pass



if __name__ == "__main__":
    print("Hello")
    time.sleep(0.5)
    csv_to_class()
    actions_define()
    main()
    print("Goodbye")