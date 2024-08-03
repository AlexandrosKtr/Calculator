import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self):
        self.root = self.create_root()
        self.entry = self.create_entry(self.root)
        self.entry.insert(0, "0")
        self.create_buttons()


    def create_root(self):
        """Create the main application window"""

        root = tk.Tk()
        root.title("Calculator")
        root.geometry("400x600")
        root.resizable(False, False)
        root.configure(bg="black")
        return root
    

    def create_entry(self, root):
        """Create an entry widget for the input"""

        entry = tk.Entry(root, width=17, borderwidth=0, font=("Arial", 30), justify="right", bg="black", fg="white")
        entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)
        return entry
    

    def button_click(self, num):
        """Adds the specified number to the operation"""
        
        curr = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, curr + str(num))


    def button_clear(self):
        """Removes the last inputed number"""

        self.entry.delete(0, tk.END)


    def button_clear_all(self):
        """Clears the display"""

        self.entry.delete(0, tk.END)


    def button_equal(self):
        """Displays the result of the current operation"""

        try:
            result = str(eval(self.entry.get()))
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)
        except Exception as ex:
            messagebox.showerror("Error", "Invalid Input")


    def button_operator(self, operator):
        """Adds the operator"""

        curr = self.entry.get()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, curr + operator)

    
    def button_percentage(self):
        """Displays the current number in a percentage type"""

        try:
            curr = float(self.entry.get())
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, curr / 100)
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")

    
    def button_negative(self):
        """Toggles between negative and positive numbers"""

        curr = self.entry.get()
        if curr:
            if curr[0] == "-":
                self.entry.delete(0, 1)
            else:
                self.entry.insert(0, "-")


    def create_buttons(self):
        """Create the buttons display"""

        # Button styles
        button_font = ("Arial", 18)
        button_bg = "#333333"
        button_fg = "white"
        button_active_bg = "#666666"
        operator_bg = "#ff9500"
        operator_active_bg = "#ffa500"

        # Define button texts and their grid positions
        buttons = [
            ("C", 1, 0, self.button_clear_all, "gray"), ("+/-", 1, 1, self.button_negative, "gray"), ("%", 1, 2, self.button_percentage, "gray"), ("/", 1, 3, self.button_operator, operator_bg),
            ("7", 2, 0, self.button_click, button_bg), ("8", 2, 1, self.button_click, button_bg), ("9", 2, 2, self.button_click, button_bg), ("*", 2, 3, self.button_operator, operator_bg),
            ("4", 3, 0, self.button_click, button_bg), ("5", 3, 1, self.button_click, button_bg), ("6", 3, 2, self.button_click, button_bg), ("-", 3, 3, self.button_operator, operator_bg),
            ("1", 4, 0, self.button_click, button_bg), ("2", 4, 1, self.button_click, button_bg), ("3", 4, 2, self.button_click, button_bg), ("+", 4, 3, self.button_operator, operator_bg),
            ("0", 5, 0, self.button_click, button_bg, 2), (".", 5, 2, self.button_click, button_bg), ("=", 5, 3, self.button_equal, operator_bg),
        ]

        # Create buttons and add them to the grid
        for button in buttons:
            if len(button) == 5:
                text, row, col, command, bg = button
                colspan = 1
            else:
                text, row, col, command, bg, colspan = button

            btn = tk.Button(self.root, text=lambda t = text: t, width=5, height=2, font=button_font, bg=bg, fg=button_fg, activebackground=button_active_bg if bg != operator_bg else operator_active_bg, command=lambda t=text: command(t) if text.isdigit() or text == "." else command)
            btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")
            if colspan == 2:
                btn.grid(columnspan=2)

        # Make the buttons expand when the window is resized
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)



def main():
    calculator = Calculator()
    
    calculator.root.mainloop()


if __name__ == "__main__":
    main()