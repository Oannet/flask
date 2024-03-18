from sqlalchemy import Column, Integer, DateTime, SmallInteger, ForeignKey, CheckConstraint 
from alchemyClasses import db

class rentar(db.Model):
    
    __tablename__ = 'rentar'
    idRentar = Column(Integer, primary_key=True)
    idUsuario = Column(Integer, ForeignKey('usuarios.idUsuario'), nullable=False)
    idPelicula = Column(Integer, ForeignKey('peliculas.idPelicula'), nullable=False)
    fecha_renta = Column(DateTime, nullable=False)
    dias_de_renta = Column(Integer, nullable=True)
    estatus = Column(Integer, CheckConstraint('duracion IN (0, 1)'), nullable=True)
    users = db.relationship("usuarios", backref=db.backref("rentasu", cascade="all, delete-orphan"))
    pelis = db.relationship("peliculas", backref=db.backref("rentasp", cascade="all, delete-orphan"))
    
    def __init__(self, idUsuario, idPelicula, fecha_renta, dias_de_renta=5, estatus=0):
        self.idUsuario = idUsuario
        self.idPelicula = idPelicula
        self.fecha_renta = fecha_renta
        self.dias_de_renta = dias_de_renta
        self.estatus = estatus
        
    def __str__(self):
        return f"ID Renta: {self.idRentar}\n" \
               f"ID Usuario: {self.idUsuario}\n" \
               f"ID Pelicula: {self.idPelicula}\n" \
               f"Fecha Renta: {self.fecha_renta}\n" \
               f"Dias de renta: {self.dias_de_renta}\n" \
               f"Estatus: {self.estatus}\n" 
               
