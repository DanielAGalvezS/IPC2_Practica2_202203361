from flask import Flask, render_template, request, jsonify

#Nota para el futuro, intenta ejecutarlo en vsc, en caso que no te permita y la terminal sea un windowsPowerShell/v0.1 y diga tipo no flask
#debes seguir los siguientes pasos
#Paso 1. abrir una consola con cmd →→→windows+r →cmd →enter
#Paso 2. →→ cd direccion-de-la-carpeta-del-proyecto
#CREACION EN ENTORNO VIRTUAL PARA FLASK
#Paso 3. Ingresar python -m venv venv         
#Paso 4. Ingresar .\venv\Scripts\activate //En windows
#Paso 5. pip install Flask
#Paso 6. pip list   #PERMITE VER LO QUE SE INSTALO, debe salir flask
#Paso 7. Ejecutar en vsc

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('registro.html')

clientes = []
@app.route('/guardar_cliente', methods=['POST'])
def guardar_cliente():
    nombre = request.form['nombre']
    email = request.form['email']
    nit = request.form['nit']
    
    if nit in [cliente['nit'] for cliente in clientes]:
        return jsonify({'success': False, 'message': 'El NIT ya existe.'})
    
    clientes.append({'nombre': nombre, 'email': email, 'nit': nit})
    
    return jsonify({'success': True})

@app.route('/getClientes')
def mostrar_cliente():
    return render_template('clientesTabla.html', clientes=clientes)




if __name__ == '__main__':
    app.run(debug=True, port=5000)
