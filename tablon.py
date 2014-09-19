# -*- coding: utf-8 -*-
# Añadir nueva entrada

from flask import Flask, render_template, request, redirect

app = Flask(__name__)

entradas = [ 'Aprendiendo Flask.',
'He encontrado un pen drive azul en la sala de estudios y lo he llevado a objetos perdidos.',
u'HOYGAN, ALGUIEN SAVE KOMO JAQUEAR FLASK¿',
'KDD en la Alfalfa. Que venga quien quiera.',
u'Apuntes de ADA en consigna. El archivo es ADA.zip y la contraseña es "rosa".',
]

@app.route('/')
def index():
	return render_template('index.html', entradas=entradas)

@app.route('/new', methods = ['POST'])
def new():
	text = request.form['text']
	entradas.append(text)
	return redirect('/')

@app.route('/about')
def about():
	author = "nradz"
	return render_template('about.html', author=author)





if __name__ == '__main__':
	app.debug = True
	app.run()