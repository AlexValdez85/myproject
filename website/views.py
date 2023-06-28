from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from .models import User
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])

def home():
    return render_template("home.html")

@views.route('/index', methods=['GET', 'POST'])

def index():
    return render_template("index.html")

@views.route('/digital', methods=['GET', 'POST'])

def digital():
    if request.method == 'POST':
        note = request.form.get('digital')#Gets the note from the HTML
    return render_template("digital.html")

@views.route('/contabilidad', methods=['GET', 'POST'])

def contabilidad():
    if request.method == 'POST':
        note = request.form.get('contabilidad')#Gets the note from the HTML
    return render_template("contabilidad.html")

@views.route('/config', methods=['GET', 'POST'])

def config():
    if request.method == 'POST':
        note = request.form.get('config')#Gets the note from the HTML
    return render_template("config.html")

@views.route('/usuarios', methods=['GET', 'POST'])

def usuarios():
    if request.method == 'POST':
        note = request.form.get('usuarios')#Gets the note from the HTML
    return render_template("usuarios.html")

@views.route('/notas', methods=['GET', 'POST'])

def notas():
    if request.method == 'POST':
        note = request.form.get('notas')#Gets the note from the HTML
    return render_template("notas.html")

@views.route('/contacto', methods=['GET', 'POST'])
@login_required
def contacto():
    if request.method == 'POST':
        note = request.form.get('contacto')#Gets the note from the HTML
    return render_template("contacto.html")