from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    lista = ['views.contabilidad', 'views.notas', 'views.contacto']
    #list.append('contabilidad')
    #list.append('notas')
    #print(lista)
    context = {'lista':lista, 'user':current_user}
    return render_template("home.html", **context)

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