from flask import Flask, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
import os
from Routes.Routes import my

app = Flask(__name__)
CORS(app)

app.register_blueprint(my)

app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///data.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Modelos
class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Float, nullable=False)
    stock = db.Column(db.Integer, default=0)

    def serialize(self):
        return {"id": self.id, "name": self.name, "price": self.price, "stock": self.stock}

# Rutas
@app.route('/')
def home():
    return jsonify({"message": "Backend funcionando correctamente"})
  

@app.route('/products')
def get_products():
    products = Product.query.all()
    return jsonify([p.serialize() for p in products])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(host='0.0.0.0', port=5000, debug=True)
