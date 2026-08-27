from decimal import Decimal

from analises import faturamento_total, faturamento_por_produto, faturamento_por_vendedor


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