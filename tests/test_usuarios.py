from usuarios import (
    cadastrar_usuario,
    listar_usuarios,
    atualizar_usuario,
    excluir_usuario
)


def test_listar_usuarios():
    usuarios = listar_usuarios()

    assert isinstance(usuarios, list)


def test_cadastrar_usuario():
    email = "teste_pytest@email.com"

    resultado = cadastrar_usuario("Usuário Teste", email)

    assert resultado is not False

    usuarios = listar_usuarios()

    usuario = next(
        usuario for usuario in usuarios
        if usuario[2] == email
    )

    assert usuario[1] == "Usuário Teste"

    excluir_usuario(usuario[0])


def test_atualizar_usuario():
    email = "teste_update@email.com"

    cadastrar_usuario("Usuário Original", email)

    usuarios = listar_usuarios()

    usuario = next(
        usuario for usuario in usuarios
        if usuario[2] == email
    )

    id_usuario = usuario[0]

    resultado = atualizar_usuario(
        id_usuario,
        "Usuário Atualizado",
        email
    )

    assert resultado == 1

    excluir_usuario(id_usuario)


def test_excluir_usuario():
    email = "teste_delete@email.com"

    cadastrar_usuario("Usuário Delete", email)

    usuarios = listar_usuarios()

    usuario = next(
        usuario for usuario in usuarios
        if usuario[2] == email
    )

    id_usuario = usuario[0]

    resultado = excluir_usuario(id_usuario)

    assert resultado == 1