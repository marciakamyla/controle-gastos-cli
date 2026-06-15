from src.banco import conectar

def test_conexao():
    conn = conectar()

    assert conn is not None

    conn.close()