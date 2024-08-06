import tkinter as tk
from tkinter import messagebox


class Calculator:
    def __init__(self):
        self.root = self.create_root()
        self.entry = self.create_entry(self.root)
        self.create_buttons()
        self.operator = ""

        # NEW
        self.temp = ""
        #

        # OLD
        # self.num1 = ""
        # self.num2 = ""
        #

        self.new = True
        self.root.mainloop()


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
        entry.insert(0, "0")
        return entry
    

    def button_num(self, num):
        """Adds the specified number to the operation"""

        # If num is the first num after running the app or if after an operation, delete existing entry and insert num.

        # NEW
        if not self.operator:
            if self.new:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(num))
                self.new = False
            else:
                self.entry.insert(tk.END, str(num))
        else:
            if self.new:
                self.temp = self.entry.get()
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(num))
                self.new = False
            else:
                self.entry.insert(tk.END, str(num))
        #

        # OLD
        # if not self.operator:
        #     if self.new:
        #         self.num1 = num
        #         self.new = False
        #     else:
        #         self.num1 = self.num1 + num
        #     self.entry.delete(0, tk.END)
        #     self.entry.insert(tk.END, str(self.num1))
        # else:
        #     if self.new:
        #         self.num2 = num
        #         self.new = False
        #     else:
        #         self.num2 = self.num2 + num
        #     self.entry.delete(0, tk.END)
        #     self.entry.insert(tk.END, str(self.num2))
        #
        
        self.btn_clear.configure(text="C")



    def button_clear(self):
        """Clears the displayed number"""
        
        self.new = True
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, "0")
        self.btn_clear.configure(text="AC")


    def button_clear_all(self):
        """Resets the calculator"""
        self.operator = ""

        # NEW
        self.temp = ""
        #

        # OLD
        # self.num1 = ""
        # self.num2 = ""
        #

        self.toggle()
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, "0")
        self.new = True


    def button_equal(self):
        """Displays the result of the current operation"""

        self.toggle()

        # NEW
        if self.operator:
            curr = self.temp + self.operator + self.entry.get()
            self.temp = self.operator + self.entry.get()
        else:
            curr = self.entry.get() + self.temp
        
        try:
            result = str(eval(curr))
            if float(result) % 1 == 0:
                result = str(int(float(result)))

            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, result)

        except ZeroDivisionError as ex:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            messagebox.showerror("ZeroDivisionError", "Cannot divide by 0")

        except Exception as ex:
            self.entry.delete(0, tk.END)
            self.entry.insert(tk.END, "Error")
            messagebox.showerror("Error", "Invalid Input")
        #

        # OLD
        # self.num1 = self.num1 + self.operator + self.num2
        # try:
        #     result = str(eval(self.num1))
        # except Exception as ex:
        #     messagebox.showerror("Error", "Invalid Input")
        #

        self.operator = ""
        self.new = True
        


    def button_operator(self, operator):
        """Adds the operator"""

        self.toggle(operator)

        if self.operator:
            curr = self.temp + self.operator + self.entry.get()
            self.temp = self.operator + self.entry.get()
        
            try:
                result = str(eval(curr))
                if float(result) % 1 == 0:
                    result = str(int(float(result)))

                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, result)

            except ZeroDivisionError as ex:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                messagebox.showerror("ZeroDivisionError", "Cannot divide by 0")

            except Exception as ex:
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, "Error")
                messagebox.showerror("Error", "Invalid Input")

        self.operator = operator
        
        self.new = True

        # OLD
        # curr = self.entry.get()
        # if curr[-1] in ["+", "-", "*", "/"]:
        #     self.entry.delete(len(curr) - 1)
        #     self.entry.insert(tk.END, operator)
        # else:
        #     self.entry.insert(tk.END, operator)
        #

    
    def button_percentage(self):
        """Displays the current number in a percentage type"""

        # NEW
        try:
            curr = str(float(self.entry.get()) / 100)
        except ValueError:
            messagebox.showerror("Error", "Invalid Input")
        self.entry.delete(0, tk.END)
        self.entry.insert(tk.END, curr)
        #

        # OLD
        # if not self.operator:
        #     try:
        #         self.num1 = str(float(self.num1) /100)
        #     except ValueError:
        #         messagebox.showerror("Error", "Invalid Input")
        #     self.entry.delete(0, tk.END)
        #     self.entry.insert(tk.END, self.num1)
        # else:
        #     try:
        #         self.num2 = str(float(self.num2) / 100)
        #     except ValueError:
        #         messagebox.showerror("Error", "Invalid Input")
        #     self.entry.delete(0, tk.END)
        #     self.entry.insert(tk.END, self.num2)
        #

        
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
        top_button_bg = "gray"
        top_button_fg = "black"  
        top_button_active_bg = "#666666"
        top_button_active_fg = top_button_fg
        operator_bg = "#ff9500"
        operator_fg = "white"
        operator_active_bg = "white"
        operator_active_fg = "#ff9500"

        # Define button texts and their grid positions
        buttons = [
            ("+/-", 1, 1, self.button_negative, top_button_bg), ("%", 1, 2, self.button_percentage, top_button_bg),
            ("7", 2, 0, self.button_num, button_bg), ("8", 2, 1, self.button_num, button_bg), ("9", 2, 2, self.button_num, button_bg),
            ("4", 3, 0, self.button_num, button_bg), ("5", 3, 1, self.button_num, button_bg), ("6", 3, 2, self.button_num, button_bg),
            ("1", 4, 0, self.button_num, button_bg), ("2", 4, 1, self.button_num, button_bg), ("3", 4, 2, self.button_num, button_bg),
            ("0", 5, 0, self.button_num, button_bg, 2), (".", 5, 2, self.button_num, button_bg), ("=", 5, 3, self.button_equal, operator_bg),
        ]

        # Create buttons and add them to the grid
        for button in buttons:
            if len(button) == 5:
                text, row, col, command, bg = button
                colspan = 1
            else:
                text, row, col, command, bg, colspan = button

            btn = tk.Button(
                self.root, 
                text=text, 
                width=5, 
                height=2, 
                font=button_font, 
                bg=bg, 
                fg=top_button_fg if text in ["C", "+/-", "%"] else button_fg, 
                activebackground=button_active_bg, 
                activeforeground=top_button_fg if text in ["C", "+/-", "%"] else button_fg, 
                command=lambda text=text, command=command: command(text) if text.isdigit() or text == "." else command()
                )
            btn.grid(row=row, column=col, columnspan=colspan, padx=5, pady=5, sticky="nsew")

        self.btn_clear = tk.Button(self.root, text="AC", width=5, height=2, font=button_font, bg=top_button_bg, fg=top_button_fg, activebackground=top_button_active_bg, activeforeground=top_button_active_fg, command=lambda: self.button_clear_all() if self.btn_clear["text"] == "AC" else self.button_clear())
        self.btn_clear.grid(row=1, column=0, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.btn_plus = tk.Button(self.root, text="+", width=5, height=2, font=button_font, bg=operator_bg, fg=operator_fg, activebackground=operator_active_bg, activeforeground=operator_active_fg, command=lambda: self.button_operator("+"))
        self.btn_plus.grid(row=4, column=3, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.btn_minus = tk.Button(self.root, text="-", width=5, height=2, font=button_font, bg=operator_bg, fg=operator_fg, activebackground=operator_active_bg, activeforeground=operator_active_fg, command=lambda: self.button_operator("-"))
        self.btn_minus.grid(row=3, column=3, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.btn_multiply = tk.Button(self.root, text="*", width=5, height=2, font=button_font, bg=operator_bg, fg=operator_fg, activebackground=operator_active_bg, activeforeground=operator_active_fg, command=lambda: self.button_operator("*"))
        self.btn_multiply.grid(row=2, column=3, columnspan=1, padx=5, pady=5, sticky="nsew")
        self.btn_subtract = tk.Button(self.root, text="/", width=5, height=2, font=button_font, bg=operator_bg, fg=operator_fg, activebackground=operator_active_bg, activeforeground=operator_active_fg, command=lambda: self.button_operator("/"))
        self.btn_subtract.grid(row=1, column=3, columnspan=1, padx=5, pady=5, sticky="nsew")

        # Make the buttons expand when the window is resized
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)


    def toggle(self, operator=""):
        match operator:
            case "+":
                self.btn_plus.configure(bg="white", fg="#ff9500")
                self.btn_minus.configure(bg="#ff9500", fg="white")
                self.btn_multiply.configure(bg="#ff9500", fg="white")
                self.btn_subtract.configure(bg="#ff9500", fg="white")
            case "-":
                self.btn_plus.configure(bg="#ff9500", fg="white")
                self.btn_minus.configure(bg="white", fg="#ff9500")
                self.btn_multiply.configure(bg="#ff9500", fg="white")
                self.btn_subtract.configure(bg="#ff9500", fg="white")
            case "*":
                self.btn_plus.configure(bg="#ff9500", fg="white")
                self.btn_minus.configure(bg="#ff9500", fg="white")
                self.btn_multiply.configure(bg="white", fg="#ff9500")
                self.btn_subtract.configure(bg="#ff9500", fg="white")
            case "/":
                self.btn_plus.configure(bg="#ff9500", fg="white")
                self.btn_minus.configure(bg="#ff9500", fg="white")
                self.btn_multiply.configure(bg="#ff9500", fg="white")
                self.btn_subtract.configure(bg="white", fg="#ff9500")
            case _:
                self.btn_plus.configure(bg="#ff9500", fg="white")
                self.btn_minus.configure(bg="#ff9500", fg="white")
                self.btn_multiply.configure(bg="#ff9500", fg="white")
                self.btn_subtract.configure(bg="#ff9500", fg="white")



def main():
    calculator = Calculator()


if __name__ == "__main__":
    main()