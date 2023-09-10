import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Calculator")
        self.geometry("400x400")

        self.result_var = tk.StringVar()
        
        # Create UI components
        self.create_widgets()

    def create_widgets(self):
        # Entry widget to display the current input
        self.entry = tk.Entry(self, textvar=self.result_var, font=("Arial", 24), bd=10, insertwidth=2, width=14, justify='right')
        self.entry.grid(row=0, column=0, columnspan=4)

        # Create buttons
        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('0', 4, 1),
            ('+', 1, 3), ('-', 2, 3), ('*', 3, 3), ('/', 4, 3),
            ('.', 4, 0), ('=', 4, 2)
        ]

        for (text, row, col) in buttons:
            self.create_button(text, row, col)

    def create_button(self, text, row, col):
        btn = tk.Button(self, text=text, padx=20, pady=20, font=("Arial", 18), command=lambda: self.on_button_click(text))
        btn.grid(row=row, column=col, sticky='nsew')

        # Adjust row and column weights to make buttons expand
        self.grid_rowconfigure(row, weight=1)
        self.grid_columnconfigure(col, weight=1)

    def on_button_click(self, char):
        current_text = self.result_var.get()

        if char == '=':
            try:
                result = eval(current_text)
                self.result_var.set(result)
            except Exception:
                self.result_var.set("Error")
        else:
            new_text = current_text + char
            self.result_var.set(new_text)

if __name__ == "__main__":
    app = Calculator()
    app.mainloop()
