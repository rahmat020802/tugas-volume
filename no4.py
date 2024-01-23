import tkinter as tk
from math import pi

def hitung():
    try:
        jari_jari = float(entry_jari_jari.get())
        tinggi = float(entry_tinggi.get())

        # Hitung volume
        volume = pi * jari_jari**2 * tinggi
        label_volume.config(text=f"Volume: {volume:.2f} satuan volume³")

        # Hitung luas kulit tabung
        luas_kulit = 2 * pi * jari_jari * (jari_jari + tinggi)
        label_luas_kulit.config(text=f"Luas Kulit: {luas_kulit:.2f} satuan luas²")

    except ValueError:
        label_volume.config(text="Masukkan angka valid untuk jari-jari dan tinggi")

# Membuat GUI
root = tk.Tk()
root.title("Aplikasi Perhitungan Tabung")

# Label dan Entry untuk jari-jari
label_jari_jari = tk.Label(root, text="Jari-Jari:")
label_jari_jari.grid(row=0, column=0, padx=10, pady=10)
entry_jari_jari = tk.Entry(root)
entry_jari_jari.grid(row=0, column=1, padx=10, pady=10)

# Label dan Entry untuk tinggi
label_tinggi = tk.Label(root, text="Tinggi:")
label_tinggi.grid(row=1, column=0, padx=10, pady=10)
entry_tinggi = tk.Entry(root)
entry_tinggi.grid(row=1, column=1, padx=10, pady=10)

# Tombol hitung
button_hitung = tk.Button(root, text="Hitung", command=hitung)
button_hitung.grid(row=2, column=0, columnspan=2, pady=10)

# Label untuk hasil perhitungan
label_volume = tk.Label(root, text="Volume: ")
label_volume.grid(row=3, column=0, columnspan=2)

label_luas_kulit = tk.Label(root, text="Luas Kulit: ")
label_luas_kulit.grid(row=4, column=0, columnspan=2)

# Menjalankan aplikasi
root.mainloop()