from formageometrica import calcular_circulo, calcular_losango, calcular_quadrado, calcular_trapezio, calcular_triangulo, limpar_terminal
def main():
    while True:
        try:
            escolha = int(input('1 - Quadrado\n2 - Circulo\n3 - Triângulo\n4 - Trapézio\n5 - Losango\n0 - Para encerrar o programa\nDigite qual forma deseja calcular: '))
            if escolha == 1:
                calcular_quadrado()
            elif escolha == 2:
                calcular_circulo()
            elif escolha == 3:
                calcular_triangulo()
            elif escolha == 4:
                calcular_trapezio()
            elif escolha == 5:
                calcular_losango()
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