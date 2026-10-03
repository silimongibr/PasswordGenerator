# Librerias
import tkinter as tk
from tkinter import messagebox

def nivel_medio(nivel):
    messagebox.showinfo("Nivel Medio", f"Has seleccionado el nivel medio: {nivel}") 
    

def nivel_alto(nivel):
    messagebox.showinfo("Nivel Alto", f"Has seleccionado el nivel alto: {nivel}")


root=tk.Tk()
root.title("Password Generator")
root.geometry("400x300")

# Etiquetas
tk.Label(root, text="Generador de Contraseñas").grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(root, text="Seleccciona el nivel de contraseña").grid(row=1, column=0, columnspan=2, pady=5)

#Botones
btn_nivelmedio = tk.Button(root, text="Nivel medio", command=lambda: nivel_medio(1)) 
btn_nivelmedio.grid(row=3, column=0, padx=5, pady=5) 

btn_nivelalto = tk.Button(root, text="Nivel alto", command=lambda: nivel_alto(2))
btn_nivelalto.grid(row=3, column=1, padx=5, pady=5)

root.mainloop()

