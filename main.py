import tkinter as tk

from anagram_solver import AnagramSolver
from calculator import Calculator
import anagram_solver as anag

def main():
    root = tk.Tk()
    root.title("Home")
    root.resizable(False, False)
    root.geometry('1024x1024')
    root.attributes('-topmost', 1)

    bg_img = tk.PhotoImage(file='img/Retro-Cityscape.png')
    bg_label = tk.Label(root, image=bg_img)
    bg_label.pack()

    title_label = tk.Label(text='UTILITIES', background='#1B90DB', font=('Terminal', 100), width=11, height=2)
    title_label.place(x=40, y=50)

    button_calc = tk.Button(root, command=lambda: Calculator().start(), text="Calculator", font=('Terminal', 20), width=20, height=5)
    button_calc.place(x=50, y=450)

    button_calc = tk.Button(root, command=lambda: AnagramSolver(), text="Anagram Solver", font=('Terminal', 20), width=20, height=5)
    button_calc.place(x=600, y=450)

    root.mainloop()

if __name__ == "__main__":
    main()