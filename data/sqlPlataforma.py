import sqlite3
import data.dataBinding as datapath
from data.pojos import Plataforma

def insertPlataforma(plataforma):
    conn = sqlite3.connect(datapath.pathCath())
    cursor = conn.cursor()
    try:
        cursor.execute("""
        insert into plataforma(nome, imagem) values (? , ?)
        """, (plataforma.nome, plataforma.imagem))
        conn.commit()

    except sqlite3.Error:
        conn.rollback()
    finally:
        conn.close()

def selectPlataforma(all = None):
    conn = sqlite3.connect(datapath.pathCath())
    cursor = conn.cursor()
    result = []
    try:
        if all == None:
            cursor.execute("""
            select * from plataforma
            """)
        else:
            cursor.execute("""
            select * from plataforma where id_plataforma == ?
            """,str(all))
        data = cursor.fetchall()
        for r in data:
            console = Plataforma(r[1],r[0],r[2])
            result.append(console)
    except sqlite3.Error:
        print("algum erro")
    finally:
        conn.close()
        if len(result) == 1:
            return result[0]
        else:
            return  result

def updatePlataforma(plataforma):
    conn = sqlite3.connect(datapath.pathCath())
    cursor = conn.cursor()
    try:
        cursor.execute("""
        update plataforma set nome = ?, imagem = ? where id_plataforma = ?
        """,(plataforma.nome,plataforma.imagem, plataforma.id_plataforma))
        conn.commit()
    except sqlite3.Error:
        conn.rollback()
    finally:
        conn.close()


