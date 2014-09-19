# Ejemplo inicial con Flask

from flask import Flask

app = Flask(__name__)


@app.route('/')
def hola_Mundo():
	return "Hola mundo"



if __name__ == '__main__':
	app.debug = True
	app.run()