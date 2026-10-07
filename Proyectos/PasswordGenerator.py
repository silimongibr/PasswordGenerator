# Librerias
#import tkinter as tk
#from tkinter import messagebox

import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox



# librerias para generar contraseñas
import secrets
import string




def nivel_medio(nivel):
    Messagebox.show_info("Nivel Medio", f"Se generará contraseña de {nivel} caracteres (solo letras y numeros).") 

    # Generar una contraseña de nivel medio con numeros y letras minúsculas
    clave_medio = [string.ascii_lowercase, string.digits]
   
   # Unir los caracteres en una sola cadena
    clave_medioUnion = ''.join(clave_medio)

    password = ""

    for i in range(nivel):
        # Agregar un caracter aleatorio de la cadena de caracteres permitidos
        password += secrets.choice(clave_medioUnion)

    
    password_box.config(state="normal")
    password_box.delete(0, "end") # Para borrar el contenido anterior
    password_box.insert(0, password)
    password_box.config(state="readonly") 


def nivel_alto(nivel):
    Messagebox.show_info("Nivel Alto", f"Se generará contraseña de {nivel} caracteres (letras, números y símbolos).")
    clave_alto = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    # Unir los caracteres en una sola cadena
    clave_altoUnion = ''.join(clave_alto)

    password = ""

    for i in range(nivel):
        # Agregar un caracter aleatorio de la cadena de caracteres permitidos
        password += secrets.choice(clave_altoUnion)

    password_box.config(state="normal")
    password_box.delete(0, "end") # Para borrar el contenido anterior
    password_box.insert(0, password)
    password_box.config(state="readonly") 

def copiar_password(password):

    if password_box.get() == "":
        Messagebox.show_warning("Advertencia", "No hay contraseña para copiar, selecciona un nivel de contraseña para generar una.") 
    else:
        root.clipboard_clear()
        root.clipboard_append(password)
        Messagebox.show_info("Copiado", "Contraseña copiada al portapapeles.")


root=ttk.Window(themename="darkly")
root.title("Password Generator")
root.geometry("300x400")



# Etiquetas
ttk.Label(root, text="Generador de Contraseñas").grid(row=0, column=0, columnspan=2, pady=10)
ttk.Label(root, text="Seleccciona el nivel de contraseña").grid(row=1, column=0, columnspan=2, pady=5)

#Botones
btn_nivelmedio = ttk.Button(root, text="Nivel medio", command=lambda: nivel_medio(8)) 
btn_nivelmedio.grid(row=3, column=0, padx=5, pady=5) 

btn_nivelalto = ttk.Button(root, text="Nivel alto", command=lambda: nivel_alto(12))
btn_nivelalto.grid(row=3, column=1, padx=5, pady=5)

password_box = ttk.Entry(root, width=30, state="readonly")
password_box.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

btn_copiar = ttk.Button(root, text="Copiar contraseña", command=lambda: copiar_password(password_box.get())) 
btn_copiar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)  


root.mainloop()

