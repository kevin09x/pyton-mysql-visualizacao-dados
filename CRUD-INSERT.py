import MySQLdb

host = 'localhost'
user = 'root'
password = '123456'
db = 'escola_curso'
port = 3306

con = MySQLdb.connect(host, user, password, db, port)

c = con.cursor(MySQLdb.cursors.DictCursor)


def select(fields, tables, where=None):

    global c

    query = "SELECT " + fields + " FROM " + tables
    if(where):
        query = query + " WHERE " + where

    c.execute(query)
    return c.fetchall()


def insert(values, table, fields=None):

    global c, con

    query = "INSERT INTO " + table
    if (fields):
        query = query + " (" + fields + ") "
    query = query + " VALUES " + ",".join(["(" + v + ") "for v in values])

    c.execute(query)
    con.commit()


values = [
    "default, 'João Pedro', '2000-01-01', 'Av das pedras, 123', 'Betim', 'MG', '12345678911'"
    "default, 'Maria Pedro', '2000-01-01', 'Av das pedras, 123', 'Betim', 'MG', '12345678911'"
]

insert(values, "alunos")
