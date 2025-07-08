import tkinter as tk
from tkinter import messagebox, Toplevel, Label, Button, PhotoImage

def repondre_oui():
    messagebox.showinfo("Réponse", "Je suis content")
    root.destroy()

def repondre_non():
    root.withdraw()
    new_window = Toplevel()
    new_window.title("Réconfort")

    try:
        img = PhotoImage(file="pochoir-coeurs.png")
    except Exception as e:
        messagebox.showerror("Erreur image", f"Impossible de charger l'image : {e}")
        root.deiconify()
        return

    new_window.geometry(f"{img.width()}x{img.height() + 80}")

    img_label = Label(new_window, image=img)
    img_label.image = img
    img_label.pack(pady=10)

    label = Label(new_window, text="Ça va mieux ?", font=("Arial", 12))
    label.pack()

    def fermer():
        messagebox.showinfo("Réponse", "Je suis content")
        new_window.destroy()

    def relancer():
        new_window.destroy()
        root.deiconify()

    bouton_oui = Button(new_window, text="Oui", command=fermer, width=10)
    bouton_oui.pack(side="left", padx=20, pady=10, expand=True)

    bouton_non = Button(new_window, text="Non", command=relancer, width=10)
    bouton_non.pack(side="right", padx=20, pady=10, expand=True)

root = tk.Tk()
root.title("Dialogue")
root.geometry("300x150")

label = tk.Label(root, text="Comment vas-tu ?", font=("Arial", 14))
label.pack(pady=20)

btn_oui = tk.Button(root, text="Oui", command=repondre_oui, width=10)
btn_oui.pack(side="left", expand=True, padx=20)

btn_non = tk.Button(root, text="Non", command=repondre_non, width=10)
btn_non.pack(side="right", expand=True, padx=20)

root.mainloop()
