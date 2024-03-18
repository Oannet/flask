from Cryptodome.Hash import SHA256
from base64 import b64encode
from sqlalchemy import Column, Integer, String, LargeBinary, CheckConstraint 
from alchemyClasses import db



class usuarios(db.Model):
    __tablename__ ='usuarios'
    idUsuario = Column (Integer,nullable = False, primary_key = True, autoincrement=True)
    nombre = Column(String(200), nullable = False, autoincrement = True)
    apPat = Column(String(200), nullable = False)
    apMat = Column(String(200), nullable = True)
    password = Column(String(45), nullable = False)
    email = Column(String(500), nullable = False)
    profilePicture = Column(LargeBinary, nullable=True)
    superUser = Column(Integer, CheckConstraint('duracion IN (0, 1)'), nullable=True) 
    
    def cifrar_password(self, password):
    # Creamos un objeto de hash SHA-256
	    hash_obj = SHA256.new()

	    # Convertimos la contraseña a bytes y actualizamos el hash
	    hash_obj.update(password.encode('utf-8'))

	    # Obtenemos el hash en formato de bytes
	    password_hash = hash_obj.digest()

	    # Convertimos el hash a una cadena Base64 para almacenarlo de forma segura
	    return b64encode(password_hash).decode('utf-8')

   
    def __init__(self, nombre, apPat, password, apMat=None, email=None, profilePicture=None, superUser=None):
            self.nombre = nombre
            self.apPat = apPat
            self.apMat = apMat
            self.password = self.cifrar_password(password)
            self.email = email
            self.profilePicture = profilePicture
            self.superUser = superUser




    def __str__(self):
        return f"ID: {self.idUsuario}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Apellido Paterno: {self.apPat}\n" \
               f"Apellido Materno: {self.apMat}\n" \
               f"Contraseña: {self.password}\n" \
               f"Email: {self.email}\n" \
               f"Imagen de perfil: {self.profilePicture}\n" \
               f"Superusuario: {self.superUser}\n"
