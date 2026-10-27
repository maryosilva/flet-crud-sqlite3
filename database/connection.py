import sqlite3 
import os
from contextlib import contextmanager

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_FILE = os.path.join(BASE_DIR, "app.db")

@contextmanager
def get_db_connection():
    conn = sqlite3.connect(DB_FILE)
    conn.row_factory = sqlite3.Row
    try:
        yield conn
    finally:
        conn.close()

def init_db():
    with get_db_connection() as conn:
        cursor = conn.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS usuarios (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL
            );
        """)
        conn.commit()

def test_connection_db():

    print("🔄 Tentando conectar ao banco de dados...")

    try:
        with get_db_connection() as conn:
            cursor = conn.cursor()
            cursor.execute("SELECT sqlite_version();")
            versao = cursor.fetchone()
            
            print("Conexão estabelecida com sucesso!")
            print(f"Versão do SQLite em uso: {versao[0]}")
            
    except Exception as e:
        print("Falha na conexão com o banco de dados!")
        print(f"Erro encontrado: {e}")
