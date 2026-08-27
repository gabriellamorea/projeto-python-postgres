import pandas as pd

from conexao import conectar


def faturamento_total():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    SUM(quantidade * valor_unitario) AS faturamento_total
                FROM vendas
                """
            )

            resultado = cursor.fetchone()

            return resultado[0]


def faturamento_por_produto():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    produto,
                    SUM(quantidade * valor_unitario) AS faturamento
                FROM vendas
                GROUP BY produto
                ORDER BY faturamento DESC
                """
            )

            return cursor.fetchall()


def faturamento_por_vendedor():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    vendedor,
                    SUM(quantidade * valor_unitario) AS faturamento
                FROM vendas
                GROUP BY vendedor
                ORDER BY faturamento DESC
                """
            )

            return cursor.fetchall()


def dataframe_faturamento_produto():
    dados = faturamento_por_produto()

    df = pd.DataFrame(
        dados,
        columns=["produto", "faturamento"]
    )

    return df