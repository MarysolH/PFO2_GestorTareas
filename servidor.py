from flask import Flask, request, jsonify, render_template_string
from werkzeug.security import generate_password_hash, check_password_hash
import db

app = Flask(__name__)
db.init_db()   # Inicializa la base de datos

# ----------- Registro de usuarios -----------
@app.route("/registro", methods=["POST"])
def registro():
    data = request.get_json()
    usuario = data.get("usuario")
    contrasena = data.get("contraseña")

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos"}), 400

    hash_pw = generate_password_hash(contrasena)

    try:
        db.add_user(usuario, hash_pw)
        return jsonify({"mensaje": "Usuario registrado con éxito"}), 201
    except Exception as e:
        return jsonify({"error": "El usuario ya existe o error en la BD"}), 409

# ----------- Inicio de sesión -----------
@app.route("/login", methods=["POST"])
def login():
    data = request.get_json()
    usuario = data.get("usuario")
    contrasena = data.get("contraseña")

    if not usuario or not contrasena:
        return jsonify({"error": "Faltan datos"}), 400

    row = db.get_user(usuario)

    if row and check_password_hash(row[0], contrasena):
        return jsonify({"mensaje": f"Bienvenido {usuario}"}), 200
    else:
        return jsonify({"error": "Credenciales inválidas"}), 401

# ----------- Página de tareas (HTML simple) -----------
@app.route("/tareas", methods=["GET"])
def tareas():
    html = """
    <html>
    <head><title>Tareas</title></head>
    <body>
        <h1>Bienvenido al gestor de tareas </h1>
        <p>Aquí podrás manejar tus pendientes.</p>
    </body>
    </html>
    """
    return render_template_string(html)

# ----------- Main -----------
if __name__ == "__main__":
    app.run(debug=True)