from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    lista = ['views.contabilidad', 'views.notas', 'views.contacto', 'views.usuarios', 'views.config', 'views.digital']
    context = {'lista':lista, 'user':current_user}
    columnas_ordenadas = [lista[i:i+2] for i in range(0, len(lista), 2)] 
    context['lista'] = columnas_ordenadas
    return render_template("home.html", lista=columnas_ordenadas, user=current_user)

def obtener_imagen(elemento):
    # Lógica para obtener la imagen según el elemento
    if elemento == 'views.contabilidad':
        return '/static/imagenes/contabilidad.png'
    elif elemento == 'views.notas':
        return '/static/imagenes/nota-de-credito.png'
    elif elemento == 'views.contacto':
        return '/static/imagenes/contacto.jpg'
    elif elemento == 'views.usuarios':
        return '/static/imagenes/usuarios.png'
    elif elemento == 'views.config':
        return '/static/imagenes/config.png'
    elif elemento == 'views.digital':
        return '/static/imagenes/digital.jpg'
    else:
        return 'ruta/imagen_predeterminada.jpg'

@views.route('/digital', methods=['GET', 'POST'])
@login_required
def digital():
    return render_template("digital.html", user=current_user)

@views.route('/contabilidad', methods=['GET', 'POST'])
@login_required
def contabilidad():
    return render_template("contabilidad.html", user=current_user)

@views.route('/config', methods=['GET', 'POST'])
@login_required
def config():
    return render_template("config.html", user=current_user)

@views.route('/usuarios', methods=['GET', 'POST'])
@login_required
def usuarios():
    return render_template("usuarios.html", user=current_user)

@views.route('/notas', methods=['GET', 'POST'])
@login_required
def notas():
    return render_template("notas.html", user=current_user)

@views.route('/contacto', methods=['GET', 'POST'])
@login_required
def contacto():
    return render_template("contacto.html", user=current_user)