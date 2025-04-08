from hashlib import sha256
from flask import session
from data.conexao import Conexao

class Usuario:
        def cadastrar(nome, login, senha):
                #  criptografando a senha
                senha = sha256(senha.encode()).hexdigest()

                # criando a conexao com banco de dados
                conexao = Conexao.criar_conexao()

                # o cursor é a ponte que vai do python ate o banco de dados
                cursor = conexao.cursor()

                # criando o SQL que será executado
                sql = """INSERT INTO tb_usuarios
                        (nome, login, senha)
                        VALUES
                        (%s, %s, %s)"""
                valores=(nome, login, senha)

                # executando o comando 
                cursor.execute(sql,valores)

                # confirmo a alteração
                conexao.commit()

                # fecho a conexao com o banco
                cursor.close()
                conexao.close()
    
        def login(login, senha):
                #  criptografando a senha
                senha = sha256(senha.encode()).hexdigest()

                # criando a conexao com banco de dados
                conexao = Conexao.criar_conexao()

                # o cursor é a ponte que vai do python ate o banco de dados
                cursor = conexao.cursor(dictionary=True)

                # criando o SQL que será executado
                sql = """SELECT login, nome FROM tb_usuarios
                        WHERE login = %s
                        AND senha = %s """
                valores=(login, senha)

                # executando o comando 
                cursor.execute(sql,valores)

                resultado = cursor.fetchone()

                # confirmo a alteração
                conexao.commit()

                # fecho a conexao com o banco
                cursor.close()
                conexao.close()

                if resultado:
                        session["usuario"] = resultado["login"]
                        session["nome_usuario"] = resultado["nome"]
                        return True
                else:
                        return False
        
        def logoff():
                session.clear()

        