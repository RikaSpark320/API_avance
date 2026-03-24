from main import db, app

def insertar_juego(nombre, descripcion, precio):
    with app.app_context():
        from models import Juego
        nuevo_juego = Juego(nombre, descripcion, precio)
        db.session.add(nuevo_juego)
        db.session.commit()

def obtener_juegos():
    with app.app_context():
        from models import Juego
        return Juego.query.all()

def obtener_juego_por_id(id):
    with app.app_context():
        from models import Juego
        return Juego.query.get(id)

def actualizar_juego(id, nombre, descripcion, precio):
    with app.app_context():
        from models import Juego
        juego = Juego.query.get(id)
        if juego:
            juego.nombre = nombre
            juego.descripcion = descripcion
            juego.precio = precio
            db.session.commit()

def eliminar_juego(id):
    with app.app_context():
        from models import Juego
        juego = Juego.query.get(id)
        if juego:
            db.session.delete(juego)
            db.session.commit()