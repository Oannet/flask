from alchemyClasses.usuarios import usuarios
from alchemyClasses import db

def crear_usuario(nombre, apPat, password, apMat=None, email=None, superUser=0):
    nuevo_usuario = usuarios(nombre=nombre, apPat=apPat, password=password, apMat=apMat, email=email, superUser=superUser)
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        return "Usuario creado exitosamente."
    except Exception as e:
        db.session.rollback()  # Asegura la integridad de la base de datos en caso de un fallo
        return f"Error al crear usuario: {e}"

def leer_usuarios():
    return usuarios.query.all()

def leer_usuario_por_id(id):
    return usuarios.query.get(id)

def actualizar_usuario(id, nombre=None, apPat=None, apMat=None, password=None, email=None, superUser=None):
    usuario = usuarios.query.get(id)
    if usuario:
        if nombre:
            usuario.nombre = nombre
        if apPat:
            usuario.apPat = apPat
        if apMat:
            usuario.apMat = apMat
        if password:
            usuario.password = password  # Considera cifrar la contraseña aquí si no lo has hecho aún
        if email:
            usuario.email = email
        if superUser is not None:
            usuario.superUser = superUser
        try:
            db.session.commit()
            return "Usuario actualizado exitosamente."
        except Exception as e:
            db.session.rollback()  # Asegura la integridad de la base de datos en caso de un fallo
            return f"Error al actualizar usuario: {e}"
    else:
        return "Usuario no encontrado."

def eliminar_usuario(id_usuario):
    try:
        usuario = leer_usuario_por_id(id_usuario)
        if usuario:
            db.session.delete(usuario)
            db.session.commit()
            return "Usuario eliminado exitosamente."
        else:
            return "Usuario no encontrado."
    except Exception as e:
        db.session.rollback()  # Asegura la integridad de la base de datos en caso de un fallo
        return f"Error al eliminar usuario: {e}"

def eliminar_todos_usuarios():
    try:
        num_rows_deleted = db.session.query(usuarios).delete()
        db.session.commit()
        if num_rows_deleted > 0:
            return "Todos los usuarios han sido eliminados exitosamente."
        else:
            return "No hay usuarios para eliminar."
    except Exception as e:
        db.session.rollback()  # Asegura la integridad de la base de datos en caso de un fallo
        return f"Error al eliminar todos los usuarios: {e}"
