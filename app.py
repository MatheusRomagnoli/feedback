from flask import Flask
app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return "PAGINA PRINCIPAL"



app.run(debug=True)