from flask import Blueprint, request, render_template
from model.model_usuarios import UsuarioModel as UsuarioService

usuario_blueprint = Blueprint('usuario', __name__, url_prefix='/usuario')

@usuario_blueprint.route('/buscarUsuario', methods=['GET', 'POST'])
def buscar_usuario():
    if request.method == 'POST':
        usuario_id = request.form['userId']
        usuario = UsuarioService.obtener_por_id(usuario_id)
        if usuario:
            return render_template('detalleUsuario.html', usuario=usuario)
        else:
            mensaje = 'No se encontró el usuario con el ID proporcionado.'
            return render_template('mensaje.html', mensaje=mensaje)
    return render_template('listaUsuarios.html')

@usuario_blueprint.route('/borrar', methods=['GET', 'POST'])
def eliminar_usuario_por_id():
    if request.method == "GET":
        return render_template('eliminarUsuario.html')
    else:  # POST
        usuario_id = request.form['userId']
        resultado = UsuarioService.eliminar(usuario_id)
        mensaje = "Usuario borrado con éxito" if resultado == "Usuario eliminado exitosamente." else "Ha habido un error al intentar borrar"
        return render_template("mensaje.html", mensaje=mensaje)

@usuario_blueprint.route('/registro', methods=['GET', 'POST'])
def registrar_usuario():
    if request.method == 'POST':
        nombre = request.form['nombre']
        apellidoP = request.form['apPat']
        apellidoM = request.form['apMat']
        correo = request.form['email']
        password = request.form['password']
        superuser = request.form.get('superUser', 0)
        
        resultado = UsuarioService.crear(nombre, apellidoP, password, apellidoM, correo, superuser)
        if resultado == 'Usuario creado exitosamente.':
            mensaje = resultado
        else:
            mensaje = 'Error al crear el usuario.'
        return render_template('mensaje.html', mensaje=mensaje)
    return render_template('nuevoUsuario.html')

@usuario_blueprint.route('/leerUsuarios')
def listar_usuarios():
    usuarios = UsuarioService.obtener_todos()
    return render_template('todosUsuarios.html', usuarios=usuarios)

@usuario_blueprint.route('/actualizar', methods=['GET', 'POST'])  # Permitir GET y POST
def actualizar_usuario():
    if request.method == 'GET':
        return render_template('editarUsuario.html')  # Asegúrate de tener esta plantilla para capturar el ID del usuario a actualizar
    elif request.method == 'POST':
        usuario_id = request.form['userId']
        data = {key: request.form[key] for key in request.form if request.form[key]}
        resultado = UsuarioService.actualizar(usuario_id, **data)
        
        if resultado == 'Usuario actualizado exitosamente.':
            mensaje = resultado
        else:
            mensaje = 'Error al actualizar el usuario.'
        return render_template('mensaje.html', mensaje=mensaje)
