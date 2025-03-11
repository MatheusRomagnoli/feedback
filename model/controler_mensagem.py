import datetime
from data.conexao import Conexao


class Mensagem:
    def cadastrar_mensagem(usuario, mensagem):
        
        data_hora = datetime.datetime.today()

        # criando a conexao com banco de dados
        conexao = Conexao.criar_conexao()

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


    def recuperar_mensagens():
        # Criar conexão
        conexao = Conexao.criar_conexao()
        # dictionary = True: quando ele me retornar as mensagens, ele vai me devolver essas informações, vai colocar o mesmo nome que está no SQL

        # o cursor é responsável por manipular o banco de dados
        cursor = conexao.cursor(dictionary=True) 

        # criando o sql que será executado
        sql = """SELECT nome, comentario, data_comentario FROM tbComentarios;"""

        # executar o comando sql
        cursor.execute(sql)

        # recuperando os dados e guardando em uma variável
        resultado = cursor.fetchall()

        # fecho a conexão com o banco
        cursor.close()
        conexao.close()

        return resultado
    

