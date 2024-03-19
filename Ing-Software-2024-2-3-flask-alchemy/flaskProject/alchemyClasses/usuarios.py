from sqlalchemy import Column, Integer, String, LargeBinary, CheckConstraint 
from alchemyClasses import db

class usuarios(db.Model):
    __tablename__ ='usuarios'
    idUsuario = Column (Integer,nullable = False, primary_key = True, autoincrement=True)
    nombre = Column(String(255))
    apPat = Column(String(200), nullable = False)
    apMat = Column(String(200), nullable = True)
    password = Column(String(64))
    email =  Column(String(255), nullable=True, unique=True) 
    profilePicture = Column(LargeBinary, nullable=True)
    superUser = Column(Integer, nullable=True) 
    
    def __init__(self, nombre, apPat, password, apMat=None, email=None, profilePicture=None, superUser=None):
        self.nombre = nombre
        self.apPat = apPat
        self.apMat = apMat
        self.password = password  
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

    def __str__(self):
        return f"ID: {self.idUsuario}\n" \
               f"Nombre: {self.nombre}\n" \
               f"Apellido Paterno: {self.apPat}\n" \
               f"Apellido Materno: {self.apMat}\n" \
               f"Contraseña: {self.password}\n" \
               f"Email: {self.email}\n" \
               f"Imagen de perfil: {self.profilePicture}\n" \
               f"Superusuario: {self.superUser}\n"