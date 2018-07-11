import sqlite3

def pathCath():
    patch = open('data_patch', 'r')
    return patch.readline()

def createDatabaseIfNotExists():
    stringPath = str(pathCath())
    print(stringPath)
    conn  = sqlite3.connect(stringPath)
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS `plataforma` (
	`id_plataforma`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nome`	TEXT NOT NULL,
	`imagem`	TEXT
        );""")
    cursor.execute("""              
    CREATE TABLE IF NOT EXISTS `jogo` (
	`id_jogo`	INTEGER PRIMARY KEY AUTOINCREMENT,
	`nome`	TEXT NOT NULL,
	`completo`	REAL DEFAULT 0.0,
	`capa`	TEXT,
	`plataforma`	INTEGER NOT NULL,
	FOREIGN KEY(`plataforma`) REFERENCES `plataforma`(`id_plataforma`)
        );
    """)
    conn.commit()
    conn.close()

