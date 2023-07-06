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
        return 'https://static.vecteezy.com/system/resources/previews/010/925/499/non_2x/balance-sheet-cartoon-web-icon-accounting-process-finance-analyst-calculating-tools-financial-consulting-idea-bookkeeping-service-flat-design-modern-illustration-vector.jpg'
    elif elemento == 'views.notas':
        return 'https://www.chipax.com/wp-content/uploads/2022/04/nota-de-credito.png'
    elif elemento == 'views.contacto':
        return 'https://media.istockphoto.com/id/1268586504/es/vector/icono-de-contacto-para-computadora-sitio-web-y-aplicaciones-m%C3%B3viles.jpg?s=170667a&w=0&k=20&c=cX0NjxacOgyJYLudCjh9RnckQM5Cb_-k47t-6LLQUy0='
    elif elemento == 'views.usuarios':
        return 'https://cdn.icon-icons.com/icons2/272/PNG/512/Contacts_30028.png'
    elif elemento == 'views.config':
        return 'https://tumovilseguro.unam.mx/pluginfile.php/60/course/section/8/configuracion.png'
    elif elemento == 'views.digital':
        return 'https://www.muycomputerpro.com/wp-content/uploads/2017/05/digitalizacion-1.jpg'
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