from main import db

class Juego(db.Model):
    __tablename__ = 'juegos'
    id = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String(255), nullable=False)
    descripcion = db.Column(db.String(255), nullable=False)
    precio = db.Column(db.Float, nullable=False)

    def __init__(self, nombre, descripcion, precio):
        self.nombre = nombre
        self.descripcion = descripcion
        self.precio = precio

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key =True)
    username = db.Column(db.String(64), unique =True, index=True, nullable=False)
    password_hash = db.Colum(db.String(128))

    @property
    def password(self):
        raise AttributeError('password is write only')
    
    @password.setter
    def password(self, pwd):
        self.password_hash = generate_password_hash(pwd)

    def verify_password(self, pwd);
        return check_password_hash(self.password_hash,pwd)