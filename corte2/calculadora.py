import tkinter as tk
from tkinter import messagebox

class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Calculadora")

        self.create_widgets()

    def create_widgets(self):
        # Etiqueta de entrada para el primer número
        self.label1 = tk.Label(self.window, text="Número 1:")
        self.label1.grid(row=0, column=0)

        self.entry1 = tk.Entry(self.window)
        self.entry1.grid(row=0, column=1)

        # Etiqueta de entrada para el segundo número
        self.label2 = tk.Label(self.window, text="Número 2:")
        self.label2.grid(row=1, column=0)

        self.entry2 = tk.Entry(self.window)
        self.entry2.grid(row=1, column=1)

        # Botones de operaciones
        self.button_add = tk.Button(self.window, text="Suma", command=self.add)
        self.button_add.grid(row=2, column=0)

        self.button_subtract = tk.Button(self.window, text="Resta", command=self.subtraction)
        self.button_subtract.grid(row=2, column=1)

        self.button_multiply = tk.Button(self.window, text="Multiplicación", command=self.multiply)
        self.button_multiply.grid(row=3, column=0)

        self.button_divide = tk.Button(self.window, text="División", command=self.divide)
        self.button_divide.grid(row=3, column=1)

        # Etiqueta para mostrar el resultado
        self.result_label = tk.Label(self.window, text="Resultado:")
        self.result_label.grid(row=4, column=0)

        self.result_value = tk.Label(self.window, text="")
        self.result_value.grid(row=4, column=1)

    def get_values(self):
        try:
            a = float(self.entry1.get())
            b = float(self.entry2.get())
            return a, b
        except ValueError:
            messagebox.showerror("Error", "Por favor, ingresa números válidos.")
            return None, None

    def add(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            result = a + b
            self.show_result(result)

    def subtraction(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            result = a - b
            self.show_result(result)

    def multiply(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            result = a * b
            self.show_result(result)

    def divide(self):
        a, b = self.get_values()
        if a is not None and b is not None:
            if b == 0:
                messagebox.showerror("Error", "No se puede dividir por cero.")
            else:
                result = a / b
                self.show_result(result)

    def show_result(self, result):
        self.result_value.config(text=str(result))

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    calc = Calculator()
    calc.run()
