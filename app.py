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
    display_option_titles('Finalizando a aplicação')


def back_to_main_menu():
    input('\nChoose an option to get back to main menu.')
    main()


def invalid_input():
    print('Invalid option\n')
    back_to_main_menu()


def display_option_titles(text):
    os.system('cls')
    print(text)
    print()


def adding_new_client():
    display_option_titles("Cadastro de novos clientes")
    client_name = input("Digite o nome do cliente que deseja cadastrar: ")
    clients.append(client_name)
    print(f"Cliente {client_name} foi cadastrado com sucesso. ")
    back_to_main_menu()


def show_registered_clients():
    display_option_titles('Listing clients: ')
    for client in clients:
        print(client)
    back_to_main_menu()


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
