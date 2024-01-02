from exercise import Exercise
import csv
import time
import prettytable

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
            actions_define()
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
                writer = csv.DictWriter(file, fieldnames = ["name", "weight", "repetitions", "sets"])
                writer.writeheader()
            return True



    def check_input():
        while True:
            try:
                name = input("Enter the name: ").lower().title()
                weight = float(input("Enter your weight(in kg): "))
                repetitions = int(input("Enter the number of repetitions: "))
                sets = int(input("Enter the number of sets: "))
                if name:
                    if weight >= 0 and repetitions >= 1 and sets >= 1:
                        return name, weight, repetitions, sets
                    else:
                        raise ValueError
                else: 
                    raise ValueError
            except ValueError:
                print("Wrong input, try again")
                pass

    exercise_name, exercise_weight, exercise_repetitions, exercise_sets = check_input()
    if create(exercise_name):
        with open("exercises.csv", "a", newline = "") as file:
            writer = csv.DictWriter(file, fieldnames = ["name", "weight", "repetitions", "sets"])
            writer.writerow({"name": exercise_name, "weight": exercise_weight, "repetitions": exercise_repetitions, "sets": exercise_sets})
        return f"The exercise {exercise_name} was created"
    else:
        return f"The exercise with the name {exercise_name} was already created, you can change it by pressing 2"

def change_m(c):
    csv_data = []
    with open("exercises.csv", "r") as file:
        reader = csv.DictReader(file)
        header = reader.fieldnames
        for row in reader:
            if row["name"] != c:
                csv_data.append(row)
            else:
                while True:
                    user_input = input("If you want to delete this exercise press 0, if you want to update it's data press 1: ")
                    match user_input:
                        case "0":
                            print(f"Exercise {c} deleted")
                            break
                        case "1":
                            try:
                                new_weight = float(input("Enter the new weight: "))
                                new_repetitions = int(input("Enter the new repetitions: "))
                                new_sets = int(input("Enter the new sets: "))
                                if new_weight < 0 or new_repetitions < 1 or new_sets < 1:
                                    raise ValueError
                                else:
                                    csv_data.append({'name': c, 'weight': new_weight, 'repetitions': new_repetitions, 'sets': new_sets})
                                    print(f"Exercise {c} updated")
                                    break
                            except ValueError:
                                print("Invalid input")
                                pass
                        case _:
                            pass
    
    with open("exercises.csv", "w", newline ="") as file:
        writer = csv.DictWriter(file, fieldnames = header)
        writer.writeheader()
        writer.writerows(csv_data)
    
    return ""

def change_exercise():
    while True:
        change = input("To change an exercise, enter it's name: ").lower().title()
        try:
            with open("exercises.csv", "r", newline = "") as file:
                reader = csv.DictReader(file)
                for row in reader:
                    if row["name"] == change:
                        print(row["name"])
                        return change_m(change)
                    else:
                        continue
                raise ValueError
        except ValueError:
            print("This exercise doesn't exist")
            pass
        except FileNotFoundError:
            return "You haven't created any exercises yet"

def see_exercises():
    print("\n\n\n")
    headers = ["Name", "Weight", "Repetitions", "Sets"]
    data = []
    try:
        with open("exercises.csv", "r") as file:
            reader = csv.DictReader(file, fieldnames = ["name", "weight", "repetitions", "sets"])
            for row in reader:
                data.append(row)
        
        if data:
            data.pop(0)
            table = prettytable.PrettyTable(headers)
            for row in data:
                table.add_row([row["name"], row["weight"], row["repetitions"], row["sets"]])
            print(table)

        else:
            print("You have no exercises defined yet")

    except FileNotFoundError:
        print("You have no exercises defined yet")

    _ = input("\n\nIf you want to go on press enter ")

def actions_define():
    print("Actions:\n1: Add an exercise\n2: Change an existing Exercise\n3: Give out your exercises\n0: Stops the program")

def csv_to_class():
    try:
        with open("exercise.csv", "r") as file:
            reader = csv.DictReader(file)
            for row in reader:
                row["name"] = Exercise(row["name"], row["weight"], row["repetitions"], row["sets"])
    except FileNotFoundError:
        pass

def main():
    while True:
        try:
            user_in = int(input("Action: "))
            if not choose_action(user_in):
                break
            else:
                time.sleep(0.5)
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