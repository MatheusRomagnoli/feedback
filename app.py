from flask import Flask, render_template, request
from datetime import datetime
import mysql.connector

app = Flask(__name__)

@app.route("/")
def pagina_principal():
    return render_template("index.html")

@app.route("/post/enviarDados", methods = ["POST"])
def post_enviarDados():
    # peguei as informações do formulario
    usuario = request.form.get("usuario")
    mensagem = request.form.get("mensagem")
    data_hora = datetime.datetime.today()



    # criando a conexqo com banco de dados
    conexao = _mysql_connector.connector.connect(
    hostname = "localhost",
    port = 3306,
    user = "root",
    password = "root",
    database = "dbFeedback"
)
    # o cursor é a ponte que vai do python ate o banco de dados
    cursor = conexao.cursor()

    # criando o SQL que será executado
    sql = """INSERT INTO tbComentarios
            (nome, data_comentario, comentario)
            VALUES
            (%s, %s, %s)"""
    valores=(usuario, data_hora, mensagem)

    # executando o comando 
    cursor.execute(sql,valores)

    # confirmo a alteração
    conexao.commit()

    # fecho a conexao com o banco
    cursor.close()
    conexao.close()

    # vai redirecionar pro index qnd clicar no botao
    return render_template("index.html")




app.run(debug=True)