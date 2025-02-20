import tkinter as tk
from tkinter import ttk

# Hauptfenster erstellen
root = tk.Tk()
root.geometry("1000x750")
root.minsize(800,600)
root.maxsize(1300,900)
root.title("Tkinter GUI Beispiel")

# Frame 1 (Pack-Manager) - Login-Maske
frame1 = ttk.Frame(root, width=300, height=750, style="Frame1.TFrame")
frame1.pack(side="left", fill="both", expand=True)
frame1.pack_propagate(False)

# Login-Maske in Frame 1 hinzufügen
login_label = ttk.Label(frame1, text="Login")
login_label.pack(pady=10)

username_label = ttk.Label(frame1, text="Benutzername:")
username_label.pack(pady=5)

username_entry = ttk.Entry(frame1)
username_entry.pack(pady=5)

password_label = ttk.Label(frame1, text="Passwort:")
password_label.pack(pady=5)

password_entry = ttk.Entry(frame1, show="*")
password_entry.pack(pady=5)

login_button = ttk.Button(frame1, text="Anmelden")
login_button.pack(pady=10)

# Frame 2 (Grid-Manager) - Karteikarte einer Person
frame2 = ttk.Frame(root, width=350, height=750, style="Frame2.TFrame")
frame2.pack(side="left", fill="both", expand=True)
frame2.pack_propagate(False)

# Karteikarte in Frame 2 hinzufügen
name_label = ttk.Label(frame2, text="Vorname:")
name_label.grid(row=0, column=0, pady=5, padx=10, sticky="w")

name_entry = ttk.Entry(frame2)
name_entry.grid(row=0, column=1, pady=5, padx=10)

surname_label = ttk.Label(frame2, text="Nachname:")
surname_label.grid(row=1, column=0, pady=5, padx=10, sticky="w")

surname_entry = ttk.Entry(frame2)
surname_entry.grid(row=1, column=1, pady=5, padx=10)

address_label = ttk.Label(frame2, text="Adresse:")
address_label.grid(row=2, column=0, pady=5, padx=10, sticky="w")

address_entry = ttk.Entry(frame2)
address_entry.grid(row=2, column=1, pady=5, padx=10)

email_label = ttk.Label(frame2, text="E-Mail:")
email_label.grid(row=3, column=0, pady=5, padx=10, sticky="w")

email_entry = ttk.Entry(frame2)
email_entry.grid(row=3, column=1, pady=5, padx=10)

# Frame 3 (Place-Manager) - Leer
frame3 = ttk.Frame(root, width=350, height=750, style="Frame3.TFrame")
frame3.pack(side="left", fill="both", expand=True)
frame3.pack_propagate(False)

# Stile für die Frames definieren
style = ttk.Style()
style.configure("Frame1.TFrame", background="lightblue")
style.configure("Frame2.TFrame", background="lightgreen")
style.configure("Frame3.TFrame", background="lightcoral")

# Hauptfenster-Loop starten
root.mainloop()
