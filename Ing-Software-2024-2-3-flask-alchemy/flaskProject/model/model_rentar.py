from alchemyClasses.rentar import rentar
from alchemyClasses import db

# Función para crear un registro de renta
def crear_renta(idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=0):
    nueva_renta = rentar(idUsuario=idUsuario, idPelicula=idPelicula, fecha_renta=fecha_renta, dias_de_renta=dias_de_renta, estatus=estatus)
    db.session.add(nueva_renta)
    db.session.commit()
    return nueva_renta

# Función para obtener todas las rentas
def leer_rentas():
    return rentar.query.all()

# Función para obtener una renta por su ID
def leer_renta_por_id(id):
    return rentar.query.get(id)

# Función para actualizar una renta por su ID
def actualizar_renta(id, idUsuario=None, idPelicula=None, fecha_renta=None, dias_de_renta=None, estatus=None):
    renta = rentar.query.get(id)
    if idUsuario:
        renta.idUsuario = idUsuario
    if idPelicula:
        renta.idPelicula = idPelicula
    if fecha_renta:
        renta.fecha_renta = fecha_renta
    if dias_de_renta:
        renta.dias_de_renta = dias_de_renta
    if estatus is not None:
        renta.estatus = estatus
    db.session.commit()
    return renta

