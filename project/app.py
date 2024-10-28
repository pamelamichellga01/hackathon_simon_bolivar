from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# Configuración de la base de datos
DATABASE = 'profiles.db'

# Función para conectarse a la base de datos
def connect_db():
    try:
        conn = sqlite3.connect(DATABASE)
        return conn
    except Exception as e:
        print(f"Error al conectar con la base de datos: {e}")

# Ruta principal para mostrar todos los perfiles
@app.route('/')
def index():
    try:
        conn = connect_db()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM profesores")
        perfiles = cursor.fetchall()
        conn.close()
        return render_template('view_profiles.html', perfiles=perfiles)
    except Exception as e:
        print(f"Error en la ruta principal: {e}")
        return "Error al cargar la página principal."

# Ruta para crear un perfil
@app.route('/create', methods=['GET', 'POST'])
def create_profile():
    if request.method == 'POST':
        nombre = request.form['nombre']
        especializacion = request.form['especializacion']
        experiencia = request.form['experiencia']
        proyectos = request.form['proyectos']
        publicaciones = request.form['publicaciones']
        linkedin = request.form['linkedin']
        
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute('''INSERT INTO profesores (nombre, especializacion, experiencia, proyectos, publicaciones, linkedin)
                              VALUES (?, ?, ?, ?, ?, ?)''', (nombre, especializacion, experiencia, proyectos, publicaciones, linkedin))
            conn.commit()
            conn.close()
            return redirect(url_for('index'))
        except Exception as e:
            print(f"Error al crear perfil: {e}")
            return "Error al guardar el perfil."
    
    return render_template('create_profile.html')

# Ruta para buscar perfiles
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        query = request.form['query']
        try:
            conn = connect_db()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM profesores WHERE especializacion LIKE ?", ('%' + query + '%',))
            resultados = cursor.fetchall()
            conn.close()
            return render_template('search.html', perfiles=resultados)
        except Exception as e:
            print(f"Error en la búsqueda: {e}")
            return "Error al realizar la búsqueda."
    
    return render_template('search.html', perfiles=[])

# Ruta para comparar perfiles
@app.route('/compare', methods=['POST'])
def compare():
    selected_profiles = request.form.getlist('profile')
    try:
        conn = connect_db()
        cursor = conn.cursor()
        query = f"SELECT * FROM profesores WHERE id IN ({','.join(['?']*len(selected_profiles))})"
        cursor.execute(query, selected_profiles)
        perfiles_comparar = cursor.fetchall()
        conn.close()
        return render_template('compare.html', perfiles=perfiles_comparar)
    except Exception as e:
        print(f"Error al comparar perfiles: {e}")
        return "Error al comparar perfiles."

if __name__ == '__main__':
    app.run(debug=True)
