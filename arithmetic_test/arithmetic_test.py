import random

LEVEL_DESCRIPTIONS = {
    1: "simple operations with numbers 2-9",
    2: "integral squares of 11-29"
}

def get_level():
    while True:
        print("Which level do you want? Enter a number:")
        print("1 - simple operations with numbers 2-9")
        print("2 - integral squares of 11-29")
        choice = input("> ")
        if choice in ["1", "2"]:
            return int(choice)
        else:
            print("Incorrect format.")

def get_user_answer():
    while True:
        user_input = input("> ")
        try:
            return int(user_input)
        except ValueError:
            print("Incorrect format.")

def level_one_task():
    num1 = random.randint(2, 9)
    num2 = random.randint(2, 9)
    operator = random.choice(['+', '-', '*'])
    print(f"{num1} {operator} {num2}")
    if operator == '+':
        return num1 + num2
    elif operator == '-':
        return num1 - num2
    else:
        return num1 * num2

def level_two_task():
    num = random.randint(11, 29)
    print(num)
    return num ** 2

def ask_save_results(score, level):
    print("Would you like to save your result to the file? Enter yes or no.")
    answer = input("> ").strip().lower()
    if answer in ["yes", "y"]:
        print("What is your name?")
        name = input("> ")
        result_line = f"{name}: {score}/5 in level {level} ({LEVEL_DESCRIPTIONS[level]}).\n"
        with open("results.txt", "a") as file:
            file.write(result_line)
        print('The results are saved in "results.txt".')

def main():
    level = get_level()
    correct_answers = 0

    for _ in range(5):
        if level == 1:
            correct = level_one_task()
        else:
            correct = level_two_task()

        user_answer = get_user_answer()
        if user_answer == correct:
            print("Right!")
            correct_answers += 1
        else:
            print("Wrong!")

    print(f"Your mark is {correct_answers}/5.")
    ask_save_results(correct_answers, level)

if __name__ == "__main__":
    main()
