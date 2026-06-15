import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

def conectar():
    return psycopg2.connect(
        host=os.getenv("DB_HOST"),
        port=os.getenv("DB_PORT"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD")
    )

def adicionar_gasto(descricao, valor, data_gasto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        """
        INSERT INTO gastos (descricao, valor, data_gasto)
        VALUES (%s, %s, %s)
        """,
        (descricao, valor, data_gasto)
    )

    conn.commit()
    cursor.close()
    conn.close()


def listar_gastos():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT id, descricao, valor, data_gasto
        FROM gastos
        ORDER BY id
    """)

    gastos = cursor.fetchall()

    cursor.close()
    conn.close()

    return gastos

def remover_gasto(id_gasto):
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        'DELETE FROM gastos WHERE "Id" = %s',
        (id_gasto,)
    )

    conn.commit()

    cursor.close()
    conn.close()

def calcular_total():
    conn = conectar()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT COALESCE(SUM(valor), 0) FROM gastos"
    )

    total = cursor.fetchone()[0]

    cursor.close()
    conn.close()

    return total