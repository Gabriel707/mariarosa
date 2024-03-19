import os


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


def chosen_option():
    try:
        user_option = int(input("Escolha uma opção: "))
        print(f"Opcão escolhida: {user_option}")

        if user_option == 1:
            print("Cadastrando usuario")
        elif user_option == 2:
            print("Clientes presentes na base de dados: ")
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
