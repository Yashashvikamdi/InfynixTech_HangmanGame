import random

def choose_word():
    words_with_hints = {
        "python": "A popular programming language 🐍",
        "apple": "A fruit and a tech company 🍎",
        "chair": "You sit on it 🪑",
        "tiger": "A big wild cat 🐅",
        "plant": "Needs water and sunlight 🌱"
    }
    return random.choice(list(words_with_hints.items()))

def display_progress(word, guessed_letters):
    return " ".join([letter if letter in guessed_letters else "_" for letter in word])

def play_game():
    word, hint = choose_word()
    guessed_letters = []
    wrong_guesses = 0
    max_wrong = 6
    hint_used = False

    print("\n🎮 Welcome to Hangman Game!")
    print("Type 'hint' to get a clue (costs 1 chance!)")

    while wrong_guesses < max_wrong:
        print("\nWord:", display_progress(word, guessed_letters))
        print("Wrong guesses left:", max_wrong - wrong_guesses)
        print("Guessed letters:", guessed_letters)

        if all(letter in guessed_letters for letter in word):
            print("\n🎉 You won! The word was:", word)
            return

        guess = input("Enter a letter (or 'hint'): ").lower()

        if guess == "hint":
            if not hint_used:
                print("💡 Hint:", hint)
                hint_used = True
                wrong_guesses += 1
            else:
                print("⚠️ Hint already used!")
            continue

        if len(guess) != 1 or not guess.isalpha():
            print("⚠️ Enter a valid single letter.")
            continue

        if guess in guessed_letters:
            print("⚠️ Already guessed!")
            continue

        guessed_letters.append(guess)

        if guess in word:
            print("✅ Correct!")
        else:
            print("❌ Wrong!")
            wrong_guesses += 1

    print("\n💀 Game Over! The word was:", word)

if __name__ == "__main__":
    play_game()
