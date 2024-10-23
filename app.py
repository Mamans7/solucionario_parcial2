from flask import Flask, render_template, request, session, redirect, url_for
app = Flask(__name__)
# Activando sesion
app.secret_key = 'clave_secreta'

@app.route('/')
def index():
  if 'diccionario' not in session:
    session['diccionario'] =[]
  total = sum(item['cantidad']*item['precio'] for item in session['diccionario'])
  print(total)
  return render_template('index.html', datos=session['diccionario'], total=total)

@app.route('/verificar', methods=['GET', 'POST'])
def verificar():
  if 'id' not in session:
      session['id'] = 0
  session['id'] += 1
  
  id = session['id']  # Asigna el valor único a la variable local id
  descripcion = request.form.get('descripcion')
  cantidad = float(request.form.get('cantidad'))
  precio = float(request.form.get('precio'))
  fecha = request.form.get('fecha')
  categoria = request.form.get('categoria')
  subtotal = cantidad*precio
  if 'diccionario' not in session:
    session['diccionario'] =[]
  session['diccionario'].append({'id':id,'descripcion':descripcion,'cantidad':cantidad,'precio':precio,'fecha':fecha,'categoria':categoria,'subtotal':subtotal})  
  session.modified=True
  return redirect(url_for('index'))
  
@app.route('/vaciar')
def vaciar():
  # Limiamos la sesion
  session.clear()
  #session.pop("diccionario", None)
  return redirect(url_for('index'))


@app.route('/editar/<int:id>')
def editar(id):
  # Lógica para editar el registro con el id correspondiente
  return f'Editar registro con ID: {id}'

@app.route('/borrar')
def borrar():
  session['diccionario'].pop(0)
  session.modified=True
  return redirect(url_for('index'))



if __name__ == '__main__':
  app.run(debug=True)