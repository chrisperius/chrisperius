#pedra,papel ou tesouro contra o computador



opcoes_do_jogo = ['pedra', 'papel', 'tesoura']
selecao_do_computador = random.choice(opcoes_do_jogo)
selecao_do_usuário = opcoes_do_jogo[int(input(' Escolha entre pedra, papel ou tesoura: \n 1. pedra \n 2. papel \n 3. tesoura \n'))-1]

if selecao_do_usuário == selecao_do_computador:
    print(' Empate! ')
elif selecao_do_usuário == 'pedra' and selecao_do_computador == 'tesoura':
    print(' Você ganhou! ')
elif selecao_do_usuário == 'papel' and selecao_do_computador == 'pedra':
    print('Você ganhou!')
elif selecao_do_usuário == 'tesoura' and selecao_do_computador == 'papel':
    print('Você ganhou!')
else:
    print(' Você perdeu!')
input(' Pressione ENTER para jogar novamente... ') 
jokenpo()