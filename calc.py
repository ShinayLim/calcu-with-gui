import tkinter as tk

lightGray = "#f5f5f5"

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("375x667")
        self.window.resizable(0,0)
        self.window.title("Calculator by ShinayLim")

        self.displayFrame = self.createDisplayFrame()
        self.buttonsFrame = self.createButtonsFrame()

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