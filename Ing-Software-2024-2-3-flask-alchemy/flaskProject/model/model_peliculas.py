# model_peliculas.py
from alchemyClasses.peliculas import peliculas
from alchemyClasses import db

class PeliculaModel:

    @staticmethod
    def crear(nombre, genero, duracion, inventario):
        nueva_pelicula = peliculas(nombre=nombre, genero=genero, duracion=duracion, inventario=inventario)
        try:
            db.session.add(nueva_pelicula)
            db.session.commit()
            return "Película creada con éxito."
        except Exception as e:
            db.session.rollback()
            return f"Error al crear la película: {e}"

    @staticmethod
    def obtener_por_id(id):
        return peliculas.query.get(id)

    @staticmethod
    def obtener_todas():
        return peliculas.query.all()

    @staticmethod
    def actualizar(id, nombre=None, genero=None, duracion=None, inventario=None):
        pelicula = PeliculaModel.obtener_por_id(id)
        if pelicula:
            if nombre:
                pelicula.nombre = nombre
            if genero:
                pelicula.genero = genero
            if duracion:
                pelicula.duracion = duracion
            if inventario is not None:
                pelicula.inventario = inventario
            try:
                db.session.commit()
                return "Película actualizada con éxito."
            except Exception as e:
                db.session.rollback()
                return f"Error al actualizar la película: {e}"
        else:
            return "Película no encontrada."

    @staticmethod
    def eliminar(id):
        pelicula = PeliculaModel.obtener_por_id(id)
        if pelicula:
            try:
                db.session.delete(pelicula)
                db.session.commit()
                return "Película eliminada con éxito."
            except Exception as e:
                db.session.rollback()
                return f"Error al eliminar la película: {e}"
        else:
            return "Película no encontrada."
