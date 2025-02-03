import tkinter as tk
import re

# TODO Format output and improve UI

def load_words():
    with open('words_alpha.txt') as word_file:
        words = word_file.read().split()

    words = order_words(words)
    return words


def order_words(words):
    word_dict = {}
    for word in words:
        length = len(word)
        if length not in word_dict:
            word_dict[length] = []
        word_dict[length].append(word)
    return word_dict


def create_letter_dict(word):
    letter_counts = {}
    for letter in word:
        if letter not in letter_counts:
            letter_counts[letter] = 0
        letter_counts[letter] += 1
    return letter_counts


def check_anagram(letter_counts, other_word):
    other_letters_counts = create_letter_dict(other_word)

    for letter in letter_counts:
        letter_exists = letter in other_letters_counts
        if not letter_exists:
            return False

        letter_counts_match = letter_counts[letter] == other_letters_counts[letter]
        if not letter_counts_match:
            return False
    return True


class AnagramSolver:
    def __init__(self):
        self.words = load_words()
        self.window = tk.Toplevel()
        self.input_box = tk.Entry(self.window)
        self.results = tk.StringVar()
        self.results_label = tk.Label(self.window)
        self.draw_ui()
        self.window.mainloop()

    def solve(self):
        user_word = self.get_user_word()
        user_letters = create_letter_dict(user_word)

        solved_words = []

        if len(user_word) == 0:
            self.display_result('Enter a word')
            return

        for word_to_check in self.words[len(user_word)]:
            if check_anagram(user_letters, word_to_check):
                solved_words.append(word_to_check)

        self.display_result(str(solved_words)
)

    def display_result(self, result):
        self.results.set(result)

    def get_user_word(self):
        word = self.input_box.get()
        word = re.sub(r'\W+', '', word)
        return word

    def draw_ui(self):
        self.window.title("Anagram Solver")
        self.window.geometry('800x500')
        self.window.resizable(False, False)

        self.input_box.configure(width=40, font=('Arial', 20))
        self.input_box.pack()


        solve_button = tk.Button(self.window, command=self.solve, width=10, height=5, text='Solve!', font=('Terminal', 15))
        solve_button.pack()
        self.results_label.configure(textvariable=self.results)
        self.results_label.pack()
