import mysql.connector
class Conexao: 
    def criar_conexao():
        conexao = mysql.connector.connect(
            hostname = "localhost",
            port = 3306,
            user = "root",
            password = "root",
            database = "dbFeedback"
    )
        return conexao
    
