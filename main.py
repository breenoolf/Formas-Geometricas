from formageometrica import Circulo, Quadrado, Triangulo, Trapezio, Losango, calcular_circulo, calcular_losango, calcular_quadrado, calcular_trapezio, calcular_triangulo
import os
import platform

def main():
    while True:
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
            print('Escolha indisponível')
if __name__ == '__main__':
    main()