from sqlalchemy import Column, Integer, String
from alchemyClasses import db

class peliculas(db.Model):
    __tablename__ ='peliculas'
    idPelicula = Column (Integer,nullable = False, primary_key = True, autoincrement=True)
    nombre = Column(String(200),nullable = False)
    genero = Column(String(45),nullable = True)
    duracion = Column(Integer,nullable = True)
    inventario = Column(Integer,nullable = False)

    def __init__(self, nombre, genero=None, duracion=None, inventario=1):
        self.nombre = nombre
        self.genero = genero
        self.duracion = duracion
        self.inventario = inventario

    def __str__(self):
        return f"ID: {self.idPelicula}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Genero: {self.genero}\n" \
               f"Duracion: {self.duracion} minutos\n" \
               f"Inventario: {self.inventario}\n"
               
