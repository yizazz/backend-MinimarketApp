from flask import Blueprint, jsonify

my = Blueprint('my', __name__)

@my.route('/api/saludo')
def saludo():
    return jsonify({"mensaje": "Hola desde Flask (rutas separadas)!"})

