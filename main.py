import streamlit as st
import pandas as pd
import numpy as np

# Titolo dell'app
st.title("🧮 Calcolatrice Semplice")
st.write("Esegui somme e sottrazioni in modo facile!")

# Sezione Somma
st.header("➕ Somma")
col1, col2 = st.columns(2)

with col1:
    num1_somma = st.number_input("Primo numero", value=0.0, key="somma1")
with col2:
    num2_somma = st.number_input("Secondo numero", value=0.0, key="somma2")

if st.button("Calcola Somma", type="primary"):
    risultato_somma = num1_somma + num2_somma
    st.success(f"✅ Risultato: {num1_somma} + {num2_somma} = **{risultato_somma}**")

st.divider()

# Sezione Sottrazione
st.header("➖ Sottrazione")
col3, col4 = st.columns(2)

with col3:
    num1_sottrazione = st.number_input("Primo numero", value=0.0, key="sott1")
with col4:
    num2_sottrazione = st.number_input("Secondo numero", value=0.0, key="sott2")

if st.button("Calcola Sottrazione", type="primary"):
    risultato_sottrazione = num1_sottrazione - num2_sottrazione
    st.success(f"✅ Risultato: {num1_sottrazione} - {num2_sottrazione} = **{risultato_sottrazione}**")


x = np.linspace(0, 1, 1000)
y = np.random.randn(1000)
df = pd.DataFrame([], columns=["x", "y"])
df["x"] = x
df["y"] = y


st.bar_chart(df, x="x", y="y")

# Footer
st.divider()
st.caption("💡 Inserisci i numeri e clicca sul pulsante per vedere il risultato!")

import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np


