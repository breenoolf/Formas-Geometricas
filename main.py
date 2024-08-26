from formageometrica import forma2d, forma3d, limpar_terminal
def main():
    while True:
        try:
            escolha = int(input('1 - Formas Bidimensionais\n2 - Formas Tridimensionais\n0 - Para encerrar o programa\nDigite qual tipo de forma deseja calcular: '))
            if escolha == 1:
                forma2d()
            elif escolha == 2:
                forma3d()
            elif escolha == 0:
                break
            else:
                print('Escolha indisponível, digite um dos números indicados.')
                limpar_terminal()
        except ValueError:
            print('Entrada inválida! Por favor, digite um número.')
            limpar_terminal()
if __name__ == '__main__':
    main()