import random


def get_computer_choice(options):
    return random.choice(options)


def determine_winner(user_choice, computer_choice, options):
    if user_choice == computer_choice:
        return "draw"
    else:
        index = options.index(user_choice)
        # Create a list where the first half loses to user_choice and the second half wins
        lose_to_user = options[index + 1:] + options[:index]
        mid = len(lose_to_user) // 2
        if computer_choice in lose_to_user[:mid]:
            return "win"
        else:
            return "lose"


def read_ratings(filename="rating.txt"):
    ratings = {}
    try:
        with open(filename, "r") as file:
            for line in file:
                name, score = line.split()
                ratings[name] = int(score)
    except FileNotFoundError:
        pass
    return ratings


def write_ratings(ratings, filename="rating.txt"):
    with open(filename, "w") as file:
        for name, score in ratings.items():
            file.write(f"{name} {score}\n")


def main():
    ratings = read_ratings()
    user_name = input("Enter your name: ").strip()
    print(f"Hello, {user_name}")

    user_score = ratings.get(user_name, 0)

    options_input = input("Enter game options separated by comma or leave empty for default: ").strip()
    if not options_input:
        options = ["rock", "paper", "scissors"]
    else:
        options = [option.strip() for option in options_input.split(",")]

    print("Okay, let's start")

    while True:
        user_choice = input("Enter your choice: ").strip().lower()

        if user_choice == "!exit":
            print("Bye!")
            ratings[user_name] = user_score
            write_ratings(ratings)
            break
        elif user_choice == "!rating":
            print(f"Your rating: {user_score}")
        elif user_choice in options:
            computer_choice = get_computer_choice(options)
            result = determine_winner(user_choice, computer_choice, options)

            if result == "draw":
                user_score += 50
                print(f"There is a draw ({computer_choice})")
            elif result == "win":
                user_score += 100
                print(f"Well done. The computer chose {computer_choice} and failed")
            else:
                print(f"Sorry, but the computer chose {computer_choice}")
        else:
            print("Invalid input")


if __name__ == "__main__":
    main()