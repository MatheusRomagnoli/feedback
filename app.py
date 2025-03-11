from flask import Flask, render_template, request, redirect
from datetime import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("index.html")

@app.route("/post/enviarDados", methods = ["POST"])
def post_enviarDados():
    # peguei as informações do formulario
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")

    Mensagem.cadastrar_mensagem(usuario, mensagem)
    

    # vai redirecionar pro index qnd clicar no botao
    return redirect("/")

   
app.run(debug=True)