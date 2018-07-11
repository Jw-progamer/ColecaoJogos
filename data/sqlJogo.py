import sqlite3
import data.dataBinding as databasePath
from data.pojos import Plataforma
import data.sqlPlataforma as foreing
from data.pojos import Jogo

def insertJogo(jogo):
    conn = sqlite3.connect(databasePath.pathCath())
    cursor = conn.cursor()
    try:
        cursor.execute("""
            insert into jogo(nome, completo, plataforma) values (? , ?, ?)
            """, (jogo.nome, str(jogo.completo), str(jogo.plataforma.id_plataforma)))
        conn.commit()

    except sqlite3.Error:
        print("Algum erro")
        conn.rollback()
    finally:
        conn.close()


def selectJogo(all = None):
    conn = sqlite3.connect(databasePath.pathCath())
    cursor = conn.cursor()
    result = []
    try:
        if all == None:
            cursor.execute("""
            select * from jogo
            """)
        else:
            cursor.execute("""
            select * from jogo where id_jogo == ?
            """,str(all))
        data = cursor.fetchall()
        for r in data:
            jogo = Jogo(r[1],foreing.selectPlataforma(r[4]),r[0],r[2],r[3])
            result.append(jogo)
    except sqlite3.Error:
        print("algum erro")
    finally:
        conn.close()
        if len(result) == 1:
            return result[0]
        else:
            return result

def updateJogo(jogo):
    conn = sqlite3.connect(databasePath.pathCath())
    cursor = conn.cursor()
    try:
        cursor.execute("""
                update jogo set nome = ?, capa =?, completo = ? where id_jogo == ?
                """, (jogo.nome, jogo.capa, str(jogo.completo), str(jogo.id_jogo)))
        conn.commit()

    except sqlite3.Error:
        print("Algum erro")
        conn.rollback()
    finally:
        conn.close()

def deleteJogo(jogo):
    conn = sqlite3.connect(databasePath.pathCath())
    cursor = conn.cursor()
    try:
        cursor.execute("""
                    delete from jogo where id_jogo == ?
                    """, (str(jogo.id_jogo)))
        conn.commit()

    except sqlite3.Error:
        print("Algum erro")
        conn.rollback()
    finally:
        conn.close()
