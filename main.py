from flask import Flask, request, make_response, redirect, render_template, session, url_for, flash
from flask_bootstrap import Bootstrap
from app.templates.forms import LoginForm

import unittest

from app import create_app

app = create_app()


todos = ['Comprar Cafe', 'Enviar Solicitud', 'Enviar video']


@app.cli.command()
def test():
	tests = unittest.TestLoader().discover('tests')
	unittest.TextTestRunner().run(tests)


@app.errorhandler(404)
def not_found(error):
	return render_template('404.html', error=error)

@app.errorhandler(500)
def server_error(error):
	return render_template('500.html', error=error)



@app.route('/', methods=['GET', 'POST']) #decorador de Flask route, crea la direccion a la ruta raiz
def index():

	user_ip = request.remote_addr #asigna la ip del visitante a user_ip

	response = make_response(redirect('/hello')) #redirecciona la respuesta a la ruta /hello
	#response.set_cookie('user_ip', user_ip) #se genera la coockie con la ip del ususario
	session['user_ip'] = user_ip

	return response
 
@app.route('/hello', methods=['GET'])
def hello():
	
	#user_ip = request.cookies.get('user_ip') 
	user_ip = session.get('user_ip')
	#login_form = LoginForm() 
	username = session.get('username')
	print(username)
	# Se crea el diccionario para pasar el contexto al template, en vez de hacerlo uno a uno se agrupa todo en un diccionario
	context = {
		'user_ip': user_ip,
		'todos': todos,
		#'login_form': login_form,
		'username': username
		}

	# if login_form.validate_on_submit():
	# 	username = login_form.username.data
	# 	session['username'] = username
	# 	flash('Nombre de usuario registrado con exito')
	# 	return redirect(url_for('index'))
	#como se creo un diccionario para pasar el contexto, este se "abre" con los ** para no tener que estar buscando dentro del diccionario
		

	return render_template('hello.html', **context)

	#con esto se hace el render del html!!! no son dos variables lo que se pasa si se quita el user_ip=user_ip y se deja solo user_ip, sale error de que se estan enviando dos variables