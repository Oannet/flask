from alchemyClasses.peliculas import peliculas
from alchemyClasses import db

def crear_pelicula(nombre, genero=None, duracion=None, inventario=1):
    nueva_pelicula = peliculas(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
    try:
        db.session.add(nueva_pelicula)
        db.session.commit()
        return 0
    except:
        return -1

def leer_peliculas():
    return peliculas.query.all()

# Función para obtener una película por su ID
def leer_pelicula_por_id(id):
    return peliculas.query.get(id)

# Función para actualizar una película por su ID
def actualizar_pelicula(id, nombre=None, genero=None, duracion=None, inventario=None):
    pelicula = peliculas.query.get(id)
    if pelicula is None:
        return -1
    else:
        if nombre:
            pelicula.nombre = nombre
        if genero:
            pelicula.genero = genero
        if duracion:
            pelicula.duracion = duracion
        if inventario:
            pelicula.inventario = inventario
        try:
            db.session.commit()
            return 0
        except:
            return -1


# Función para eliminar una película por su ID
def eliminar_pelicula(id):
    if not id:
        rentar.query.delete()
        peliculas.query.delete()
        db.session.commit()
        return 0
    else:
        pelicula = leer_pelicula_por_id(id)
        if pelicula is not None:
            db.session.delete(pelicula)
            db.session.commit()
            return 0
        else:
            return -1