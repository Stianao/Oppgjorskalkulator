import tkinter as tk
from tkinter import ttk, messagebox
from Oppgjorskalkulator import Oppgjor

def regn_ut_oppgjor():
    try:
        antall_personer = int(entry_antall_personer.get())
        mat = float(entry_mat.get())
        liter_per_km = float(entry_liter_per_kilometer.get())
        kr_per_kilometer = float(entry_kr_per_kilometer.get())
        km = float(entry_km.get())
        
        oppgjor = Oppgjor(antall_personer, mat)
        oppgjor.kilometer_godtgjorelse(liter_per_km, kr_per_kilometer, km)
        
        messagebox.showinfo("Oppgjør", oppgjor.vis_oppgjoret())
        
    except ValueError:
        messagebox.showerror("Error", "Fyll inn alle feltene med gyldige tall.")
        

root = tk.Tk()
root.geometry("430x330")
root.title("Oppgjørskalkulator")

tk.Label(root, text="Antall personer: ", font=10).grid(row=1, column=0, sticky="w", pady=10)
entry_antall_personer = tk.Entry(root, font=10)
entry_antall_personer.grid(row = 1, column=1)

tk.Label(root, text="Matutgifter: ", font=10).grid(row=2, column=0, sticky="w", pady=10)
entry_mat = tk.Entry(root, font=10)
entry_mat.grid(row=2, column=1)

tk.Label(root, text="Liter per km: ", font=10).grid(row=3, column=0, sticky="w", pady=10)
entry_liter_per_kilometer = tk.Entry(root, font=10)
entry_liter_per_kilometer.grid(row=3, column=1)

tk.Label(root, text="Kr per liter: ", font=10).grid(row=4, column=0, sticky="w", pady=10)
entry_kr_per_kilometer = tk.Entry(root, font=10)
entry_kr_per_kilometer.grid(row=4, column=1)

tk.Label(root, text="Distanse en vei (km)", font=10).grid(row=5, column=0, sticky="w", pady=10)
entry_km = tk.Entry(root, font=12)
entry_km.grid(row=5, column=1)

stil = ttk.Style()
stil.configure("Big.TButton", font=("Arial", 12), padding=(20, 10))

utregning_knapp = ttk.Button(root, text="Regn ut oppgjøret", command = regn_ut_oppgjor, style="Big.TButton")
utregning_knapp.grid(row=6, columnspan=2, pady=10)

def start_gui():
    root.mainloop()

if __name__ == "__main__":
    start_gui()