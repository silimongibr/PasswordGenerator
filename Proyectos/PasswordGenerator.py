# Librerias
#import tkinter as tk
#from tkinter import messagebox


#librerias para mejorar la interfaz
import ttkbootstrap as ttk
from ttkbootstrap.dialogs import Messagebox



# librerias para generar contraseñas
import secrets
import string


#Version 1.0 (primer prototipo) de generador de contraseñas con interfaz grafica, que permite generar contraseñas de nivel medio y alto, con la posibilidad de copiar la contraseña generada al portapapeles.
'''
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
    clave_alto = [string.ascii_lowercase, string.ascii_uppercase, string.digits, "!@#$%^&*()_+-=[]{}|;:,.<>?/"]

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
'''

def generar_password():
    # Obtener la longitud de la contraseña seleccionada
    longitud = int(longitud_box.get())

    # Crear una lista de grupos de caracteres según las opciones seleccionadas
    grupos = []
    if mayusculas_var.get():
        grupos.append(string.ascii_uppercase)
    if minusculas_var.get():
        grupos.append(string.ascii_lowercase)
    if numeros_var.get():
        grupos.append(string.digits)
    if simbolos_var.get():
        grupos.append("!@#$%^&*()_+-=[]{}|;:,.<>?/")

    if not grupos:  
        Messagebox.show_warning("Selecciona al menos un tipo de carácter para generar la contraseña.", "Advertencia") 
        return

    password = ""
    for i in range(longitud):
        # Agregar un caracter aleatorio de la cadena de caracteres permitidos
        password += secrets.choice("".join(grupos))


    password_box.config(state="normal")
    password_box.delete(0, "end") # Para borrar el contenido anterior
    password_box.insert(0, password)
    password_box.config(state="readonly")




def copiar_password(password):

    if password_box.get() == "":
        Messagebox.show_warning("No hay contraseña para copiar, selecciona un nivel de contraseña para generar una.","Advertencia") 
    else:
        root.clipboard_clear()
        root.clipboard_append(password)
        Messagebox.show_info("Contraseña copiada al portapapeles.", "Copiado")


root=ttk.Window(themename="darkly")
root.title("Password Generator")
root.geometry("300x400")



# Etiquetas
ttk.Label(root, text="Generador de Contraseñas").grid(row=0, column=0, columnspan=2, pady=10)
ttk.Label(root, text="Seleccciona la longitud de la contraseña").grid(row=1, column=0, columnspan=2, pady=5)

# Entrada para la longitud de la contraseña
longitud_box = ttk.Combobox(root, values=list(range(8, 17)), state="readonly", width=10)
longitud_box.grid(row=2, column=0, columnspan=2, padx=5, pady=5)
longitud_box.set(8)  # Valor por defecto


#Casillas seleccionables para tipo de caracteres
#Creacion de variables para los checkbuttons
mayusculas_var = ttk.BooleanVar(value=False)
minusculas_var = ttk.BooleanVar(value=False)
numeros_var = ttk.BooleanVar(value=False)
simbolos_var = ttk.BooleanVar(value=False)

#Labels para los checkbuttons
ttk.Label(root, text="Selecciona el tipo de caracteres:").grid(row=3, column=0, columnspan=2, pady=10)

#Checkbuttons para seleccionar los tipos de caracteres con la funcion generar_password() como comando para generar la contraseña al seleccionar una opcion
ttk.Checkbutton(root, text="Letras mayúsculas (A-Z)", variable=mayusculas_var,command=generar_password).grid(row=4, column=0, sticky="w", padx=5)
ttk.Checkbutton(root, text="Letras minúsculas (a-z)", variable=minusculas_var,command=generar_password).grid(row=5, column=0, sticky="w", padx=5)
ttk.Checkbutton(root, text="Números (0-9)", variable=numeros_var,command=generar_password).grid(row=6, column=0, sticky="w", padx=5)
ttk.Checkbutton(root, text="Símbolos (!@#$%^&*)", variable=simbolos_var,command=generar_password).grid(row=7, column=0, sticky="w", padx=5)




#Botones
#btn_nivelmedio = ttk.Button(root, text="Nivel medio", command=lambda: nivel_medio(int(longitud_box.get()))) 
#btn_nivelmedio.grid(row=3, column=0, padx=5, pady=5) 

#btn_nivelalto = ttk.Button(root, text="Nivel alto", command=lambda: nivel_alto(int(longitud_box.get())))
#btn_nivelalto.grid(row=3, column=1, padx=5, pady=5)

password_box = ttk.Entry(root, width=30, state="readonly")
password_box.grid(row=9, column=0, columnspan=2, padx=5, pady=5)

btn_copiar = ttk.Button(root, text="Copiar contraseña", command=lambda: copiar_password(password_box.get())) 
btn_copiar.grid(row=10, column=0, columnspan=2, padx=5, pady=5)  


root.mainloop()

