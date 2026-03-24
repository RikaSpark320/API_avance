from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, login_required
from werkzeug.security import generate_password_hash, check_password_hash

login_manager = LoginManager(main)
login_manager.login_view = 'auth.login'
login_manager.session_protection ='strong'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

# Importar y registrar blueprints
from auth import auth as auth_blueprint
app.register_blueprint(auth_blueprint, url_prefix='/auth')

from api.routes import api_blueprint
app.register_blueprint(api_blueprint, url_prefix='/api')



app = Flask(__name__)
app.config['SECRET_KEY'] = 'hola123.'
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:@localhost/juegos'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

import controlador_juegos

@app.route("/")
@app.route("/juegos")
def juegos():
    juegos = controlador_juegos.obtener_juegos()
    return render_template("juegos.html", juegos=juegos)

@app.route("/agregar_juego")
@login_required
def formulario_agregar_juego():
    return render_template("agregar_juego.html")


@app.route("/guardar_juego", methods=["POST"])
@login_required
def guardar_juego():
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_juegos.insertar_juego(nombre, descripcion, precio)
    return redirect("/juegos")

@app.route("/eliminar_juego", methods=["POST"])
@login_required
def eliminar_juego():
    controlador_juegos.eliminar_juego(request.form["id"])
    return redirect("/juegos")

@app.route("/formulario_editar_juego/<int:id>")
@login_required
def editar_juego(id):
    juego = controlador_juegos.obtener_juego_por_id(id)
    return render_template("editar_juego.html", juego=juego)

@app.route("/actualizar_juego", methods=["POST"])
@login_required
def actualizar_juego():
    id = request.form["id"]
    nombre = request.form["nombre"]
    descripcion = request.form["descripcion"]
    precio = request.form["precio"]
    controlador_juegos.actualizar_juego(id, nombre, descripcion, precio)
    return redirect("/juegos")

app.register.blueprint(auth_blueprint, url_prefix ='/auth')

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8000, debug=True)