import tkinter as tk

largeFontStyle = ("Arial", 40, "bold")
smallFontStyle = ("Arial", 16)
lightGray = "#f5f5f5"
labelColor = "#25265e"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator by ShinayLim")

        self.totalExpression = "0"
        self.currentExpression = "0"
        self.displayFrame = self.createDisplayFrame()

        self.totalLabel, self.label = self.createDisplayLabels()

        self.digits = {
            7: (1, 1), 8: (1, 2), 9: (1, 3),
            4: (2, 1), 5: (2, 2), 6: (2, 3),
            1: (3, 1), 2: (3, 2), 3: (3, 3),
            0: (4, 2), '.': (4, 1)
        }

        self.buttonsFrame = self.createButtonsFrame()

    def createDisplayLabels(self):
        totalLabel = tk.Label(self.displayFrame, text=self.totalExpression, 
                              anchor=tk.E, bg=labelColor, padx=24, font=smallFontStyle)
        totalLabel.pack(expand=True, fill="both")

        label = tk.Label(self.displayFrame, text=self.currentExpression, 
                              anchor=tk.E, bg=labelColor, padx=24, font=largeFontStyle)
        label.pack(expand=True, fill="both")
        return totalLabel,label

    def createDisplayFrame(self):
        frame = tk.Frame(self.window, height=221, bg=lightGray)
        frame.pack(expand=True, fill="both")
        return frame
    
    def createButtonsFrame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame
    
    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()