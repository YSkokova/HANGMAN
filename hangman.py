import random


def choose_word():
    words = ["python", "java", "swift", "javascript"]
    return random.choice(words)


def display_word(word, uncovered_letters):
    display = ""
    for letter in word:
        if letter in uncovered_letters:
            display += letter
        else:
            display += "-"
    return display


def play_game():
    word_to_guess = choose_word()
    attempts = 8
    uncovered_letters = set()
    guessed_letters = set()

    # print("H A N G M A N\n")

    while attempts > 0:
        # print("\nAttempts left:", attempts)
        current_display = display_word(word_to_guess, uncovered_letters)
        print(current_display)
        guess = input("Input a letter: ")

        if not guess.isalpha() or not guess.islower():
            if len(guess) != 1:
                print("Please, input a single letter.")
                continue
            print("Please, enter a lowercase letter from the English alphabet.")
            continue

        if guess in guessed_letters:
            print("You've already guessed this letter.")
            continue

        if len(guess) != 1:
            print("Please, input a single letter.")
            continue

        if guess in uncovered_letters:
            print("You've already guessed this letter.")

        elif guess in word_to_guess:
            # print("Good guess!")
            uncovered_letters.add(guess)

        else:
            print("That letter doesn't appear in the word.")
            attempts -= 1

        guessed_letters.add(guess)

        current_display = display_word(word_to_guess, uncovered_letters)

        if word_to_guess == current_display:
            print(f"You guessed the word {word_to_guess}!")
            print("You survived!")
            return True

    if attempts == 0:
        print("You lost!")


def main():
    wins = 0
    losses = 0

    while True:
        print("H A N G M A N")
        choice = input(
            'Type "play" to play the game, "results" to show the scoreboard, and "exit" to quit: ').lower()

        if choice == "play":
            if play_game():
                wins += 1
            else:
                losses += 1
        if choice == "results":
            print("\nGame Statistics:")
            print(f"You won: {wins} times.")
            print(f"You lost: {losses} times.")
        if choice == "exit":
            # print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Please enter 'play', 'results', or 'exit'.")


if __name__ == "__main__":
    main()
