from usuarios import (
    cadastrar_usuario,
    listar_usuarios,
    atualizar_usuario,
    excluir_usuario
)


def mostrar_menu():
    print("\n===== SISTEMA DE USUÁRIOS =====")
    print("1 - Cadastrar usuário")
    print("2 - Listar usuários")
    print("3 - Atualizar usuário")
    print("4 - Excluir usuário")
    print("0 - Sair")


def ler_id():
    while True:
        try:
            id_usuario = int(input("Digite o ID do usuário: "))

            if id_usuario <= 0:
                print("Digite um ID maior que zero.")
                continue

            return id_usuario

        except ValueError:
            print("Digite um ID válido.")


def ler_texto(mensagem):
    while True:
        valor = input(mensagem).strip()

        if valor:
            return valor

        print("Esse campo não pode ficar vazio.")


def cadastrar():
    print("\n===== CADASTRAR USUÁRIO =====")

    nome = ler_texto("Digite o nome: ")
    email = ler_texto("Digite o e-mail: ")

    resultado = cadastrar_usuario(nome, email)

    if resultado is False:
        print("\nErro: esse e-mail já está cadastrado!")
    else:
        print("\nUsuário cadastrado com sucesso!")


def listar():
    usuarios = listar_usuarios()

    print("\n===== USUÁRIOS CADASTRADOS =====")

    if not usuarios:
        print("Nenhum usuário cadastrado.")
        return

    for usuario in usuarios:
        id_usuario, nome, email, data_cadastro = usuario

        print(f"ID: {id_usuario}")
        print(f"Nome: {nome}")
        print(f"E-mail: {email}")
        print(f"Data de cadastro: {data_cadastro}")
        print("-" * 40)


def atualizar():
    print("\n===== ATUALIZAR USUÁRIO =====")

    id_usuario = ler_id()
    nome = ler_texto("Digite o novo nome: ")
    email = ler_texto("Digite o novo e-mail: ")

    resultado = atualizar_usuario(id_usuario, nome, email)

    if resultado == 1:
        print("\nUsuário atualizado com sucesso!")
    else:
        print("\nUsuário não encontrado.")


def excluir():
    print("\n===== EXCLUIR USUÁRIO =====")

    id_usuario = ler_id()

    resultado = excluir_usuario(id_usuario)

    if resultado == 1:
        print("\nUsuário excluído com sucesso!")
    else:
        print("\nUsuário não encontrado.")


def main():
    while True:
        mostrar_menu()

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar()

        elif opcao == "2":
            listar()

        elif opcao == "3":
            atualizar()

        elif opcao == "4":
            excluir()

        elif opcao == "0":
            print("\nEncerrando o sistema...")
            break

        else:
            print("\nOpção inválida.")


if __name__ == "__main__":
    main()