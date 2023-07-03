from flask import Blueprint, render_template, request, flash, jsonify
from flask_login import login_required, current_user
from . import db
import json

views = Blueprint('views', __name__)

@views.route('/', methods=['GET', 'POST'])
@login_required
def home():
    return render_template("home.html", user=current_user)

@views.route('/digital', methods=['GET', 'POST'])
@login_required
def digital():
    if request.method == 'POST':
        note = request.form.get('digital')#Gets the note from the HTML
    return render_template("digital.html", user=current_user)

@views.route('/contabilidad', methods=['GET', 'POST'])
@login_required
def contabilidad():
    if request.method == 'POST':
        note = request.form.get('contabilidad')#Gets the note from the HTML
    return render_template("contabilidad.html", user=current_user)

@views.route('/config', methods=['GET', 'POST'])
@login_required
def config():
    if request.method == 'POST':
        note = request.form.get('config')#Gets the note from the HTML
    return render_template("config.html", user=current_user)

@views.route('/usuarios', methods=['GET', 'POST'])
@login_required
def usuarios():
    if request.method == 'POST':
        note = request.form.get('usuarios')#Gets the note from the HTML
    return render_template("usuarios.html", user=current_user)

@views.route('/notas', methods=['GET', 'POST'])
@login_required
def notas():
    if request.method == 'POST':
        note = request.form.get('notas')#Gets the note from the HTML
    return render_template("notas.html", user=current_user)

@views.route('/contacto', methods=['GET', 'POST'])
@login_required
def contacto():
    if request.method == 'POST':
        note = request.form.get('contacto')#Gets the note from the HTML
    return render_template("contacto.html", user=current_user)