from flask import Flask, render_template, request
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/puntaje")
def stars():
    return("Puntaje (estrellas)")

@app.route("/comentario")
def commentary():
    return("Pagina de Comentario")

if __name__ == "__main__":
    app.run()
