# -*- coding: utf-8 -*-
# Eliminar entradas que pertenezcan al usuario según su sesión.

import random
from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = '\xac\xb5`\xec\n\xa5>\xac?\x15\xee\x8b=&\x14\x90\xf9\xc3\x00^5QqJ\xc0\xa2\x08\xc0f\xa5\xdb#'


entradas = [ ['Aprendiendo Flask.', 0],
['He encontrado un pen drive azul en la sala de estudios y lo he llevado a objetos perdidos.', 0],
[u'HOYGAN, ALGUIEN SAVE KOMO JAQUEAR FLASK¿', 0],
['KDD en la Alfalfa. Que venga quien quiera.', 0],
[u'Apuntes de ADA en consigna. El archivo es ADA.zip y la contraseña es "rosa".', 0],
]

@app.before_request
def session_id():
	if not 'id' in session:
		session['id'] = random.getrandbits(32)

@app.route('/')
def index():
	return render_template('index.html', entradas=entradas, id=session['id'])

@app.route('/new', methods = ['POST'])
def new():
	text = request.form['text']
	entradas.append([text, session['id']])
	return redirect('/')

@app.route('/post/<int:num>')
def post(num):
	if num >= len(entradas):
		entrada = "No existe dicha entrada."
	else:
		entrada = entradas[num]

	return render_template('post.html', index=num, entrada=entrada, id=session['id'])

@app.route('/delete/<int:num>')
def delete(num):
	if num >= len(entradas):
		return redirect('/')

	if entradas[num][1] == session['id']:
		del entradas[num]

	return redirect('/')


@app.route('/about')
def about():
	author = "nradz"
	return render_template('about.html', author=author)





if __name__ == '__main__':
	app.debug = True
	app.run()