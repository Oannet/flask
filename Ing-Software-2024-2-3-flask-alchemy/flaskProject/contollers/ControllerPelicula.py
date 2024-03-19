# ControllerPelicula.py
from flask import Blueprint, request, render_template
from model.model_peliculas import PeliculaModel as PeliculaService

pelicula_blueprint = Blueprint('pelicula', __name__, url_prefix='/pelicula')

@pelicula_blueprint.route('/buscarPelicula', methods=['GET', 'POST'])
def buscar_pelicula():
    if request.method == 'POST':
        pelicula_id = request.form['peliculaId']
        pelicula = PeliculaService.obtener_por_id(pelicula_id)
        if pelicula:
            return render_template('mostrar_pelicula.html', pelicula=pelicula)
        else:
            mensaje = 'No se encontró la película con el ID proporcionado.'
            return render_template('mensaje.html', mensaje=mensaje)
    return render_template('leer_peliculas.html')

@pelicula_blueprint.route('/borrar', methods=['GET', 'POST'])
def eliminar_pelicula_por_id():
    if request.method == "GET":
        return render_template('borrar_peliculas.html')
    else:  # POST
        pelicula_id = request.form['peliculaId']
        resultado = PeliculaService.eliminar(pelicula_id)
        mensaje = resultado
        return render_template("mensaje.html", mensaje=mensaje)

@pelicula_blueprint.route('/registro', methods=['GET', 'POST'])
def registrar_pelicula():
    if request.method == 'POST':
        nombre = request.form['nombre']
        genero = request.form['genero']
        duracion = request.form['duracion']
        inventario = request.form['inventario']
        
        resultado = PeliculaService.crear(nombre, genero, duracion, inventario)
        mensaje = resultado
        return render_template('mensaje.html', mensaje=mensaje)
    return render_template('crear_pelicula.html')

@pelicula_blueprint.route('/leerPeliculas')
def listar_peliculas():
    peliculas = PeliculaService.obtener_todas()
    return render_template('mostrar_peliculas.html', peliculas=peliculas)

@pelicula_blueprint.route('/actualizar', methods=['GET', 'POST'])
def actualizar_pelicula():
    if request.method == 'GET':
        return render_template('actualizar_pelicula.html')
    else:  # POST
        pelicula_id = request.form.get('peliculaId')
        # Prepara los datos excluyendo 'peliculaId' para evitar el error
        data = {key: request.form[key] for key in request.form if key != 'peliculaId' and request.form[key]}

        # Llama al método de actualización pasando el ID de la película y los datos desempaquetados
        resultado = PeliculaService.actualizar(pelicula_id, **data)

        if resultado == 'Película actualizada con éxito.':
            mensaje = resultado
        else:
            mensaje = 'Error al actualizar la película.'
        return render_template('mensaje.html', mensaje=mensaje)