class NumberInterface:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Number Calculator - NumPy Operations")
        self.root.geometry("600x500")

        self.setup_ui()

    def setup_ui(self):
        """Setup the user interface"""
        # Main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Title
        title_label = ttk.Label(main_frame, text="Number Calculator",
                                font=('Arial', 18, 'bold'))
        title_label.grid(row=0, column=0, columnspan=2, pady=20)

        # Number input section
        input_frame = ttk.LabelFrame(main_frame, text="Enter Two Numbers", padding="15")
        input_frame.grid(row=1, column=0, columnspan=2, sticky=(tk.W, tk.E), pady=10)

        # First number
        ttk.Label(input_frame, text="First Number:", font=('Arial', 12)).grid(row=0, column=0, sticky=tk.W, pady=5)
        self.num1_var = tk.StringVar(value="0.0")
        self.num1_entry = ttk.Entry(input_frame, textvariable=self.num1_var, font=('Arial', 12), width=20)
        self.num1_entry.grid(row=0, column=1, pady=5, padx=10)

        # Second number
        ttk.Label(input_frame, text="Second Number:", font=('Arial', 12)).grid(row=1, column=0, sticky=tk.W, pady=5)
        self.num2_var = tk.StringVar(value="0.0")
        self.num2_entry = ttk.Entry(input_frame, textvariable=self.num2_var, font=('Arial', 12), width=20)
        self.num2_entry.grid(row=1, column=1, pady=5, padx=10)

        # Calculate button
        calc_btn = ttk.Button(input_frame, text="Calculate All Operations",
                              command=self.calculate_operations, style='Accent.TButton')
        calc_btn.grid(row=2, column=0, columnspan=2, pady=15)

        # Results section
        results_frame = ttk.LabelFrame(main_frame, text="Results", padding="15")
        results_frame.grid(row=2, column=0, columnspan=2, sticky=(tk.W, tk.E, tk.N, tk.S), pady=10)

        # Basic operations
        basic_frame = ttk.LabelFrame(results_frame, text="Basic Operations", padding="10")
        basic_frame.grid(row=0, column=0, sticky=(tk.W, tk.E), pady=5)

        self.results_text = tk.Text(results_frame, height=15, width=60, font=('Courier', 10))
        self.results_text.grid(row=1, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Scrollbar for results
        scrollbar = ttk.Scrollbar(results_frame, command=self.results_text.yview)
        scrollbar.grid(row=1, column=1, sticky=(tk.N, tk.S))
        self.results_text.config(yscrollcommand=scrollbar.set)

        # Clear button
        clear_btn = ttk.Button(main_frame, text="Clear Results", command=self.clear_results)
        clear_btn.grid(row=3, column=0, pady=10)

        # Exit button
        exit_btn = ttk.Button(main_frame, text="Exit", command=self.root.quit)
        exit_btn.grid(row=3, column=1, pady=10)

        # Configure grid weights
        self.root.columnconfigure(0, weight=1)
        self.root.rowconfigure(0, weight=1)
        main_frame.columnconfigure(0, weight=1)
        main_frame.rowconfigure(2, weight=1)
        results_frame.columnconfigure(0, weight=1)
        results_frame.rowconfigure(1, weight=1)

        # Bind Enter key to calculate
        self.root.bind('<Return>', lambda event: self.calculate_operations())

    def get_numbers(self):
        """Get and validate the two numbers"""
        try:
            num1 = float(self.num1_var.get())
            num2 = float(self.num2_var.get())
            return num1, num2
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter valid numbers")
            return None, None

    def calculate_operations(self):
        """Calculate all operations on the two numbers"""
        num1, num2 = self.get_numbers()

        if num1 is None or num2 is None:
            return

        self.results_text.delete(1.0, tk.END)

        # Basic operations
        self.results_text.insert(tk.END, "=" * 50 + "\n")
        self.results_text.insert(tk.END, "BASIC OPERATIONS\n")
        self.results_text.insert(tk.END, "=" * 50 + "\n\n")
        self.results_text.insert(tk.END, f"Numbers: {num1} and {num2}\n\n")

        self.results_text.insert(tk.END, f"Addition:       {num1} + {num2} = {num1 + num2}\n")
        self.results_text.insert(tk.END, f"Subtraction:    {num1} - {num2} = {num1 - num2}\n")
        self.results_text.insert(tk.END, f"Multiplication: {num1} * {num2} = {num1 * num2}\n")

        if num2 != 0:
            self.results_text.insert(tk.END, f"Division:       {num1} / {num2} = {num1 / num2}\n")
            self.results_text.insert(tk.END, f"Modulo:         {num1} % {num2} = {num1 % num2}\n")
        else:
            self.results_text.insert(tk.END, f"Division:       Cannot divide by zero\n")
            self.results_text.insert(tk.END, f"Modulo:         Cannot modulo by zero\n")

        self.results_text.insert(tk.END, f"Power:          {num1} ** {num2} = {num1 ** num2}\n")

        # NumPy operations
        self.results_text.insert(tk.END, "\n" + "=" * 50 + "\n")
        self.results_text.insert(tk.END, "NUMPY OPERATIONS\n")
        self.results_text.insert(tk.END, "=" * 50 + "\n\n")

        # Create arrays
        arr1 = np.array([num1, num2])
        arr2 = np.array([num2, num1])

        self.results_text.insert(tk.END, f"Array 1: {arr1}\n")
        self.results_text.insert(tk.END, f"Array 2: {arr2}\n\n")

        self.results_text.insert(tk.END, f"Array addition:     {arr1} + {arr2} = {arr1 + arr2}\n")
        self.results_text.insert(tk.END, f"Array multiplication: {arr1} * {arr2} = {arr1 * arr2}\n")
        self.results_text.insert(tk.END, f"Dot product:        np.dot({arr1}, {arr2}) = {np.dot(arr1, arr2)}\n\n")

        # Statistical operations
        self.results_text.insert(tk.END, "Statistical Operations:\n")
        self.results_text.insert(tk.END, f"Mean:        np.mean([{num1}, {num2}]) = {np.mean(arr1)}\n")
        self.results_text.insert(tk.END, f"Sum:         np.sum([{num1}, {num2}]) = {np.sum(arr1)}\n")
        self.results_text.insert(tk.END, f"Maximum:     np.max([{num1}, {num2}]) = {np.max(arr1)}\n")
        self.results_text.insert(tk.END, f"Minimum:     np.min([{num1}, {num2}]) = {np.min(arr1)}\n")
        self.results_text.insert(tk.END, f"Std Dev:     np.std([{num1}, {num2}]) = {np.std(arr1):.6f}\n")
        self.results_text.insert(tk.END, f"Variance:    np.var([{num1}, {num2}]) = {np.var(arr1):.6f}\n")

        # Matrix operations
        self.results_text.insert(tk.END, "\n" + "=" * 50 + "\n")
        self.results_text.insert(tk.END, "MATRIX OPERATIONS\n")
        self.results_text.insert(tk.END, "=" * 50 + "\n\n")

        # Create 2x2 matrix
        matrix = np.array([[num1, num2], [num2, num1]])
        self.results_text.insert(tk.END, f"Matrix:\n{matrix}\n\n")

        self.results_text.insert(tk.END, f"Determinant:  {np.linalg.det(matrix):.6f}\n")
        self.results_text.insert(tk.END, f"Trace:        {np.trace(matrix)}\n")
        self.results_text.insert(tk.END, f"Transpose:\n{matrix.T}\n")

        try:
            inverse = np.linalg.inv(matrix)
            self.results_text.insert(tk.END, f"Inverse:\n{inverse}\n")
        except:
            self.results_text.insert(tk.END, "Inverse:      Matrix is singular (no inverse)\n")

        # Advanced operations
        self.results_text.insert(tk.END, "\n" + "=" * 50 + "\n")
        self.results_text.insert(tk.END, "ADVANCED OPERATIONS\n")
        self.results_text.insert(tk.END, "=" * 50 + "\n\n")

        # Create larger arrays for demonstration
        larger_arr = np.linspace(num1, num2, 10)
        self.results_text.insert(tk.END, f"Linspace array (10 points from {num1} to {num2}):\n")
        self.results_text.insert(tk.END, f"{larger_arr}\n\n")

        self.results_text.insert(tk.END, f"Reshaped to 2x5:\n{larger_arr.reshape(2, 5)}\n\n")

        # Random operations
        random_arr = np.random.uniform(num1, num2, 5)
        self.results_text.insert(tk.END, f"Random array (5 values between {num1} and {num2}):\n")
        self.results_text.insert(tk.END, f"{random_arr}\n")

    def clear_results(self):
        """Clear the results text"""
        self.results_text.delete(1.0, tk.END)
        self.num1_var.set("0.0")
        self.num2_var.set("0.0")
        self.num1_entry.focus()

    def run(self):
        """Run the application"""
        self.num1_entry.focus()
        self.root.mainloop()


def main():
    """Main function to run the number interface"""
    print("Starting Number Interface...")
    print("This application provides a GUI for entering two numbers and performing various operations.")
    print("\nFeatures:")
    print("- Enter two numbers")
    print("- Basic arithmetic operations")
    print("- NumPy array operations")
    print("- Matrix operations")
    print("- Statistical calculations")
    print("- Advanced NumPy demonstrations")
    print("\nPress Enter in any input field to calculate!")

    app = NumberInterface()
    app.run()


if __name__ == "__main__":
    main()
