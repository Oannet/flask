from alchemyClasses.usuarios import usuarios
from alchemyClasses import db

class UsuarioModel:
    
    @staticmethod
    def crear(nombre, apPat, password, apMat=None, email=None, superUser=0):
        user = usuarios(nombre=nombre, apPat=apPat, password=password, apMat=apMat, email=email, superUser=superUser)
        try:
            db.session.add(user)
            db.session.commit()
            return "Usuario creado exitosamente."
        except Exception as e:
            db.session.rollback()
            return f"Error al crear usuario: {e}"
    
    @staticmethod
    def obtener_todos():
        return usuarios.query.all()
    
    @staticmethod
    def obtener_por_id(id_usuario):
        return usuarios.query.get(id_usuario)
    
    @staticmethod
    def actualizar(id_usuario, **kwargs):
        user = UsuarioModel.obtener_por_id(id_usuario)
        if user:
            for key, value in kwargs.items():
                if hasattr(user, key) and value is not None:
                    setattr(user, key, value)
            try:
                db.session.commit()
                return "Usuario actualizado exitosamente."
            except Exception as e:
                db.session.rollback()
                return f"Error al actualizar usuario: {e}"
        return "Usuario no encontrado."
    
    @staticmethod
    def eliminar(id_usuario):
        user = UsuarioModel.obtener_por_id(id_usuario)
        if user:
            try:
                db.session.delete(user)
                db.session.commit()
                return "Usuario eliminado exitosamente."
            except Exception as e:
                db.session.rollback()
                return f"Error al eliminar usuario: {e}"
        return "Usuario no encontrado."
    
    @staticmethod
    def eliminar_todos():
        try:
            num_rows_deleted = db.session.query(usuarios).delete()
            db.session.commit()
            return "Todos los usuarios han sido eliminados exitosamente." if num_rows_deleted > 0 else "No hay usuarios para eliminar."
        except Exception as e:
            db.session.rollback()
            return f"Error al eliminar todos los usuarios: {e}"