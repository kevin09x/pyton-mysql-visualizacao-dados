# import MySQLdb

# host = "localhost"
# user = "root"
# password = "123456"
# db = "escola_curso"
# port = 3306

# con = MySQLdb.connect(host, user, password, db, port)

# c = con.cursor()


# def select(fields, tables, where=None):

#     global c

#     query = "Select" + fields + "FROM" + tables
#     if (where):
#         query = query + "where" + where
#     c.execute(query)

#     return c, fetchall()


# print(select("nome, cpf", "alunos", "id_aluno = 1"))
# print(c)
