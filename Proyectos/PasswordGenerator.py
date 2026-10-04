# Librerias
import tkinter as tk
from tkinter import messagebox

# librerias para generar contraseñas
import secrets
import string




def nivel_medio(nivel):
    messagebox.showinfo("Nivel Medio", f"Se generará contraseña de {nivel} caracteres (solo letras y numeros).") 

    # Generar una contraseña de nivel medio con numeros y letras minúsculas
    clave_medio = [string.ascii_lowercase, string.digits]
   
   # Unir los caracteres en una sola cadena
    clave_medioUnion = ''.join(clave_medio)

    password = ""

    for i in range(nivel):
        # Agregar un caracter aleatorio de la cadena de caracteres permitidos
        password += secrets.choice(clave_medioUnion)

    
    password_box.config(state="normal")
    password_box.delete(0, tk.END) # Para borrar el contenido anterior
    password_box.insert(0, password)
    password_box.config(state="readonly") 


def nivel_alto(nivel):
    messagebox.showinfo("Nivel Alto", f"Se generará contraseña de {nivel} caracteres (letras, números y símbolos).")
    clave_alto = [string.ascii_lowercase, string.ascii_uppercase, string.digits, string.punctuation]
    # Unir los caracteres en una sola cadena
    clave_altoUnion = ''.join(clave_alto)

    password = ""

    for i in range(nivel):
        # Agregar un caracter aleatorio de la cadena de caracteres permitidos
        password += secrets.choice(clave_altoUnion)

    password_box.config(state="normal")
    password_box.delete(0, tk.END) # Para borrar el contenido anterior
    password_box.insert(0, password)
    password_box.config(state="readonly") 

def copiar_password(password):

    if password_box.get() == "":
        messagebox.showwarning("Advertencia", "No hay contraseña para copiar, selecciona un nivel de contraseña para generar una.") 
    else:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copiado", "Contraseña copiada al portapapeles.")


root=tk.Tk()
root.title("Password Generator")
root.geometry("250x200")



# Etiquetas
tk.Label(root, text="Generador de Contraseñas").grid(row=0, column=0, columnspan=2, pady=10)
tk.Label(root, text="Seleccciona el nivel de contraseña").grid(row=1, column=0, columnspan=2, pady=5)

#Botones
btn_nivelmedio = tk.Button(root, text="Nivel medio", command=lambda: nivel_medio(8)) 
btn_nivelmedio.grid(row=3, column=0, padx=5, pady=5) 

btn_nivelalto = tk.Button(root, text="Nivel alto", command=lambda: nivel_alto(12))
btn_nivelalto.grid(row=3, column=1, padx=5, pady=5)

password_box = tk.Entry(root, width=30, state="readonly")
password_box.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

btn_copiar = tk.Button(root, text="Copiar contraseña", command=lambda: copiar_password(password_box.get())) 
btn_copiar.grid(row=5, column=0, columnspan=2, padx=5, pady=5)  


root.mainloop()

