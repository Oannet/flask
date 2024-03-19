from flask import Blueprint, request, render_template, flash, url_for, redirect
from model import model_usuarios as mu

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/buscarUsuario', methods=['GET', 'POST'])
def mostrar_usuario_por_id():
    if request.method == "GET":
        return render_template('listaUsuarios.html')
    else:
        id = request.form["userId"]
        usuario = mu.leer_usuario_por_id(id)
        if usuario is not None:
            return render_template("detalleUsuario.html", usuario=usuario)
        else:
            return render_template("mensaje.html", mensaje="No existe usuario con dicho Id")

@usuario_blueprint.route('/borrar', methods=['GET', 'POST'])
def eliminar_usuario_por_id():
    if request.method == "GET":
        return render_template('eliminarUsuario.html')
    else:
        id = request.form["userId"]
        retorno = mu.eliminar_usuario(id)
        return render_template("mensaje.html", mensaje="Usuario borrado con éxito" if retorno == "Usuario eliminado exitosamente." else "Ha habido un error al intentar borrar")

@usuario_blueprint.route('/registro', methods=['GET', 'POST'])
def agregar_usuario():
    if request.method == "GET":
        return render_template('nuevoUsuario.html')
    else:
        nombre = request.form["nombre"]
        apellidoP = request.form["apPat"]
        apellidoM = request.form["apMat"]
        correo = request.form["email"]
        password = request.form["password"]
        superuser = request.form.get("superUser", 0)
        retorno = mu.crear_usuario(nombre, apellidoP, password, apellidoM, correo, superuser)
        return render_template("mensaje.html", mensaje="Usuario creado con éxito" if retorno == "Usuario creado exitosamente." else "error usuario no creado")

@usuario_blueprint.route('/leerUsuarios')
def mostrar_usuarios():
    usuarios = mu.leer_usuarios()
    return render_template("todosUsuarios.html", usuarios=usuarios)

@usuario_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_usuario():
    if request.method == "GET":
        return render_template('editarUsuario.html')
    else:
        id = request.form["userId"]
        nombre = request.form.get("nombre")
        apellidoP = request.form.get("apPat")
        apellidoM = request.form.get("apMat")
        correo = request.form.get("email")
        password = request.form.get("password")
        superuser = request.form.get("superUser")
        retorno = mu.actualizar_usuario(id, nombre, apellidoP, apellidoM, password, correo, superUser=superuser)
        return render_template("mensaje.html", mensaje="Usuario actualizado con éxito" if retorno == "Usuario actualizado exitosamente." else "Ha habido un error al querer actualizar")
