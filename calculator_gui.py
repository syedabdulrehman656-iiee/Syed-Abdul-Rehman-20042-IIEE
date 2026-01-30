import tkinter as tk
from tkinter import ttk

class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.root.geometry("400x500")
        self.root.resizable(False, False)
        
        # Variables
        self.current_value = ""
        self.previous_value = ""
        self.operation = None
        
        # Create UI
        self.create_widgets()
    
    def create_widgets(self):
        # Display
        self.display = tk.Entry(
            self.root,
            font=("Arial", 24),
            justify="right",
            bd=10,
            bg="#f0f0f0"
        )
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=20, sticky="ew")
        
        # Button layout
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
            ('C', 5, 0), ('CE', 5, 1), ('←', 5, 2), ('±', 5, 3)
        ]
        
        # Create buttons
        for (text, row, col) in buttons:
            if text == '=':
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 18, "bold"),
                    bg="#4CAF50",
                    fg="white",
                    command=self.calculate
                )
            elif text in ['/', '*', '-', '+']:
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 18, "bold"),
                    bg="#ff9800",
                    fg="white",
                    command=lambda t=text: self.operation_click(t)
                )
            elif text in ['C', 'CE', '←', '±']:
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 18, "bold"),
                    bg="#f44336",
                    fg="white",
                    command=lambda t=text: self.special_operation(t)
                )
            else:
                btn = tk.Button(
                    self.root,
                    text=text,
                    font=("Arial", 18),
                    bg="#e0e0e0",
                    command=lambda t=text: self.number_click(t)
                )
            
            btn.grid(row=row, column=col, padx=5, pady=5, sticky="nsew", ipadx=20, ipady=20)
        
        # Configure grid weights
        for i in range(6):
            self.root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.root.grid_columnconfigure(i, weight=1)
    
    def number_click(self, number):
        """Handle number button clicks"""
        self.current_value += str(number)
        self.display.delete(0, tk.END)
        self.display.insert(0, self.current_value)
    
    def operation_click(self, op):
        """Handle operation button clicks"""
        if self.current_value:
            if self.previous_value and self.operation:
                self.calculate()
            self.previous_value = self.current_value
            self.current_value = ""
            self.operation = op
    
    def calculate(self):
        """Perform the calculation"""
        if self.previous_value and self.current_value and self.operation:
            try:
                num1 = float(self.previous_value)
                num2 = float(self.current_value)
                
                if self.operation == '+':
                    result = num1 + num2
                elif self.operation == '-':
                    result = num1 - num2
                elif self.operation == '*':
                    result = num1 * num2
                elif self.operation == '/':
                    if num2 == 0:
                        result = "Error"
                    else:
                        result = num1 / num2
                
                # Display result
                self.display.delete(0, tk.END)
                if result != "Error":
                    # Remove trailing zeros and decimal point if not needed
                    result_str = str(result)
                    if '.' in result_str:
                        result_str = result_str.rstrip('0').rstrip('.')
                    self.display.insert(0, result_str)
                    self.current_value = result_str
                else:
                    self.display.insert(0, "Error")
                    self.current_value = ""
                
                self.previous_value = ""
                self.operation = None
                
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(0, "Error")
                self.current_value = ""
                self.previous_value = ""
                self.operation = None
    
    def special_operation(self, op):
        """Handle special operations"""
        if op == 'C':
            # Clear all
            self.current_value = ""
            self.previous_value = ""
            self.operation = None
            self.display.delete(0, tk.END)
        elif op == 'CE':
            # Clear entry
            self.current_value = ""
            self.display.delete(0, tk.END)
        elif op == '←':
            # Backspace
            self.current_value = self.current_value[:-1]
            self.display.delete(0, tk.END)
            self.display.insert(0, self.current_value)
        elif op == '±':
            # Toggle sign
            if self.current_value:
                if self.current_value.startswith('-'):
                    self.current_value = self.current_value[1:]
                else:
                    self.current_value = '-' + self.current_value
                self.display.delete(0, tk.END)
                self.display.insert(0, self.current_value)

if __name__ == "__main__":
    root = tk.Tk()
    app = Calculator(root)
    root.mainloop()
