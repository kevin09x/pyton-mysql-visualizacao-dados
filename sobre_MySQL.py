# . open Source

import MySQLdb

host = 'localhost'
user = 'root'
password = '123456'
db = 'central_escola'
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor()


def select(fields, tables, where=None):

    global c

    query = "SELECT " + fields + " FROM " + tables
    if(where):
        query = query + "WHERE " + where

    c.execute(query)
    return c.fetchall()


print(select("id_aluno, nome", "alunos"))
