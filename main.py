from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ejercicio1', methods=['GET', 'POST'])
def ejercicio1():
    if request.method == 'POST':
        #Procesar datos del formulario del ejercicio 1
        nota1 = int(request.form['nota1'])
        nota2 = int(request.form['nota2'])
        nota3 = int(request.form['nota3'])
        asistencia = int(request.form['asistencia'])

        #Calcular promedio
        promedio = (nota1 + nota2 + nota3) / 3

        #Verificar condiciones para aprobar o reprobar
        if promedio >= 40 and asistencia >= 75:
            estado = 'APROBADO'

        else:
            estado = 'REPROBADO'

        return render_template('ejercicio1.html', promedio=promedio, estado=estado, nota1=nota1, nota2=nota2, nota3=nota3, asistencia=asistencia)
    return render_template('ejercicio1.html')

@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
    if request.method == 'POST':
        #Procesar datos del formulario del ejericio 2
        nombre1 = request.form['nombre1']
        nombre2 = request.form['nombre2']
        nombre3 = request.form['nombre3']

        #Encontrar el nombre más largo
        nombres = [nombre1, nombre2, nombre3]
        nombre_mas_largo = max(nombres, key=len)
        cantidad_caracteres = len(nombre_mas_largo)

        return render_template('ejercicio2.html', nombre1=nombre1, nombre2=nombre2, nombre3=nombre3, nombre_mas_largo=nombre_mas_largo, cantidad_caracteres=cantidad_caracteres)
    return render_template('ejercicio2.html')

if __name__ == '__main__':
    app.run(debug=True)


