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

def dataframe_vendas():
    with conectar() as conexao:
        with conexao.cursor() as cursor:
            cursor.execute(
                """
                SELECT
                    cliente,
                    produto,
                    vendedor,
                    quantidade,
                    valor_unitario,
                    data_venda
                FROM vendas
                ORDER BY id;
                """
            )

            dados = cursor.fetchall()
            df = pd.DataFrame(
                dados,
                columns=[
                    "cliente",
                    "produto",
                    "vendedor",
                    "quantidade",
                    "valor_unitario",
                    "data_venda"
                ]
            )

            df["faturamento"] = df["quantidade"] * df["valor_unitario"]

            return df
        
def faturamento_total_pandas():
    df = dataframe_vendas()

    return df["faturamento"].sum()  

def vendas_ordenadas_por_faturamento():
    df = dataframe_vendas()

    return df.sort_values("faturamento", ascending=False)

def maior_venda():
    df = vendas_ordenadas_por_faturamento()

    return df.iloc[0]

def faturamento_por_produto_pandas():
    df = dataframe_vendas()

    return df.groupby("produto")["faturamento"].sum()

def faturamento_por_vendedor_pandas():
    df = dataframe_vendas()

    return df.groupby("vendedor")["faturamento"].sum()