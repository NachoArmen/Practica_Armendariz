import sqlite3

class Conexion:
    def __init__(self, escuela):
        self.conexion = sqlite3.connect("escuela.db")
        self.cursor = self.conexion.cursor()

    def crear_tabla(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS personas (
                matricula INTEGER(20),
                nombre VARCHAR(50),
                apellido VARCHAR(50)
            )
        ''')
        self.conexion.commit()

    def agregar_persona(self, persona):
        matricula= persona.matricula
        nombre= persona.nombre
        apellido= persona.apellido
        self.cursor.execute('''INSERT INTO personas(matricula, nombre, apellido) VALUES(?,?,?)''',
                            (matricula, nombre, apellido))
        self.conexion.commit()

    def modificar_persona(self, persona):
        matricula = persona.matricula
        nombre = persona.nombre
        apellido = persona.apellido
        self.cursor.execute('''UPDATE personas set nombre=?,apellido=? WHERE matricula=?''',
                            (nombre, apellido, matricula))
        self.conexion.commit()

    def eliminar_persona(self, persona):
        matricula = persona.matricula
        self.cursor.execute('''DELETE FROM personas WHERE matricula=?''', (matricula,))
        self.conexion.commit()

    def lista_personas(self):
        self.cursor.execute('''SELECT * FROM personas''')
        personas = self.cursor.fetchall()
        return personas

    def eliminar_tabla(self):
        pass

