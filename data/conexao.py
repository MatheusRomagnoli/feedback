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
            # # IP COMPUTADOR:
            # host = "10.110.134.2",
            host = "bdgodofredo-alexstocco-93db.b.aivencloud.com",
            port = 27974,
            user = "3ds",
            password = "banana",
            database = "db_Feedback"
    )
        return conexao
    
    


