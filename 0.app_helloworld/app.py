#Se importa el módulo Flask desde el paquete flask
from flask import Flask

#Se crea una instancia de la clase Flask
app = Flask(__name__) #El argumento (__name__) indica a Flask que útilice el nombre del archivo actual main.py

#Se usa el decorador "@app.route("")" que define una ruta que corresponde a la página principal del app
@app.route("/")

def hello():
    return "<h1>Hello, World Flask!</h1>"

#Solo se ejecuta si el archivo es ejecutado directamente 
if __name__ == '__main__':
    app.run(debug=True, port=5000) #"debug=True" arranca la aplicación Flask en modo de depuración.