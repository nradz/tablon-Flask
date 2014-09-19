# Dos controladores con sus rutas y plantillas

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/about')
def about():
	author = "nradz"
	return render_template('about.html', author=author)





if __name__ == '__main__':
	app.debug = True
	app.run()