import tkinter as tk
import random

words = ["apple", "tiger", "chair", "plant", "robot"]

word = random.choice(words)
guessed_letters = []
wrong_guesses = 0
max_attempts = 6
hint_used = False

root = tk.Tk()
root.title("Hangman Game 🎮")

def update_display():
    display_word = ""
    for letter in word:
        if letter in guessed_letters:
            display_word += letter + " "
        else:
            display_word += "_ "
    word_label.config(text=display_word)

def guess_letter():
    global wrong_guesses

    letter = entry.get().lower()
    entry.delete(0, tk.END)

    if not letter or len(letter) != 1 or not letter.isalpha():
        message_label.config(text="Enter valid letter!")
        return

    if letter in guessed_letters:
        message_label.config(text="Already guessed!")
        return

    guessed_letters.append(letter)

    if letter in word:
        message_label.config(text="Correct 🎉")
    else:
        wrong_guesses += 1
        message_label.config(text=f"Wrong ❌ ({wrong_guesses}/6)")

    update_display()
    check_game_status()

def give_hint():
    global hint_used

    if hint_used:
        message_label.config(text="Hint already used!")
        return

    for letter in word:
        if letter not in guessed_letters:
            guessed_letters.append(letter)
            hint_used = True
            message_label.config(text=f"Hint 💡: '{letter}' revealed")
            break

    update_display()

def check_game_status():
    if all(letter in guessed_letters for letter in word):
        message_label.config(text="You Won! 🏆")
        guess_button.config(state="disabled")

    elif wrong_guesses >= max_attempts:
        message_label.config(text=f"You Lost 😢 Word: {word}")
        guess_button.config(state="disabled")

word_label = tk.Label(root, text="_ " * len(word), font=("Arial", 20))
word_label.pack(pady=20)

entry = tk.Entry(root)
entry.pack()

guess_button = tk.Button(root, text="Guess 🎯", command=guess_letter)
guess_button.pack(pady=5)

hint_button = tk.Button(root, text="Hint 💡", command=give_hint)
hint_button.pack(pady=5)

message_label = tk.Label(root, text="")
message_label.pack(pady=10)

update_display()
root.mainloop()
