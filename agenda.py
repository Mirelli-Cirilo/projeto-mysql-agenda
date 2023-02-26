import pymysql
from base import Base

conexao = pymysql.connect(host='localhost', user='root', database='agenda', password='987654321')

cursor = conexao.cursor()


class Agenda:
    def __init__(self, nome=None, email=None):
        self._nome = nome
        self._email = email

    def novo(self):
        c = Base()
        sql = "INSERT INTO contatos (nome, email) "
        sql += f"VALUES ('{self._nome}', '{self._email}')"
        c.execute_DML(sql)
        print('Contato salvo!')

    def listar_contatos(self):
        c = Base()
        sql = "SELECT * FROM contatos"
        res = c.executa_DQL(sql)
        return res

    def pesquisar_nome(self, nome):
        c = Base()
        sql = f"SELECT * FROM contatos WHERE nome = '{nome}'"
        res = c.executa_DQL(sql)
        return res

    def pesquisar_id(self, id):
        c = Base()
        sql = f"SELECT * FROM contatos WHERE id = {id}"
        res = c.executa_DQL(sql)
        return res

    def excluir_contato(self, id):
        c = Base()
        sql = "DELETE FROM contatos "
        sql += f"WHERE id = {id}"
        c.execute_DML(sql)

    def atualizar_contato(self, id, nome, email):
        c = Base()
        sql = f"UPDATE contatos "
        sql += f" SET nome = '{nome}', email = '{email}'"
        sql += f"WHERE id = {id}"
        c.execute_DML(sql)
