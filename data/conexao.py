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
            # IP NOTEBOOK
            # host = "10.110.131.18",
            # IP COMPUTADOR:
            host = "10.110.134.2",
            port = 3306,
            user = "3ds",
            password = "banana",
            database = "db_Feedback"
    )
        return conexao
    
    


