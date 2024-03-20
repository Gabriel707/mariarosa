import os

clientes = [{'nome': 'Gabriella Izabel', 'categoria': 'Premium', 'ativo': True},
            {'nome': 'Andre Santana', 'categoria': 'Platinum', 'ativo': False},
            {'nome': 'Rosane Nô', 'categoria': 'Gold', 'ativo': True},
            {'nome': 'Gabriel Araujo', 'categoria': 'Basic', 'ativo': True}]


def exibir_nome_do_programa():
    print('𝓜𝓪𝓻𝓲𝓪 𝓡𝓸𝓼𝓪\n')


def listar_opcoes():
    print("1. Cadastrar cliente")
    print("2. Listar cliente")
    print("3. Alterar status do cliente")
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
    linha = '*' * (len(text) + 4)
    print(linha)
    print(text)
    print(linha)
    print()


def add_novo_cliente():
    '''Função que adiciona novo cliente a base de dados.

    Inputs:
    - Nome do Cliente
    - Categoria do Cliente(plano escolhido)

    Output:
    - Adiciona novo cliente a base de clientes.

    '''
    exibir_subtitulo("Cadastro de novos clientes")
    nome_cliente = input("Digite o nome do cliente que deseja cadastrar: ")
    categoria = input('Digite o tipo de membership desejada: ')
    dados_do_cliente = {'nome': nome_cliente,
                        'categoria': categoria,
                        'ativo': False}
    clientes.append(dados_do_cliente)
    clientes.append(nome_cliente)
    print(f"Cliente {nome_cliente} foi cadastrado com sucesso. ")
    voltar_ao_menu()


def listar_clientes_cadastrados():
    exibir_subtitulo('Listing clients: ')

    print(f'{'Nome do cliente'.ljust(22)} | {'Categoria'.ljust(20)} | Status')

    for client in clientes:
        client_name = client['nome']
        categoria = client['categoria']
        ativo = 'ativado' if client['ativo'] else 'desativado'
        print(f' - {client_name.ljust(20)} | {categoria.ljust(20)} | {ativo}')
    voltar_ao_menu()


def alternar_status_do_cliente():
    exibir_subtitulo('Alterando status do restaurante')
    nome_cliente = input(
        'Digite o nome do cliente que deseja alterar o status:')
    cliente_encontrado = False

    for cliente in clientes:
        if nome_cliente == cliente['nome']:
            cliente_encontrado = True
            cliente['ativo'] = not cliente['ativo']
            mensagem = f'O {nome_cliente} foi ativado com sucesso.' if cliente['ativo'] else f'O  cliente: {
                nome_cliente} foi desativado com sucesso.'
            print(mensagem)

    if not cliente_encontrado:
        print('Cliente nao encontrado.')

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
            alternar_status_do_cliente()
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
