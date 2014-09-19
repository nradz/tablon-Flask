# -*- coding: utf-8 -*-
# Eliminar entradas que pertenezcan al usuario según su sesión.

import random, sqlite3
from flask import Flask, render_template, request, redirect, session, g

app = Flask(__name__)
app.secret_key = '\xac\xb5`\xec\n\xa5>\xac?\x15\xee\x8b=&\x14\x90\xf9\xc3\x00^5QqJ\xc0\xa2\x08\xc0f\xa5\xdb#'

@app.before_request
def before_request():
	if not 'id' in session:
		session['id'] = random.getrandbits(32)

	g.db = sqlite3.connect('entradas.db')

@app.teardown_request
def teardown_request(exception):
	if hasattr(g, 'db'):
		g.db.close()

@app.route('/')
def index():
	entradas = g.db.execute("SELECT * FROM entradas").fetchall()

	return render_template('index.html', entradas=entradas, id=session['id'])

@app.route('/new', methods = ['POST'])
def new():
	text = request.form['text']
	g.db.execute("INSERT INTO entradas (text, id_session) VALUES(?,?)", (text, session['id']))
	g.db.commit()
	return redirect('/')

@app.route('/post/<int:num>')
def post(num):

	res = g.db.execute("SELECT * FROM entradas WHERE id=?", (num,)).fetchone()

	if res == None:
		res = (0, "No existe la entrada.", 0)

	return render_template('post.html', entrada=res, id=session['id'])

@app.route('/delete/<int:num>')
def delete(num):

	g.db.execute("DELETE FROM entradas WHERE id=?", (num,))
	g.db.commit()

	return redirect('/')


@app.route('/about')
def about():
	author = "nradz"
	return render_template('about.html', author=author)





if __name__ == '__main__':
	app.debug = True
	app.run()