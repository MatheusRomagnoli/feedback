from flask import Flask, render_template, request, redirect
from datetime import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    mensagens = Mensagem.recuperar_mensagens()

    return render_template("index.html", mensagens = mensagens)

@app.route("/post/enviarDados", methods = ["POST"])
def post_enviarDados():
    # peguei as informações do formulario
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")

    Mensagem.cadastrar_mensagem(usuario, mensagem)

    

    # vai redirecionar pro index qnd clicar no botao
    return redirect("/")

@app.route("/delete/mensagem/<codigo>")
def delete_mensagem(codigo):
    Mensagem.deletar_mensagem(codigo)
    return redirect("/")
   
# ROTA CURTIR MENSAGEM
@app.route("put/mensagem/adicionar/curtida/<codigo>")
def adicionar_curtida(codigo):
    Mensagem.curtir_mensagem(codigo)
    return redirect("/")

app.run(debug=True)

# ROTA DESCURTIR MENSAGEM
@app.route("put/mensagem/remover/curtida/<codigo>")
def remover_curtida(codigo):
    Mensagem.descurtir_mensagem(codigo)
    return redirect("/")

app.run(debug=True)