import tkinter as tk
from tkinter import messagebox

class AljabarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Kalkulator Matriks - Kelompok 2")
        self.root.geometry("850x750")
        
        # PALET WARNA
        self.bg_main = "#121212"
        self.bg_card = "#1E1E1E"
        self.green = "#42b26d"
        self.white = "#FFFFFF"
        
        self.root.configure(bg=self.bg_main)
        self.container = tk.Frame(self.root, bg=self.bg_main)
        self.container.pack(fill="both", expand=True)

        self.show_dashboard()

    def clear_screen(self):
        for widget in self.container.winfo_children():
            widget.destroy()

    # 1. DASHBOARD UTAMA (MENU PILIHAN)
    def show_dashboard(self):
        self.clear_screen()
        
        tk.Frame(self.container, bg=self.green, height=5).pack(fill="x")
        
        header = tk.Frame(self.container, bg=self.bg_main, pady=60)
        header.pack(fill="x")
        
        tk.Label(header, text="ALJABAR GEOMETRI", bg=self.bg_main, fg=self.white, font=("Helvetica", 35, "bold")).pack()
        tk.Label(header, text="TUGAS BESAR UAS SEMESTER GANJIL 2025/2026", bg=self.bg_main, fg=self.green, font=("Helvetica", 10, "bold")).pack(pady=5)
        tk.Label(header, text="Informatika - STT Cipasung", bg=self.bg_main, fg="#888", font=("Helvetica", 9)).pack()

        menu_frame = tk.Frame(self.container, bg=self.bg_main)
        menu_frame.place(relx=0.5, rely=0.65, anchor="center")

        style_btn = {"font": ("Helvetica", 11, "bold"), "width": 35, "height": 2, "relief": "flat", "cursor": "hand2"}

        tk.Button(menu_frame, text="PROSES KALKULATOR MATRIKS", command=self.setup_kalkulator_ui, bg=self.green, fg="black", **style_btn).grid(row=0, pady=10)
        tk.Button(menu_frame, text="IDENTITAS KELOMPOK", command=self.show_info_kelompok, bg=self.bg_card, fg=self.green, **style_btn).grid(row=1, pady=10)
        tk.Button(menu_frame, text="INFORMASI APLIKASI", command=self.show_info_aplikasi, bg=self.bg_card, fg=self.white, **style_btn).grid(row=2, pady=10)
        tk.Button(menu_frame, text="KELUAR", command=self.root.destroy, bg="#331111", fg="white", **style_btn).grid(row=3, pady=10)

    # 2. IDENTITAS KELOMPOK 
    def show_info_kelompok(self):
        self.clear_screen()
        card = tk.Frame(self.container, bg=self.bg_card, padx=60, pady=50, highlightbackground=self.green, highlightthickness=1)
        card.place(relx=0.5, rely=0.5, anchor="center")

        tk.Label(card, text="KELOMPOK PENYUSUN", bg=self.bg_card, fg=self.green, font=("Helvetica", 18, "bold")).pack(pady=(0,25))
        
        # List Anggota kelompok
        anggota = [
            "👤 Yandi Alfiansyah (10224052)", 
            "👤 Lutfi Ismail A. P. (10224004)", 
            "👤 Rizki Permadi Salim (10224126)", 
            "👤 Jaka Ismail (10224092)", 
            "👤 Ardika Mahesa (10224036)",
            "👤 Ade Sopi Fauzan (10224041)"
        ]
        for a in anggota:
            tk.Label(card, text=a, bg=self.bg_card, fg=self.white, font=("Consolas", 12), pady=8).pack()

        tk.Button(card, text="KEMBALI KE MENU", command=self.show_dashboard, bg="#444", fg="white", relief="flat", padx=20, pady=8).pack(pady=(35,0))

    
    # 3. KALKULATOR UTAMA
    def setup_kalkulator_ui(self):
        self.clear_screen()
        
        # Top Nav Bar
        top_nav = tk.Frame(self.container, bg=self.bg_card, height=60)
        top_nav.pack(fill="x")
        tk.Button(top_nav, text="← DASHBOARD", command=self.show_dashboard, bg=self.bg_card, fg=self.green, relief="flat", font=("bold")).pack(side="left", padx=20, pady=15)

        # Main Workspace
        work = tk.Frame(self.container, bg=self.bg_main, padx=50)
        work.pack(fill="both", expand=True)

        # Input Card
        input_f = tk.Frame(work, bg=self.bg_card, pady=25, padx=25)
        input_f.pack(fill="x", pady=20)

        tk.Label(input_f, text="MATRIKS A (Contoh: 1,2;3,4)", bg=self.bg_card, fg=self.green, font=("bold")).pack(anchor="w")
        self.entA = tk.Entry(input_f, width=60, font=("Consolas", 12), bg=self.bg_main, fg=self.white, borderwidth=0, insertbackground="white")
        self.entA.pack(pady=(5,15), ipady=8)

        tk.Label(input_f, text="MATRIKS B / VEKTOR b (Opsional)", bg=self.bg_card, fg=self.green, font=("bold")).pack(anchor="w")
        self.entB = tk.Entry(input_f, width=60, font=("Consolas", 12), bg=self.bg_main, fg=self.white, borderwidth=0, insertbackground="white")
        self.entB.pack(pady=5, ipady=8)

        # Button Grid
        btn_f = tk.Frame(work, bg=self.bg_main)
        btn_f.pack()

        ops = [
            ("PENJUMLAHAN (A+B)", lambda: self.hitung_mtx('+')), # Poin 1 & 30
            ("PENGURANGAN (A-B)", lambda: self.hitung_mtx('-')), # Poin 1 & 31
            ("TRANSPOSE A", self.hitung_transpose),              # Poin 2 & 32
            ("INVERS A (2x2)", self.hitung_invers),              # Poin 3
            ("DETERMINAN A", self.hitung_determinan),            # Poin 4 & 35
            ("SOLUSI SPL (2x3)", self.hitung_spl)                # Poin 5
        ]

        r, c = 0, 0
        for text, cmd in ops:
            btn = tk.Button(btn_f, text=text, command=cmd, width=22, bg=self.bg_card, fg=self.white, relief="flat", activebackground=self.green)
            btn.grid(row=r, column=c, padx=8, pady=8)
            c += 1
            if c > 1: c = 0; r += 1

        # Panel Hasil
        tk.Label(work, text="TERMINAL OUTPUT", bg=self.bg_main, fg="#555", font=("bold", 9)).pack(anchor="w", pady=(15,0))
        self.res_txt = tk.Text(work, height=8, bg="black", fg=self.white, font=("Consolas", 11), padx=15, pady=15, borderwidth=0)
        self.res_txt.pack(fill="x")

    # LOGIKA MATEMATIKA
    def get_data(self, e):
        try: return [list(map(float, r.split(","))) for r in e.get().strip().split(";")]
        except: return None

    def hitung_mtx(self, op):
        A, B = self.get_data(self.entA), self.get_data(self.entB)
        if A and B and len(A)==2:
            res = [[(A[i][j]+B[i][j] if op=='+' else A[i][j]-B[i][j]) for j in range(2)] for i in range(2)]
            self.show_output(res)
        else: messagebox.showerror("Error", "Matriks A dan B harus 2x2")

    def hitung_transpose(self):
        A = self.get_data(self.entA)
        if A: self.show_output([[A[j][i] for j in range(len(A))] for i in range(len(A[0]))])

    def hitung_determinan(self):
        A = self.get_data(self.entA)
        if A:
            n = len(A)
            if n==2: det = A[0][0]*A[1][1]-A[0][1]*A[1][0]
            else:
                det = (A[0][0]*A[1][1]*A[2][2]+A[0][1]*A[1][2]*A[2][0]+A[0][2]*A[1][0]*A[2][1])-(A[0][2]*A[1][1]*A[2][0]+A[0][0]*A[1][2]*A[2][1]+A[0][1]*A[1][0]*A[2][2])
            self.show_output(f"Determinan = {det}")

    def hitung_invers(self):
        A = self.get_data(self.entA)
        if A and len(A)==2:
            d = A[0][0]*A[1][1]-A[0][1]*A[1][0]
            if d!=0: self.show_output([[A[1][1]/d, -A[0][1]/d], [-A[1][0]/d, A[0][0]/d]])
            else: self.show_output("Matriks tidak punya invers (Det=0)")

    def hitung_spl(self):
        A, B = self.get_data(self.entA), self.get_data(self.entB)
        if A and B and len(A)==2:
            a11, a12, a21, a22 = A[0][0], A[0][1], A[1][0], A[1][1]
            b1, b2 = B[0][0], B[1][0]
            det = a11*a22 - a12*a21
            if det!=0:
                self.show_output(f"Hasil SPL:\nx = {(b1*a22 - a12*b2)/det}\ny = {(a11*b2 - b1*a21)/det}")

    def show_output(self, data):
        self.res_txt.delete("1.0", tk.END)
        # self.res_txt.insert(tk.END, f">>> SYSTEM_READY\n>>> OUTPUT RESULT:\n{data}")
        self.res_txt.insert(tk.END, f"OUTPUT RESULT:\n{data}")

    def show_info_aplikasi(self):
        self.clear_screen()
        f = tk.Frame(self.container, bg=self.bg_card, padx=40, pady=40, highlightbackground=self.green, highlightthickness=1)
        f.place(relx=0.5, rely=0.5, anchor="center")
        tk.Label(f, text="INFORMASI TUGAS BESAR", bg=self.bg_card, fg=self.green, font=("Helvetica", 14, "bold")).pack()
        t = "IF Aljabar Geometri 2025/2026\nSTT Cipasung\n\n- Operasi Matriks 2x2 & 3x3\n- Invers & Determinan\n- Solusi SPL (Metode Cramer)\n- Built with Python & Tkinter\n- Referensi YT Kelas Terbuka\n- YT Erfan Erianto Belajar GUI "
        tk.Label(f, text=t, bg=self.bg_card, fg=self.white, justify="left").pack(pady=15)
        tk.Button(f, text="CLOSE", command=self.show_dashboard, bg="#333", fg="white", relief="flat").pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = AljabarApp(root)
    root.mainloop()
