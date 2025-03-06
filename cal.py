import tkinter as tk  # Import the Tkinter library for GUI

# Styling constants
LARGE_FONT = ("Arial", 36, "bold")
SMALL_FONT = ("Arial", 14)
DEFAULT_FONT = ("Arial", 18)
BACKGROUND_COLOR = "#F8FAFF"
BUTTON_COLOR = "#FFFFFF"
OPERATOR_BUTTON_COLOR = "#CCEDFF"
SPECIAL_BUTTON_COLOR = "#F5F5F5"
TEXT_COLOR = "#25265E"


class Calculator:
    """A simple GUI-based calculator using Tkinter."""

    def __init__(self):
        """Initialize the calculator window and components."""
        self.window = tk.Tk()
        self.window.title("Python Calculator")
        self.window.geometry("400x600")
        self.window.resizable(False, False)

        # Variables to store user input
        self.current_input = ""
        self.full_expression = ""

        # Set up display and buttons
        self.create_display()
        self.create_buttons()
        self.setup_key_bindings()

    def create_display(self):
        """Create the display area for the calculator."""
        self.display_frame = tk.Frame(self.window, height=100, bg=SPECIAL_BUTTON_COLOR)
        self.display_frame.pack(expand=True, fill="both")

        self.expression_label = tk.Label(
            self.display_frame, text=self.full_expression,
            font=SMALL_FONT, fg=TEXT_COLOR, bg=SPECIAL_BUTTON_COLOR,
            anchor=tk.E, padx=20
        )
        self.expression_label.pack(expand=True, fill="both")

        self.input_label = tk.Label(
            self.display_frame, text=self.current_input,
            font=LARGE_FONT, fg=TEXT_COLOR, bg=SPECIAL_BUTTON_COLOR,
            anchor=tk.E, padx=20
        )
        self.input_label.pack(expand=True, fill="both")

    def create_buttons(self):
        """Create and arrange calculator buttons."""
        self.button_frame = tk.Frame(self.window)
        self.button_frame.pack(expand=True, fill="both")

        buttons = [
            ("C", 1, 1, self.clear_input), ("⌫", 1, 2, self.delete_last_character),
            ("%", 1, 3, self.convert_to_percentage), ("÷", 1, 4, lambda: self.add_operator("/")),

            ("7", 2, 1, lambda: self.add_digit("7")), ("8", 2, 2, lambda: self.add_digit("8")),
            ("9", 2, 3, lambda: self.add_digit("9")), ("×", 2, 4, lambda: self.add_operator("*")),

            ("4", 3, 1, lambda: self.add_digit("4")), ("5", 3, 2, lambda: self.add_digit("5")),
            ("6", 3, 3, lambda: self.add_digit("6")), ("-", 3, 4, lambda: self.add_operator("-")),

            ("1", 4, 1, lambda: self.add_digit("1")), ("2", 4, 2, lambda: self.add_digit("2")),
            ("3", 4, 3, lambda: self.add_digit("3")), ("+", 4, 4, lambda: self.add_operator("+")),

            ("0", 5, 1, lambda: self.add_digit("0")), (".", 5, 2, lambda: self.add_digit(".")),
            ("=", 5, 3, self.calculate_result)
        ]

        for text, row, col, command in buttons:
            self.create_button(text, row, col, command)

    def create_button(self, text, row, col, command):
        """Helper function to create a button with specific properties."""
        bg_color = BUTTON_COLOR if text not in ["C", "⌫", "%", "÷", "×", "-", "+", "="] else OPERATOR_BUTTON_COLOR

        button = tk.Button(
            self.button_frame, text=text, bg=bg_color, fg=TEXT_COLOR,
            font=DEFAULT_FONT, borderwidth=0, command=command
        )
        button.grid(row=row, column=col, sticky=tk.NSEW, padx=2, pady=2)
        
        self.button_frame.rowconfigure(row, weight=1)
        self.button_frame.columnconfigure(col, weight=1)

    def setup_key_bindings(self):
        """Enable keyboard shortcuts for calculator operations."""
        self.window.bind("<Return>", lambda event: self.calculate_result())
        self.window.bind("<BackSpace>", lambda event: self.delete_last_character())
        
        for char in "0123456789+-*/%.":
            self.window.bind(char, lambda event, c=char: self.add_digit(c))

    def add_digit(self, digit):
        """Append a digit or decimal point to the current input."""
        self.current_input += str(digit)
        self.update_display()

    def add_operator(self, operator):
        """Append an operator if it's valid to do so."""
        if self.current_input and self.current_input[-1] not in "+-*/%":
            self.current_input += operator
            self.update_display()

    def clear_input(self):
        """Clear the calculator display."""
        self.current_input = ""
        self.full_expression = ""
        self.update_display()

    def delete_last_character(self):
        """Remove the last character from the input."""
        self.current_input = self.current_input[:-1]
        self.update_display()

    def convert_to_percentage(self):
        """Convert the current input to a percentage."""
        try:
            self.current_input = str(eval(self.current_input) / 100)
        except:
            self.current_input = "Error"
        self.update_display()

    def calculate_result(self):
        """Evaluate the mathematical expression and display the result."""
        try:
            self.full_expression = self.current_input
            self.current_input = str(eval(self.current_input))
        except:
            self.current_input = "Error"
        self.update_display()

    def update_display(self):
        """Refresh the calculator display with the latest input."""
        self.input_label.config(text=self.current_input[:12])  # Limit display size
        self.expression_label.config(text=self.full_expression)

    def run(self):
        """Start the calculator's main event loop."""
        self.window.mainloop()


# Run the calculator
if __name__ == "__main__":
    calc = Calculator()
    calc.run()