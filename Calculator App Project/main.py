import tkinter as tk
from tkinter import messagebox

class CalculatorApp(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator App")
        self.geometry("400x300")
        self.resizable(width=False, height=False)
        self.configure(bg="#4b0082")

        self._build_ui()

    def _build_ui(self):
        title = tk.Label(self, text="Calculator", bg="#4b0082", fg="white", font=("Arial", 16, "bold"))
        title.grid(column=0, row=0, columnspan=2, sticky="w", padx=12, pady=(12,16))

        tk.Label(self, text="First number:", bg="#4b0082", fg="white", font=("Arial", 12, "bold")).grid(column=0, row=1, sticky="w", padx=12, pady=6)

        self.first_var = tk.StringVar()
        self.first_entry = tk.Entry(self, textvariable=self.first_var, font=("Arial", 12))
        self.first_entry.grid(column=1, row=1, sticky="w", padx=12, pady=6)

        tk.Label(self, text="Second number:", bg="#4b0082", fg="white", font=("Arial", 12, "bold")).grid(column=0, row=2, sticky="w", padx=12, pady=6)

        self.second_var = tk.StringVar()
        self.second_entry = tk.Entry(self, textvariable=self.second_var, font=("Arial", 12))
        self.second_entry.grid(column=1, row=2, sticky="w", padx=12, pady=6)

        self.result_var = tk.StringVar(value="Result: -")
        result_label = tk.Label(self, textvariable=self.result_var, bg="#4b0082", fg="white", font=("Arial", 12, "bold"))
        result_label.grid(column=0, row=3, columnspan=2, sticky="w", padx=12, pady=(10,16))

        btn_frame = tk.Frame(self, bg="#4b0082")
        btn_frame.grid(column=0, row=4, columnspan=2,sticky="ew", padx=12, pady=6)

        buttons = [
            ("Add (+)", "+"),
            ("Subtract", "-"),
            ("Multiply", "*"),
            ("Divide", "/"),
        ]

        for i, (text, operator) in enumerate(buttons):
            tk.Button(btn_frame, text=text, command=lambda o=operator: self.calculate(o), bg="#4b0082", fg="white", font=("Arial", 12, "bold"), activebackground="#16a34a", activeforeground="white", width=14).grid(row=i // 2, column=i % 2, sticky="ew", padx=6, pady=6)

        tk.Button(self, text="Clear", command=self.clear, bg="#ef4444", fg="white", font=("Arial", 12, "bold"), activebackground="#dc2626", activeforeground="white").grid(row=5, column=0, columnspan=2, padx=12, pady=(10,12), sticky="ew")

        self.grid_columnconfigure(1, weight=1)

        self.first_entry.focus()
        self.bind("Return", lambda _event: self.calculate("+"))

    def _parse_numbers(self):
        a = self.first_var.get().strip()
        b = self.second_var.get().strip()

        if not a or not b:
            messagebox.showerror("Error", "Please fill both numbers.")
            return None

        try:
            return float(a), float(b)
        except ValueError:
            messagebox.showerror("Error", "Please enter valid numbers.")
            return None

    def calculate(self, operator : str):
        nums = self._parse_numbers()
        if nums is None:
            return

        a, b = nums

        try:
            if operator == "+":
                result = a + b
            elif operator == "-":
                result = a - b
            elif operator == "*":
                result = a * b
            elif operator == "/":
                if b == 0:
                    raise ZeroDivisionError
                result = a / b
            else:
                messagebox.showerror("Error", "Unknown operator.")
                return

            self.result_var.set(f"Result: {result}")
        except ZeroDivisionError:
            messagebox.showerror("Error", "Cannot divide by zero.")
    def clear(self):
        self.first_var.set("")
        self.second_var.set("")
        self.result_var.set("Result: -")
        self.first_entry.focus()

if __name__ == "__main__":
    app = CalculatorApp()
    app.mainloop()