import os

clients = ['Gabriella Izabel', 'Andre Santana', 'Rosane Nô', 'Gabriel Araujo']


def display_program_name():
    print('𝓜𝓪𝓻𝓲𝓪 𝓡𝓸𝓼𝓪\n')


def display_options():
    print("1. Cadastrar cliente")
    print("2. Listar cliente")
    print("3. Ativar cliente")
    print("4. Sair\n")


def terminate_app():
    os.system('cls')
    print('Closing program/application')


def invalid_input():
    print('Invalid option\n')
    input('Choose an option to get back to main menu.')
    main()


def adding_new_client():
    os.system('cls')
    print("Cadastro de novos clientes\n")
    client_name = input("Digite o nome do cliente que deseja cadastrar: ")
    clients.append(client_name)
    print(f"Cliente {client_name} foi cadastrado com sucesso. ")
    input("Digite a tecla para voltar ao menu principal.")
    main()


def show_registered_clients():
    os.system('cls')
    print('Listing all clients alrteady registered: \n')
    for client in clients:
        print(client)
    input('Press any key to go back to main menu...')
    main()


def chosen_option():
    try:
        user_option = int(input("Escolha uma opção: "))
        print(f"Opcão escolhida: {user_option}")

        if user_option == 1:
            adding_new_client()
        elif user_option == 2:
            show_registered_clients()
        elif user_option == 3:
            print("Cliente validado para prosseguir com as compras")
        elif user_option == 4:
            terminate_app()
        else:
            invalid_input()
    except:
        invalid_input()


def main():
    os.system('cls')
    display_program_name()
    display_options()
    chosen_option()


if __name__ == '__main__':
    main()
