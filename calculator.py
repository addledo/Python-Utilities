import tkinter as tk
from tkinter import Label, Frame, Button

class Calculator:
    button_font = ('arial', 15)
    button_height = 4
    button_width = 4
    display_width = 29
    display_height = 4
    display_font = ('arial', 18)

    def __init__(self):
        self.buffer = ""
        self.display_text = tk.StringVar()
        window = self.draw_calc()
        window.mainloop()

    def button_press(self, num):
        self.buffer += str(num)
        self.display_text.set(self.buffer)

    def equals(self):
        try:
            result = str(eval(self.buffer))
            self.buffer = result
            self.display_text.set(self.buffer)

        except SyntaxError:
            self.display_text.set("SYNTAX ERR")
            self.buffer= ""

        except ZeroDivisionError:
            self.display_text.set("DIV 0 ERR")
            self.buffer= ""

    def clear(self):
        self.buffer = ""
        self.display_text.set(self.buffer)

    def backspace(self):
        self.buffer = self.buffer[:-1]
        self.display_text.set(self.buffer)


    def draw_calc(self):
        window = tk.Toplevel()
        window.title("Calculator")
        window.geometry('400x600')
        window.resizable(False, False)

        calc_display = Label(window, width=self.display_width, height=self.display_height, bg="white",
            textvariable=self.display_text, font=self.display_font)
        calc_display.pack()

        frame = Frame(window)
        frame.pack()


        ## NUMBERS
        button1 = Button(frame, text="1", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(1))
        button2 = Button(frame, text="2", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(2))
        button3 = Button(frame, text="3", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(3))
        button4 = Button(frame, text="4", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(4))
        button5 = Button(frame, text="5", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(5))
        button6 = Button(frame, text="6", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(6))
        button7 = Button(frame, text="7", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(7))
        button8 = Button(frame, text="8", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(8))
        button9 = Button(frame, text="9", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(9))
        button0 = Button(frame, text="0", height=self.button_height, width=self.button_width, font=self.button_font,
                         command=lambda: self.button_press(0))


        ## OPERATIONS
        button_plus = Button(frame, text="+", height=self.button_height, width=self.button_width, font=self.button_font,
                             command=lambda: self.button_press("+"))
        button_minus = Button(frame, text="-", height=self.button_height, width=self.button_width, font=self.button_font,
                              command=lambda: self.button_press("-"))
        button_times = Button(frame, text="*", height=self.button_height, width=self.button_width, font=self.button_font,
                              command=lambda: self.button_press("*"))
        button_divide = Button(frame, text="/", height=self.button_height, width=self.button_width, font=self.button_font,
                               command=lambda: self.button_press("/"))
        button_dp = Button(frame, text=".", height=self.button_height, width=self.button_width, font=self.button_font,
                           command=lambda: self.button_press("."))
        button_clear = Button(frame, text="C", height=self.button_height, width=self.button_width, font=self.button_font,
                              command=self.clear)
        button_ce = Button(frame, text="CE", height=self.button_height, width=self.button_width, font=self.button_font,
                           command=self.backspace)
        button_equals = Button(frame, text="=", height=self.button_height, width=self.button_width, font=self.button_font,
                               command=self.equals)

        ## DRAW NUMBER BUTTONS
        button1.grid(row=0, column=0)
        button2.grid(row=0, column=1)
        button3.grid(row=0, column=2)
        button4.grid(row=1, column=0)
        button5.grid(row=1, column=1)
        button6.grid(row=1, column=2)
        button7.grid(row=2, column=0)
        button8.grid(row=2, column=1)
        button9.grid(row=2, column=2)
        button0.grid(row=3, column=1)

        ## DRAW OPERATION BUTTONS
        button_plus.grid(row=0, column=3, padx=(20,0))
        button_minus.grid(row=0, column=4)
        button_times.grid(row=1, column=3, padx=(20,0))
        button_divide.grid(row=1, column=4)
        button_clear.grid(row=2, column=3, padx=(20,0))
        button_ce.grid(row=2, column=4)
        button_dp.grid(row=3, column=2)
        button_equals.grid(row=3, column=3, padx=(20,0))

        return window