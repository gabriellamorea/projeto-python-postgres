import pytest
from unittest.mock import patch

import conexao


def test_conexao_com_erro():
    with patch(
        "conexao.psycopg.connect",
        side_effect=conexao.psycopg.OperationalError
    ):
        with pytest.raises(conexao.ErroConexao):
            conexao.conectar()