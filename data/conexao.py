# import mysql.connector
# class Conexao: 
#     def criar_conexao():
#         conexao = mysql.connector.connect(
#             host = "localhost",
#             port = 3306,
#             user = "root",
#             password = "root",
#             database = "dbFeedback"
#     )
#         return conexao
    

import mysql.connector
class Conexao: 
    def criar_conexao():
        conexao = mysql.connector.connect(
            host = "10.110.131.22",
            port = 3306,
            user = "3ds",
            password = "banana",
            database = "db_Feedback"
            # FALTA ADICIONAR AS CURTIDAS
    )
        return conexao
    
    


