import sqlite3

# Nombre del archivo de base de datos
DATABASE = 'profiles.db'

# Conectar y crear la base de datos
conn = sqlite3.connect(DATABASE)
cursor = conn.cursor()

# Crear la tabla de profesores
cursor.execute('''
    CREATE TABLE IF NOT EXISTS profesores (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre TEXT NOT NULL,
        especializacion TEXT,
        experiencia TEXT,
        proyectos TEXT,
        publicaciones TEXT,
        linkedin TEXT
    )
''')

# Datos de ejemplo para poblar la tabla
profesores_data = [
    ("Ana Gómez", "Ingeniería", "5 años en sector privado", "Proyecto A, Proyecto B", "Publicación 1", "https://linkedin.com/in/anagomez"),
    ("Juan Pérez", "Ciencias Sociales", "3 años en cooperación internacional", "Proyecto C", "Publicación 2", "https://linkedin.com/in/juanperez"),
    ("María López", "Biotecnología", "Investigación aplicada en biotecnología", "Proyecto D, Proyecto E", "Publicación 3", "https://linkedin.com/in/marialopez"),
    ("Carlos Ruiz", "Matemáticas", "Consultoría en análisis de datos", "Proyecto F", "Publicación 4", "https://linkedin.com/in/carlosruiz"),
    ("Luis Torres", "Economía", "Sector público y privado", "Proyecto G, Proyecto H", "Publicación 5", "https://linkedin.com/in/luistorres")
]

# Insertar datos de ejemplo en la tabla profesores
cursor.executemany('''
    INSERT INTO profesores (nombre, especializacion, experiencia, proyectos, publicaciones, linkedin)
    VALUES (?, ?, ?, ?, ?, ?)
''', profesores_data)

# Confirmar los cambios y cerrar la conexión
conn.commit()
conn.close()

print("Base de datos creada y poblada con datos de ejemplo.")
