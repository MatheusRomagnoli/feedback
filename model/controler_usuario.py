from data.conexao import Conexao

class Usuario:
     def cadastrar(nome, login, senha):
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
        
        
