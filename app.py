import os

clients = [{'nome': 'Gabriella Izabel', 'categoria': 'Premium', 'ativo': True},
           {'nome': 'Andre Santana', 'categoria': 'Platinum', 'ativo': False},
           {'nome': 'Rosane Nô', 'categoria': 'Gold', 'ativo': True},
           {'nome': 'Gabriel Araujo', 'categoria': 'Basic', 'ativo': True}]


def exibir_nome_do_programa():
    print('𝓜𝓪𝓻𝓲𝓪 𝓡𝓸𝓼𝓪\n')


def listar_opcoes():
    print("1. Cadastrar cliente")
    print("2. Listar cliente")
    print("3. Ativar cliente")
    print("4. Sair\n")


def terminate_app():
    exibir_subtitulo('Finalizando a aplicação')


def voltar_ao_menu():
    input('\nChoose an option to get back to main menu.')
    main()


def input_invalido():
    print('Invalid option\n')
    voltar_ao_menu()


def exibir_subtitulo(text):
    os.system('cls')
    print(text)
    print()


def add_novo_cliente():
    exibir_subtitulo("Cadastro de novos clientes")
    nome_cliente = input("Digite o nome do cliente que deseja cadastrar: ")
    categoria = input('Digite o tipo de membership desejada: ')
    dados_do_cliente = {'nome': nome_cliente,
                        'categoria': categoria,
                        'ativo': False}
    clients.append(dados_do_cliente)
    clients.append(nome_cliente)
    print(f"Cliente {nome_cliente} foi cadastrado com sucesso. ")
    voltar_ao_menu()


def listar_clientes_cadastrados():
    exibir_subtitulo('Listing clients: ')

    for client in clients:
        client_name = client['nome']
        categoria = client['categoria']
        ativo = client['ativo']
        print(f' - {client_name} | {categoria} | {ativo}')
    voltar_ao_menu()


def chosen_option():
    try:
        user_option = int(input("Escolha uma opção: "))
        print(f"Opcão escolhida: {user_option}")

        if user_option == 1:
            add_novo_cliente()
        elif user_option == 2:
            listar_clientes_cadastrados()
        elif user_option == 3:
            print("Cliente validado para prosseguir com as compras")
        elif user_option == 4:
            terminate_app()
        else:
            input_invalido()
    except:
        input_invalido()


def main():
    os.system('cls')
    exibir_nome_do_programa()
    listar_opcoes()
    chosen_option()


if __name__ == '__main__':
    main()
