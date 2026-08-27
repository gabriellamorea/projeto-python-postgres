from psycopg import errors

from conexao import conectar


def cadastrar_usuario(nome, email):
    try:
        with conectar() as conexao:
            with conexao.cursor() as cursor:
                cursor.execute(
                    """
                    INSERT INTO usuarios (nome, email)
                    VALUES (%s, %s)
                    """,
                    (nome, email)
                )

    except errors.UniqueViolation:
        return False


def listar_usuarios():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT id, nome, email, data_cadastro
                FROM usuarios
                ORDER BY id
                """
            )

            return cursor.fetchall()


def atualizar_usuario(id_usuario, nome, email):
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                UPDATE usuarios
                SET nome = %s,
                    email = %s
                WHERE id = %s
                """,
                (nome, email, id_usuario)
            )

            return cursor.rowcount


def excluir_usuario(id_usuario):
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                DELETE FROM usuarios
                WHERE id = %s
                """,
                (id_usuario,)
            )

            return cursor.rowcount