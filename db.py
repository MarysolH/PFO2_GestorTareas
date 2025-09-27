import sqlite3

DB_NAME = "database.db"

def init_db():
    
    """Crea la tabla de usuarios si no existe"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        usuario TEXT UNIQUE NOT NULL,
        contrasena TEXT NOT NULL
    )
    """)
    conn.commit()
    conn.close()

def add_user(usuario, hash_pw):

    """Agrega un nuevo usuario con contraseña hasheada"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO usuarios (usuario, contrasena) VALUES (?, ?)", (usuario, hash_pw))
    conn.commit()
    conn.close()

def get_user(usuario):

    """Obtiene la contraseña hasheada de un usuario"""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT contrasena FROM usuarios WHERE usuario = ?", (usuario,))
    row = cursor.fetchone()
    conn.close()
    return row