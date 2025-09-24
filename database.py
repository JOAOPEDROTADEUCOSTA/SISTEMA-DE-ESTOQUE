import sqlite3

DB_NAME = "estoque.db"

def get_connection():
    return sqlite3.connect(DB_NAME)

def init_db():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            tipo TEXT NOT NULL,
            nome TEXT NOT NULL,
            quantidade INTEGER NOT NULL,
            preco REAL NOT NULL
        )
    """)
    conn.commit()
    conn.close()

def get_all_produtos():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM produtos")
    produtos = cur.fetchall()
    conn.close()
    return produtos

def add_produto(tipo, nome, quantidade, preco):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("INSERT INTO produtos (tipo, nome, quantidade, preco) VALUES (?, ?, ?, ?)",
                (tipo, nome, quantidade, preco))
    conn.commit()
    conn.close()

def remove_produto(produto_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("DELETE FROM produtos WHERE id=?", (produto_id,))
    conn.commit()
    conn.close()
