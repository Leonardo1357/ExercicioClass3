login = int(input('Pressione 1 para login ou 2 para se cadastrar: '))

if(login == 2):
    print('Para se cadastrar siga as seguintes informações.')
    email1 = input('Seu email: ')
    senha1 = input('Sua senha: ')
    confsenha = input("Confirme a senha: ")
    if(confsenha != senha1):
        print('Digite a senha corretamente!')
        senha1 = input('Sua senha: ')
        confsenha = input("Confirme a senha: ")
    print('Cadastro feito! Agora faça o login.')
    email = input('Coloque seu email: ')
    while(email != email1):
        print('Digite o email cadastrado!!')
        email = input("Coloque seu email: ")
        if(email == email1):
            break

    senha = input('Coloque a sua senha: ')
    while(senha != senha1):
        print('Digite a senha corretamente!!')
        senha = input('Coloque a sua senha: ')
        if(senha == senha1):
            break

    print('Login feito com sucesso!')



if(login == 1):
    email = input('Coloque seu email: ')
    senha = input('Coloque a sua senha: ')

