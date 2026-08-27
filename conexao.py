import os

import psycopg

from dotenv import load_dotenv

load_dotenv()


class ErroConexao(Exception):
    """Erro relacionado à conexão com o PostgreSQL."""
    pass


def conectar():
    try:
        return psycopg.connect(
            host=os.getenv("DB_HOST"),
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD")
        )

    except psycopg.Error as erro:
        raise ErroConexao(
            "Não foi possível conectar ao PostgreSQL."
        ) from erro