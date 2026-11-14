from dicionario import funcoes

def escolha_opcao():
    print("O que você deseja fazer/visualizar?\n".center(20, " "))
    for indice, chave in enumerate(funcoes, start=1):
        print(f'{indice}) {chave['nome']}')
    
    while True:
        try:
            escolha = int(input('\nresposta: '))
        except ValueError:
            print("Erro de validação! Digite novamente.")
            continue
        if escolha <1 or escolha > 19:
            print("Escolha um número entre os que estão disponíveis!")
            continue
        else:
            return escolha
def tentar_novamente():
    print("\nDeseja fazer outra análise?[S/N]")
    escolha = str(input(": ")).upper()

    if escolha.startswith('S'):
        escolha_usuario =  escolha_opcao()
        print(f"{funcoes[escolha_usuario - 1]['nome']}".center(20," "))
        print(f'{funcoes[escolha_usuario-1]['funcao']}')
        return tentar_novamente()
    else:
        print("Obrigado por utilizar nosso sistema!")

escolha_usuario = escolha_opcao()

print(f"{funcoes[escolha_usuario - 1]['nome']}".center(20," "))
print(f'{funcoes[escolha_usuario-1]['funcao']}')

escolha_usuario= tentar_novamente()