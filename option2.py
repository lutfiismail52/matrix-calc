import tkinter as tk
from tkinter import messagebox


class MatrixCalculatorApp:
    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Kalkulator Matriks - Aljabar Geometri")
        self.root.geometry("700x600")

        self.build_ui()

    # UI
    def build_ui(self):
        frame = tk.Frame(self.root, padx=20, pady=20)
        frame.pack(fill="both", expand=True)

        tk.Label(frame, text="Kalkulator Matriks", font=("Helvetica", 18, "bold")).pack(pady=10)

        tk.Label(frame, text="Matriks A (contoh: 1,2;3,4)").pack(anchor="w")
        self.entry_a = tk.Entry(frame, width=50)
        self.entry_a.pack(pady=5)

        tk.Label(frame, text="Matriks B / vektor b (opsional)").pack(anchor="w")
        self.entry_b = tk.Entry(frame, width=50)
        self.entry_b.pack(pady=5)

        btn_frame = tk.Frame(frame)
        btn_frame.pack(pady=15)

        tk.Button(btn_frame, text="A + B", width=20, command=self.add_matrix).grid(row=0, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="A - B", width=20, command=self.sub_matrix).grid(row=0, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Transpose A", width=20, command=self.transpose_matrix).grid(row=1, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="Invers A (2x2)", width=20, command=self.inverse_matrix).grid(row=1, column=1, padx=5, pady=5)
        tk.Button(btn_frame, text="Determinan A", width=20, command=self.determinant_matrix).grid(row=2, column=0, padx=5, pady=5)
        tk.Button(btn_frame, text="SPL (Cramer)", width=20, command=self.solve_spl).grid(row=2, column=1, padx=5, pady=5)

        tk.Label(frame, text="Output").pack(anchor="w", pady=(10, 0))
        self.output = tk.Text(frame, height=8)
        self.output.pack(fill="x")

    # Utility
    def parse_matrix(self, entry: tk.Entry):
        try:
            rows = entry.get().strip().split(";")
            return [list(map(float, row.split(","))) for row in rows]
        except ValueError:
            return None

    def is_matrix_2x2(self, m):
        return len(m) == 2 and all(len(row) == 2 for row in m)

    def is_matrix_3x3(self, m):
        return len(m) == 3 and all(len(row) == 3 for row in m)

    def show_output(self, text):
        self.output.delete("1.0", tk.END)
        self.output.insert(tk.END, text)

    # Operations
    def add_matrix(self):
        A = self.parse_matrix(self.entry_a)
        B = self.parse_matrix(self.entry_b)

        if not A or not B or not self.is_matrix_2x2(A) or not self.is_matrix_2x2(B):
            messagebox.showerror("Error", "Penjumlahan membutuhkan dua matriks 2x2")
            return

        result = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
        self.show_output(f"Hasil A + B:\n{result}")

    def sub_matrix(self):
        A = self.parse_matrix(self.entry_a)
        B = self.parse_matrix(self.entry_b)

        if not A or not B or not self.is_matrix_2x2(A) or not self.is_matrix_2x2(B):
            messagebox.showerror("Error", "Pengurangan membutuhkan dua matriks 2x2")
            return

        result = [[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]
        self.show_output(f"Hasil A - B:\n{result}")

    def transpose_matrix(self):
        A = self.parse_matrix(self.entry_a)

        if not A:
            messagebox.showerror("Error", "Input matriks A tidak valid")
            return

        result = list(map(list, zip(*A)))
        self.show_output(f"Transpose A:\n{result}")

    def inverse_matrix(self):
        A = self.parse_matrix(self.entry_a)

        if not A or not self.is_matrix_2x2(A):
            messagebox.showerror("Error", "Invers hanya untuk matriks 2x2")
            return

        det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        if det == 0:
            self.show_output("Matriks tidak memiliki invers (determinan = 0)")
            return

        inv = [
            [ A[1][1] / det, -A[0][1] / det],
            [-A[1][0] / det,  A[0][0] / det]
        ]
        self.show_output(f"Invers A:\n{inv}")

    def determinant_matrix(self):
        A = self.parse_matrix(self.entry_a)

        if not A:
            messagebox.showerror("Error", "Input matriks tidak valid")
            return

        if self.is_matrix_2x2(A):
            det = A[0][0] * A[1][1] - A[0][1] * A[1][0]
        elif self.is_matrix_3x3(A):
            det = (
                A[0][0]*A[1][1]*A[2][2] +
                A[0][1]*A[1][2]*A[2][0] +
                A[0][2]*A[1][0]*A[2][1] -
                A[0][2]*A[1][1]*A[2][0] -
                A[0][0]*A[1][2]*A[2][1] -
                A[0][1]*A[1][0]*A[2][2]
            )
        else:
            messagebox.showerror("Error", "Determinan hanya untuk matriks 2x2 atau 3x3")
            return

        self.show_output(f"Determinan = {det}")

    def solve_spl(self):
        A = self.parse_matrix(self.entry_a)
        B = self.parse_matrix(self.entry_b)

        if not A or not B or not self.is_matrix_2x2(A) or len(B) != 2 or len(B[0]) != 1:
            messagebox.showerror("Error", "SPL membutuhkan A (2x2) dan b (2x1)")
            return

        a11, a12 = A[0]
        a21, a22 = A[1]
        b1, b2 = B[0][0], B[1][0]

        det = a11 * a22 - a12 * a21
        if det == 0:
            self.show_output("SPL tidak memiliki solusi tunggal")
            return

        x = (b1 * a22 - a12 * b2) / det
        y = (a11 * b2 - b1 * a21) / det

        self.show_output(f"Hasil SPL:\nx = {x}\ny = {y}")


if __name__ == "__main__":
    root = tk.Tk()
    app = MatrixCalculatorApp(root)
    root.mainloop()
