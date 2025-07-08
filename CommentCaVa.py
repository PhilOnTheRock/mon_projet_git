import tkinter as tk
from tkinter import messagebox

def repondre_oui():
    messagebox.showinfo("Réponse", "Je suis content")
    root.destroy()

def repondre_non():
    messagebox.showinfo("Réponse", "Je suis vraiment désolé")
    root.destroy()

# Création de la fenêtre principale
root = tk.Tk()
root.title("Dialogue")
root.geometry("300x150")

# Message principal
label = tk.Label(root, text="Comment vas-tu ?", font=("Arial", 14))
label.pack(pady=20)

# Boutons
btn_oui = tk.Button(root, text="Oui", command=repondre_oui, width=10)
btn_oui.pack(side="left", expand=True, padx=20)

btn_non = tk.Button(root, text="Non", command=repondre_non, width=10)
btn_non.pack(side="right", expand=True, padx=20)

# Lancement de la boucle principale
root.mainloop()
