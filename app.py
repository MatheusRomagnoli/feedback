from flask import Flask, render_template, request, redirect, session
from datetime import datetime
import mysql.connector
from data.conexao import Conexao
from model.controler_mensagem import Mensagem
from model.controler_usuario import Usuario

app = Flask(__name__)

app.secret_key = "Maithe"

@app.route("/")
def pagina_principal():
    if "usuario" in session:
        mensagens = Mensagem.recuperar_mensagens()

        return render_template("index.html", mensagens = mensagens)
    else:
        return redirect("/login")

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
@app.route("/put/mensagem/adicionar/curtida/<codigo>")
def adicionar_curtida(codigo):
    Mensagem.curtir_mensagem(codigo)
    return redirect("/")


# ROTA DESCURTIR MENSAGEM
@app.route("/put/mensagem/remover/curtida/<codigo>")
def remover_curtida(codigo):
    Mensagem.descurtir_mensagem(codigo)
    return redirect("/")

# ROTA CADASTRO FUNÇÃO
@app.route("/post/cadastrarUsuario", methods=["POST"])
def cadastrar_usuario():
    nome = request.form.get("nome")
    login = request.form.get("login")
    senha = request.form.get("senha")

    Usuario.cadastrar(nome, login, senha)
    return redirect("/login")

@app.route("/cadastro")
def pagina_usuario():
    return render_template ("cadastro.html")

# LOGIN USUARIO
@app.route("/post/login", methods = ["POST"])
def post_login():
    login = request.form.get("login")
    senha = request.form.get("senha")

    esta_logado = Usuario.login(login, senha)
    if esta_logado:
        return redirect("/")
    else:
        return redirect("/login")
    
@app.route("/login")
def pagina_login():
    return render_template ("login.html")

# LOGOFF
@app.route("/logoff")
def logoff():
    Usuario.logoff()
    return render_template ("login.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)




