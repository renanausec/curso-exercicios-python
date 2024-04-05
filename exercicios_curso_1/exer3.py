def verifica_user_e_password(user, password):
    if user == 'renanausec' and password =='123456':
        print(f'Usuário logado como {user}. Login efetuado com sucesso!')
    elif user == 'renanausec' and password != '123456':
        print(f'Senha incorreta para o usuario {user}')
    else:
        print(f'Usuário {user} inexistente!')

def main():
    user = input('Digite o usuário: ')
    password = input('Digite sua senha: ')
    verifica_user_e_password(user, password)


if __name__ =='__main__':
    main()