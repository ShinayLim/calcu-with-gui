import tkinter as tk

DARK_THEME = {
    "bg": "#1E1E1E",
    "fg": "#FFFFFF",
    "button_bg": "#2A2A2A",
    "button_fg": "#FFFFFF",
    "display_bg": "#000000",
    "label_bg": "#1E1E1E",
    "special_button_bg": "#2A2A2A",
}

LIGHT_THEME = {
    "bg": "#FFFFFF",
    "fg": "#000000",
    "button_bg": "#F5F5F5",
    "button_fg": "#000000",
    "display_bg": "#F5F5F5",
    "label_bg": "#F5F5F5",
    "special_button_bg": "#CCEDFF",
}


largeFontStyle = ("Arial", 40, "bold")
smallFontStyle = ("Arial", 16)
digitsFontStyle = ("Arial", 24, "bold")
defaultFontStyle = ("Arial", 20)

offWhite = "#F8FAFF"
white = "#FFFFFF"
lightBlue = "#CCEDFF"
lightGray = "#F5F5F5"
labelColor = "#25265E"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0, 0)
        self.window.title("Calculator by ShinayLim")

        self.theme = LIGHT_THEME
        self.totalExpression = ""
        self.currentExpression = ""
        self.displayFrame = self.createDisplayFrame()

        self.totalLabel, self.label = self.createDisplayLabels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttonsFrame = self.createButtonsFrame()

        self.buttonsFrame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttonsFrame.rowconfigure(x, weight=1)
            self.buttonsFrame.columnconfigure(x, weight=1)
        self.createDigitButtons()
        self.createOperatorButtons()
        self.createSpecialButtons()
        self.bindKeys()

    def bindKeys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event,
                             digit=key: self.addToExpression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event,
                             operator=key: self.appendOperator(operator))

    def createSpecialButtons(self):
        self.createClearButton()
        self.createEqualsButton()
        self.createSquareButton()
        self.createSqrtButton()

    def createDisplayLabels(self):
        totalLabel = tk.Label(self.displayFrame, text=self.totalExpression, anchor=tk.E, bg=lightGray,
                              fg=labelColor, padx=24, font=smallFontStyle)
        totalLabel.pack(expand=True, fill='both')

        label = tk.Label(self.displayFrame, text=self.currentExpression, anchor=tk.E, bg=lightGray,
                         fg=labelColor, padx=24, font=largeFontStyle)
        label.pack(expand=True, fill='both')

        return totalLabel, label

    def createDisplayFrame(self):
        frame = tk.Frame(self.window, height=221, bg=lightGray)
        frame.pack(expand=True, fill="both")
        return frame

    def addToExpression(self, value):
        self.currentExpression += str(value)
        self.updateLabel()

    def createDigitButtons(self):
        for digit, gridValue in self.digits.items():
            button = tk.Button(self.buttonsFrame, text=str(digit), bg=self.theme["button_bg"], fg=self.theme["button_fg"], font=digitsFontStyle,
                           borderwidth=0, command=lambda x=digit: self.addToExpression(x))
            button.grid(row=gridValue[0], column=gridValue[1], sticky=tk.NSEW)


    def appendOperator(self, operator):
        self.currentExpression += operator
        self.totalExpression += self.currentExpression
        self.currentExpression = ""
        self.updateTotalLabel()
        self.updateLabel()

    def createOperatorButtons(self):
        i = 0
        for operator, symbol in self.operations.items():
            button = tk.Button(self.buttonsFrame, text=symbol, bg=offWhite, fg=labelColor, font=defaultFontStyle,
                               borderwidth=0, command=lambda x=operator: self.appendOperator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def clear(self):
        self.currentExpression = ""
        self.totalExpression = ""
        self.updateLabel()
        self.updateTotalLabel()

    def createClearButton(self):
        button = tk.Button(self.buttonsFrame, text="C", bg=offWhite, fg=labelColor, font=defaultFontStyle,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def square(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**2"))
        self.updateLabel()

    def createSquareButton(self):
        button = tk.Button(self.buttonsFrame, text="x\u00b2", bg=offWhite, fg=labelColor, font=defaultFontStyle,
                           borderwidth=0, command=self.square)
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.currentExpression = str(eval(f"{self.currentExpression}**0.5"))
        self.updateLabel()

    def createSqrtButton(self):
        button = tk.Button(self.buttonsFrame, text="\u221ax", bg=offWhite, fg=labelColor, font=defaultFontStyle,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def evaluate(self):
        self.totalExpression += self.currentExpression
        self.updateTotalLabel()
        try:
            self.currentExpression = str(eval(self.totalExpression))

            self.totalExpression = ""
        except Exception as e:
            self.currentExpression = "Error"
        finally:
            self.updateLabel()

    def createEqualsButton(self):
        button = tk.Button(self.buttonsFrame, text="=", bg=lightBlue, fg=labelColor, font=defaultFontStyle,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=4, column=3, columnspan=2, sticky=tk.NSEW)

    def createButtonsFrame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def updateTotalLabel(self):
        expression = self.totalExpression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol} ')
        self.totalLabel.config(text=expression)

    def updateLabel(self):
        self.label.config(text=self.currentExpression[:11])

    def toggleTheme(self):
        if self.theme == LIGHT_THEME:
            self.theme = DARK_THEME
        else:
            self.theme = LIGHT_THEME
        self.applyTheme()

    def applyTheme(self):
        self.window.config(bg=self.theme["bg"])

        for widget in self.buttonsFrame.winfo_children():
            if isinstance(widget, tk.Button):
                widget.config(bg=self.theme["button_bg"], fg=self.theme["button_fg"])

        self.displayFrame.config(bg=self.theme["display_bg"])
        self.label.config(bg=self.theme["label_bg"], fg=self.theme["fg"])
        self.totalLabel.config(bg=self.theme["label_bg"], fg=self.theme["fg"])

        # Special buttons (C, x², √, and =) have a different background color
        for widget in self.buttonsFrame.winfo_children():
            if widget["text"] in ["C", "x²", "\u221ax", "="]:
                widget.config(
                    bg=self.theme["special_button_bg"], fg=self.theme["button_fg"])

    def createThemeToggleButton(self):
        themeButton = tk.Button(self.buttonsFrame, text="🌙", font=defaultFontStyle,
                            borderwidth=0, command=self.toggleTheme)
        themeButton.grid(row=0, column=4, sticky=tk.NSEW)

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.applyTheme()  # Apply the default theme (light mode)
    calc.createThemeToggleButton()  # Create the toggle button to switch between modes
    calc.run()
