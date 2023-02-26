import pymysql


class Base:
    def __init__(self, host='localhost', user='root', password='987654321', database='agenda'):
        self.host = host
        self.user = user
        self.psw = password
        self.db = database

    def conectar(self):
        self.con = pymysql.connect(host=self.host, user=self.user, password=self.psw, database=self.db)
        self.cur = self.con.cursor()

    def desconectar(self):
        self.con.close()

    def executa_DQL(self, sql):
        self.conectar()
        self.cur.execute(sql)
        res = self.cur.fetchall()
        self.desconectar()
        for c in res:
            print(c)

    def execute_DML(self, sql):
        self.conectar()
        self.cur.execute(sql)
        self.con.commit()
        self.desconectar()