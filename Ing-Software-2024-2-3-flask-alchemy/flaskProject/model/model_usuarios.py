from alchemyClasses.usuarios import usuarios
from alchemyClasses import db

def crear_usuario(nombre, apPat, password, apMat=None, email=None, superUser=0):
    nuevo_usuario = usuarios(nombre=nombre, apPat=apPat, password=password, apMat=apMat, email=email, superUser=superUser)
    try:
        db.session.add(nuevo_usuario)
        db.session.commit()
        return "Usuario creado exitosamente."
    except Exception as e:
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
            usuario.password = password
        if email:
            usuario.email = email
        if superUser is not None:
            usuario.superUser = superUser
        try:
            db.session.commit()
            return "Usuario actualizado exitosamente."
        except Exception as e:
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
        return f"Error al eliminar usuario: {e}"
