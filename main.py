import tkinter as tk
from tkinter import ttk
import sqlite3
from Conexion import Conexion
from Persona import Persona


#Inicializamos DB y tkinter
db = Conexion("escuela.db")
db.crear_tabla()
root = tk.Tk()
root.title("Admin Personas")

# Ponemos el layout mas bonito
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

header_frame = ttk.Frame(root)
header_frame.grid(column=0, row=0, sticky='ew')

header_label = ttk.Label(header_frame, text='Ingresa tus datos', font=('Segoe UI', 18))
header_label.pack()

content_frame = ttk.Frame(root)
content_frame.grid(column=0, row=1, sticky='nsew', padx=20, pady=20)

#Agregamos estilo
style = ttk.Style()
style.theme_use('winnative')
style.configure('TButton', padding=10, relief='flat', background='#0078D4')
style.configure('TLabel', foreground='white', background='#0078D4')




#Creamos el layout del programa
tree_frame = tk.Frame(root)
tree_frame.grid(pady=20)
label_frame= tk.Frame(root)
label_frame.grid(pady=10)
input_frame = tk.Frame(root)
input_frame.grid(pady=20)
buttons_frame = tk.Frame(root)
buttons_frame.grid(pady=20)





# Agregamos Inputs Y labels
label_matricula= tk.Label(label_frame, text="Matricula: ")
label_matricula.grid(row=0, column=0, padx=5, pady=5)
input_matricula = tk.Entry(input_frame)
input_matricula.grid(row=0, column=0, padx=5, pady=5)

label_nombre= tk.Label(label_frame, text="Nombre: ")
label_nombre.grid(row=0, column=1, padx=100, pady=5)
input_nombre = tk.Entry(input_frame)
input_nombre.grid(row=0, column=1, padx=5, pady=5)

label_apellido= tk.Label(label_frame, text="Apellido: ")
label_apellido.grid(row=0, column=2, padx=5, pady=5)
input_apellido = tk.Entry(input_frame)
input_apellido.grid(row=0, column=2, padx=5, pady=5)


#Creamos funciones para llamar a DB y administrar
def agregar():
    matricula= input_matricula.get()
    nombre= input_nombre.get()
    apellido= input_apellido.get()

    persona= Persona(matricula,nombre,apellido)

    db.agregar_persona(persona)

    ver()

def mod():
    matricula = input_matricula.get()
    nombre = input_nombre.get()
    apellido = input_apellido.get()

    persona = Persona(matricula, nombre, apellido)

    db.modificar_persona(persona)

    ver()

def borrar():
    matricula= input_matricula.get()

    persona= Persona(matricula,None,None)

    db.eliminar_persona(persona)

    ver()

def ver():
    personas= db.lista_personas()

    tree.delete(*tree.get_children())

    for persona in personas:
        tree.insert('', 'end', values=(persona[0],persona[1],persona[2]))


# Inicializamos la ventana donde se veran los datos
tree = ttk.Treeview(tree_frame)
tree["columns"] = ("Matricula", "Nombre", "Apellido")
tree.column("Matricula", width=120)
tree.column("Nombre", width=120)
tree.column("Apellido", width=120)
tree.heading("Matricula", text="Matricula")
tree.heading("Nombre", text="Nombre")
tree.heading("Apellido", text="Apellido")
tree.pack()


# Agregamos botones
btn_create = ttk.Button(buttons_frame, text="Agregar", command=agregar)
btn_read = ttk.Button(buttons_frame, text="Lista", command=ver)
btn_update = ttk.Button(buttons_frame, text="Modificar", command=mod)
btn_delete = ttk.Button(buttons_frame, text="Eliminar", command=borrar)

btn_create.grid(row=0, column=1, padx=5, pady=5)
btn_read.grid(row=0, column=0, padx=5, pady=5)
btn_update.grid(row=0, column=2, padx=5, pady=5)
btn_delete.grid(row=0, column=3, padx=5, pady=5)


#Logica para habilitar y deshabilitar botones
def check_campos():
  matricula = input_matricula.get()
  nombre = input_nombre.get()
  apellido = input_apellido.get()

  if matricula:
      btn_delete.config(state="normal")
  else:
      btn_delete.config(state="disabled")

  if matricula and nombre and apellido:
      btn_create.config(state="normal")
      btn_update.config(state="normal")
  else:
      btn_create.config(state="disabled")
      btn_update.config(state="disabled")

check_campos()

input_matricula.bind("<KeyRelease>", lambda event: check_campos())
input_nombre.bind("<KeyRelease>", lambda event: check_campos())
input_apellido.bind("<KeyRelease>", lambda event: check_campos())



#Iniciamos el programa
root.mainloop()


