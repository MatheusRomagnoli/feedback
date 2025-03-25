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
        sql = """INSERT INTO tb_Comentarios
                (nome, data_hora, comentario)
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
        sql = """SELECT cod_comentario, nome as usuario, comentario as mensagem, data_hora as data, curtidas FROM tb_comentarios;"""

        # executar o comando sql
        cursor.execute(sql)

        # recuperando os dados e guardando em uma variável
        resultado = cursor.fetchall()

        # fecho a conexão com o banco
        cursor.close()
        conexao.close()

        return resultado
    
    def deletar_mensagem(codigo):
        # criando a conexao com banco de dados
        conexao = Conexao.criar_conexao()

        # o cursor é a ponte que vai do python ate o banco de dados
        cursor = conexao.cursor()

        # criando o SQL que será executado
        sql = """DELETE FROM tb_comentarios
                WHERE cod_comentario = %s"""
        valores=(codigo)

        # executando o comando 
        cursor.execute(sql,valores)

        # confirmo a alteração
        conexao.commit()

        # fecho a conexao com o banco
        cursor.close()
        conexao.close()

    def curtir_mensagem(codigo):
        # criando a conexao com banco de dados
        conexao = Conexao.criar_conexao()

        # o cursor é a ponte que vai do python ate o banco de dados
        cursor = conexao.cursor()

        # criando o SQL que será executado
        sql = """UPDATE tb_comentarios
                SET curtidas = curtidas + 1
                WHERE cod_comentario = %s"""
        valores=(codigo,)

        # executando o comando 
        cursor.execute(sql,valores)

        # confirmo a alteração
        conexao.commit()

        # fecho a conexao com o banco
        cursor.close()
        conexao.close()

    def descurtir_mensagem(codigo):
        # criando a conexao com banco de dados
        conexao = Conexao.criar_conexao()

        # o cursor é a ponte que vai do python ate o banco de dados
        cursor = conexao.cursor()

        # criando o SQL que será executado
        sql = """UPDATE tb_comentarios
                SET curtidas = curtidas - 1
                WHERE cod_comentario = %s"""
        valores=(codigo,)

        # executando o comando 
        cursor.execute(sql,valores)

        # confirmo a alteração
        conexao.commit()

        # fecho a conexao com o banco
        cursor.close()
        conexao.close()

