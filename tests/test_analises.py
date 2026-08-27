from analises import faturamento_total, faturamento_por_produto, faturamento_por_vendedor, faturamento_total_pandas, maior_venda, faturamento_por_produto_pandas, faturamento_por_vendedor_pandas

from decimal import Decimal

def test_faturamento_total():
    resultado = faturamento_total()

    assert resultado == Decimal("2725.00")


def test_faturamento_por_produto():
    resultado = faturamento_por_produto()

    assert resultado == [
        ("Produto X", Decimal("1087.80")),
        ("Produto Y", Decimal("998.00")),
        ("Produto Z", Decimal("639.20"))
    ]

def test_faturamento_por_vendedor():
    resultado = faturamento_por_vendedor()

    assert resultado == [
        ("Vendedor 1", Decimal("1087.80")),
        ("Vendedor 2", Decimal("998.00")),
        ("Vendedor 3", Decimal("639.20"))
    ]   

def test_faturamento_total_pandas():
    resultado = faturamento_total_pandas()

    assert resultado == 2725.00 

def test_maior_venda():
    resultado = maior_venda()

    assert resultado["cliente"] == "Cliente D"
    assert resultado["produto"] == "Produto Y"
    assert resultado["vendedor"] == "Vendedor 2"
    assert resultado["quantidade"] == 15
    assert resultado["faturamento"] == 748.50

def test_faturamento_por_produto_pandas():
    resultado = faturamento_por_produto_pandas()

    assert resultado["Produto X"] == Decimal("1087.80")
    assert resultado["Produto Y"] == Decimal("998.00")
    assert resultado["Produto Z"] == Decimal("639.20")

def test_faturamento_por_vendedor_pandas():
    resultado = faturamento_por_vendedor_pandas()

    assert resultado["Vendedor 1"] == Decimal("1087.80")
    assert resultado["Vendedor 2"] == Decimal("998.00")
    assert resultado["Vendedor 3"] == Decimal("639.20")