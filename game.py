import random

COLORS = ["R", "G", "B", "Y", "W", "O"]
TRIES = 10
CODE_LENGTH = 4


def generate_code():
    code = []

    for _ in range(CODE_LENGTH):
        color = random.choice(COLORS)
        code.append(color)
    # print(code)

    return code


def guess_code():
    while True:
        guess = input("Guess: ").upper().split(" ")

        if len(guess) != CODE_LENGTH:
            print(f"You Must Check {CODE_LENGTH} Colors. ")
            continue

        for color in guess:
            if color not in COLORS:
                print(f"Invalid color : {color} . Try Again")
                break
        else:
            break

    return guess


def check_code(guess, real_code):
    color_counts = {}
    correct_pos = 0
    incorrect_pos = 0

    for color in real_code:
        if color not in color_counts:
            color_counts[color] = 1
        else:
            color_counts[color] += 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color == real_color:
            correct_pos += 1
            color_counts[guess_color] -= 1

    for guess_color, real_color in zip(guess, real_code):
        if guess_color in color_counts and color_counts[guess_color] > 1:
            incorrect_pos += 1
            color_counts[guess_color] -= 1

    return correct_pos, incorrect_pos


def game():
    print(f"Welcome to Mastermind Game , You have {TRIES} tries to guess the code")
    print(f"The Valid colors are", *COLORS)

    code = generate_code()

    for attempts in range(1, TRIES + 1):
        guess = guess_code()
        correct_position, incorrect_position = check_code(guess, code)

        if correct_position == CODE_LENGTH:
            print(f"You guessed the Colors in {attempts} tries. Awesome...")
            break

        print(
            f"Correct Position : {correct_position} | Incorrect Position : {incorrect_position}"
        )

    else:
        print(f"You ran out of Tries .. Sorry Restart the Game .. The Color is ", *code)


if __name__ == "__main__":
    game()
