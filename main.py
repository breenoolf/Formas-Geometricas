from formageometrica import forma2d, forma3d,
def main():
    while True:
        try:
            escolha: int = int(input('1 - Formas Bidimensionais\n2 - Formas Tridimensionais\n0 - Para encerrar o programa\nDigite qual tipo de forma deseja calcular: '))
            if escolha not in range(0, 3):
                raise ValueError("Opção inválida. Escolha um número entre 0 e 2")
            if escolha == 1:
                forma2d()
            elif escolha == 2:
                forma3d()
            else:
                break
        except ValueError as e:
            print(f"Erro: {e}. Por favor, tente novamente.")
if __name__ == '__main__':
    main()