import unittest
from Persona import Persona
from Conexion import Conexion

class TestPersona(unittest.TestCase):

    def setUp(self):
        self.db = Conexion('escuela.db')
        self.db.crear_tabla()

    def tearDown(self):
        # Limpiar la DB después de cada test
        self.db.eliminar_tabla()

    def test_agregar_persona(self):
        p = Persona('2023', 'Ignacito', 'Armendariz')
        self.db.agregar_persona(p)

        personas = self.db.lista_personas()
        self.assertEqual(len(personas), 2)
        self.assertEqual(personas[0][1], 'Ignacito')

    def test_modificar_persona(self):
        p = Persona('2023', 'Ignacito', 'Armendariz')
        self.db.agregar_persona(p)

        p2= Persona('2023', 'Ignacito', 'Armendariz')
        self.db.modificar_persona(p2)

        personas = self.db.lista_personas()
        self.assertEqual(personas[0][1], 'Ignacito')

    def test_eliminar_persona(self):
        p = Persona('2023', 'Ignacito', 'Armendariz')
        self.db.agregar_persona(p)

        self.db.eliminar_persona(p)

        personas= self.db.lista_personas()
        self.assertEqual(len(personas),0)

if __name__ == '__main__':
    unittest.main()