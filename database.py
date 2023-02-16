import sqlite3

conn = sqlite3.connect("Usuariodata.db")

cursor = conn.cursor()

cursor.execute("""

CREATE TABLE IF NOT EXISTS Usuario (
    CPF INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    Nome TEXT NOT NULL,
    Data TEXT NOT NULL,
    RG TEXT NOT NULL,
    Senha TEXT NOT NULL,
    Tel TEXT NOT NULL,
    End TEXT NOT NULL,
);
""")

print("Conectado ao Banco de dados")