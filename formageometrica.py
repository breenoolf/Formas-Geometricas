from abc import ABC, abstractmethod
import math
import os
import platform
# class FormaGeometrica3D(ABC):
#     @abstractmethod
#     def calculo_area (self):
#         pass
#     @abstractmethod
#     def calculo_perimetro (self):
#         pass
#     @abstractmethod
#     def calculo_volume (self):
#         pass
#     def area_lateral (self):
#         pass
class FormaGeometrica2D (ABC):
    @abstractmethod
    def calculo_area (self):
        pass
    @abstractmethod
    def calculo_perimetro (self):
        pass
    
def calcular_quadrado():
    try:
        calculo = input('Qual cálculo deseja fazer? 1 - Área | 2 - Perímetro')
        q1 = Quadrado(int(input('Digite o valor do lado deste quadrado: ')))
        if calculo == 1:
            print(q1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            print(q1.calculo_perimetro())
            limpar_terminal()
    except:
        print('ERRO! Insira os valores corretamente.')
        limpar_terminal()
def calcular_circulo(self):
    try:
        calculo = input('Qual cálculo deseja fazer? 1 - Área | 2 - Perímetro')
        c1 = Circulo(int(input('Digite o valor do raio deste cícrulo: ')))
        if calculo == 1:
            c1.calculo_area()
            limpar_terminal()
        elif calculo == 2:
            print(c1.calculo_perimetro())
            limpar_terminal()
    except:
        print('ERRO! Insira os valores corretamente.')
        limpar_terminal()
# def calcular_triangulo():
#     try:
#         calculo = int(input('Qual cálculo deseja fazer? 1 - Área | 2 - Perímetro'))
#         t1 = (input('Digite o valor da base e da altura deste triângulo: '))
#         base_str, altura_str = map(int, t1.split())
#         t1 = Triangulo(base_str, altura_str)
#         if calculo == 1:
#             print(t1.calculo_area())
#             limpar_terminal()
#         elif calculo == 2:
#             print(t1.calculo_perimetro())
#             limpar_terminal()
#     except:
#         print('ERRO! Insira os valores corretamente.')
#         limpar_terminal()
def calcular_trapezio():
    try:
        calculo = input('Qual cálculo deseja fazer? 1 - Área | 2 - Perímetro')
        tra1 = input('Digite o valor da base menor, base maior, dos dois lados e da altura: ')
        base_menor, base_maior, lado1, lado2, altura = map(int, tra1.split())
        tra1 = Trapezio(base_menor, base_maior, lado1, lado2, altura)
        if calculo == 1:
            print(tra1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            print(tra1.calculo_perimetro())
            limpar_terminal()
    except:
            print('ERRO! Insira todos os valores')
            limpar_terminal()
def calcular_losango():
    try:
        calculo = input('Qual cálculo deseja fazer? 1 - Área | 2 - Perímetro')
        l1 = input('Digite o valor da diagonal maior e menor, e do lado:')
        diagonal_maior, diagonal_menor, lado = map(int, l1.split())
        l1 = Losango(diagonal_maior, diagonal_menor, lado)
        if calculo == 1:
            print(l1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            print(l1.calculo_perimetro())
            limpar_terminal()
    except:
        print('ERRO! Insira todos os valores')
        limpar_terminal()

class Circulo(FormaGeometrica2D):
    def __init__(self, raio):
        self.raio = raio
        super().__init__()
    def get_raio (self):
        return self.raio
    def set_raio (self, novo_raio):
        self.raio = novo_raio
    def calculo_perimetro(self):
        perimetro = 2 * math.pi * self.raio
        return f'O valor do perímetro deste círculo é {perimetro}' 
    def calculo_area(self):
        area = math.pi * (self.raio**2)
        return f'O valor da área deste círculo é {area}'
    
class Quadrado (FormaGeometrica2D):
    def __init__(self, lado):
        self.lado = lado
        super().__init__()
    def get_lado (self):
        return self.lado
    def set_lado (self, novo_lado):
        self.lado = novo_lado
    def calculo_perimetro(self):
        perimetro = self.lado * 4
        return f'O valor do perímetro deste quadrado é {perimetro}'
    def calculo_area(self):
        area = self.lado**2
        return f'O valor da área deste quadrado é {area}'

class TrianguloEquilatero (FormaGeometrica2D):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
        super().__init__()
    def get_base (self):
        return self.base
    def set_base(self, nova_base):
        self.base = nova_base
    def get_altura (self):
        self.altura
    def set_altura (self, nova_alutra):
        self.altura = nova_alutra
    def calculo_area(self):
        area = (self.base*self.altura)/2
        return f'O valor da área deste triângulo é {area}'
    def calculo_perimetro(self):
        perimetro = self.base * 3
        return f'O valor do perímetro deste triângulo é {perimetro}'
class TrianguloRetangulo(FormaGeometrica2D):
    def __init__(self, cateto1, cateto2):
        self.cateto1 = cateto1
        self.cateto2 = cateto2
        super().__init__()
    def get_cateto1(self):
        return self.cateto1
    def set_cateto1 (self, novo_cateto1):
        self.cateto1 = novo_cateto1
    def get_cateto2(self):
        return self.cateto2
    def set_cateto(self, novo_cateto2):
        self.cateto2 = novo_cateto2
    def calculo_area(self):
        area = (self.cateto1 * self.cateto2)/2
        return f'O valor da área deste triângulo é {area}'
    def calculo_perimetro(self):
        hipotenusa = math.sqrt(self.cateto1**2 + self.cateto2**2)
        perimetro = self.cateto1 + self.cateto2 + hipotenusa
        return f'O valor do perimetro deste triângulo é {perimetro}'
class TrianguloIsoceles(FormaGeometrica2D):
    def __init__(self, lado, base, altura):
        self.altura  = altura
        self.base = base
        self.lado = lado
        super().__init__()
    def get_base(self):
        return self.base
    def set_base(self, nova_base):
        self.base = nova_base
    def get_lado(self):
        return self.lado
    def set_lado(self, novo_lado):
        self.lado = novo_lado
    def calculo_area(self):
        area = (self.base * self.altura)/2
        return f'O valor da área deste triângulo é {area}'
    def calculo_perimetro(self):
        perimetro = self.base + (self.lado*2)
        return f'O valor do perímetro deste triângulo é {perimetro}'

class TrianguloEscaleno(FormaGeometrica2D):
    def __init__(self, lado1, lado2, base):
        self.lado1 = lado1
        self.lado2 = lado2
        self.base = base
        super().__init__()
    def get_lado1(self):
        return self.lado1
    def set_lado1(self, novo_lado1):
        self.lado1 = novo_lado1
    def get_lado2(self):
        return self.lado2
    def set_lado2 (self, novo_lado2):
        self.lado2 = novo_lado2
    def get_base(self):
        return self.base
    def set_base(self, nova_base):
        self.base = nova_base
    def get_altura(self):
        return self.altura
    def set_altura(self, nova_altura):
        self.altura = nova_altura
    def calculo_area(self):
        altura = int(input('Digite o valor da altura: '))
        area = (self.base*altura)/2
        return f'O valor da área deste triângulo é {area}'
    def calculo_perimetro(self):
        perimetro = self.lado1 + self.lado2 + self.base
        return f'O valor do perímetro deste triângulo é {perimetro}'
    
class Elipse(FormaGeometrica2D):
    def __init__(self, raio_maior, raio_menor):
        self.raio_maior = raio_maior
        self.raio_menor = raio_menor
        super().__init__()
    def get_raio_menor (self):
        return self.raio_menor
    def set_raio_menor(self, novo_raio_menor):
        self.raio_menor = novo_raio_menor
    def get_raio_maior(self):
        return self.raio_maior
    def set_raio_maior(self, novo_raio_maior):
        self.raio_maior = novo_raio_maior
    def calculo_perimetro(self):
        perimetro = 2*(math.pi) * math.sqrt((self.raio_maior * 2 + self.raio_menor * 2) / 2)
        return f'O valor do perímetro desta elipse é {perimetro}'
    def calculo_area(self):
        area = math.pi * self.raio_maior * self.raio_menor
        return f'O valor da área desta elipse é {area}'

class Trapezio (FormaGeometrica2D):
    def __init__(self, base_menor, base_maior, lado1, lado2, altura):
        super().__init__()
        self.base_menor = base_menor
        self.base_maior = base_maior
        self.lado1 = lado1
        self.lado2 = lado2
        self.altura = altura
    def get_base_menor(self):
        return self.base_menor
    def set_base_menor(self, nova_base_menor):
        self.base_menor = nova_base_menor
    def get_base_maior(self):
        return self.base_maior
    def set_base_maior(self, nova_base_maior):
        self.base_maior = nova_base_maior
    def get_lado1 (self):
        return self.lado1
    def set_lado1 (self, novo_lado1):
        self.lado1 = novo_lado1
    def get_lado2(self):
        return self.lado2
    def set_lado2(self, novo_lado2):
        self.lado2 = novo_lado2
    def get_altura(self):
        return self.altura
    def set_altura(self, nova_altura):
        self.altura = nova_altura
    def calculo_perimetro(self):
        perimetro = self.base_maior + self.base_menor + self.lado1 + self.lado2
        return f'O valor do perímetro deste trapézio é {perimetro}'
    def calculo_area(self):
        area = ((self.base_maior + self.base_menor) * self.altura)/2
        return f'O valor da área deste trapézio é {area}'

class Losango (FormaGeometrica2D):
    def __init__(self, diagonal_maior, diagonal_menor, lado):
        self.diagonal_maior = diagonal_maior
        self.diagonal_menor = diagonal_menor
        self.lado = lado
        super().__init__()
    def get_diagonal_menor(self):
        return self.base_menor
    def set_diagonal_menor(self, nova_diagonal_menor):
        self.diagonal_menor = nova_diagonal_menor
    def get_diagonal_maior(self):
        return self.diagonal_maior
    def set_diagonal_maior(self, nova_diagonal_maior):
        self.diagonal_maior = nova_diagonal_maior
    def get_lado (self):
        return self.lado
    def set_lado (self, novo_lado):
        self.lado = novo_lado
    def calculo_area(self):
        area = (self.diagonal_maior * self.diagonal_menor)/2
        return f'O valor da área deste losango é {area}'
    def calculo_perimetro(self):
        perimetro = self.lado*4
        return f'O valor do perímetro deste losango é {perimetro}'
    
def calcular_quadrado():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
        if calculo == 1:
            q1 = Quadrado(int(input('Digite o valor do lado deste quadrado: ')))
            print(q1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            q1 = Quadrado(int(input('Digite o valor do lado deste quadrado: ')))
            print(q1.calculo_perimetro())
            limpar_terminal()
        else:
            print('ERRO! Digite um dos valores correspondentes.')
            limpar_terminal()
    except ValueError:
        print('ERRO! Insira apenas valores inteiros.')
        limpar_terminal()
def calcular_circulo():
    try:
        calculo = int(input('Qual cálculo deseja fazer? (1 - Área, 2 - Perímetro): '))
        if calculo == 1:
            c1 = Circulo(int(input('Digite o valor do raio deste círculo: ')))
            print(c1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            c1 = Circulo(int(input('Digite o valor do raio deste círculo: ')))
            print(c1.calculo_perimetro())
            limpar_terminal()
        else:
            print('ERRO! Digite um dos valores correspondentes.')
            limpar_terminal()
    except ValueError:
        print('ERRO! Insira apenas valores inteiros.')
        limpar_terminal()

def calcular_triangulo_equilatero():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
        if calculo == 1:
            t1 = (input('Digite o valor da base e da altura deste triângulo: '))
            base_str, altura_str = map(int, t1.split())
            t1 = TrianguloEquilatero(base_str, altura_str)
            print(t1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            t1 = (input('Digite o valor da base e da altura deste triângulo: '))
            base_str, altura_str = map(int, t1.split())
            t1 = TrianguloEquilatero(base_str, altura_str)
            print(t1.calculo_perimetro())
            limpar_terminal()
        else:
            print('ERRO! Digite um dos valores correspondentes.')
            limpar_terminal()
    except ValueError:
        print('ERRO! Insira apenas valores inteiros.')
        limpar_terminal()
def calcular_triangulo_retangulo():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
        if calculo == 1:
            t1 = (input('Digite o valor dos catetos deste triângulo: '))
            cateto1, cateto2 = map(int, t1.split())
            t1 = TrianguloEquilatero(cateto1, cateto2)
            print(t1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            t1 = (input('Digite o valor da base e da altura deste triângulo: '))
            cateto1, cateto2 = map(int, t1.split())
            t1 = TrianguloEquilatero(cateto1, cateto2)
            print(t1.calculo_perimetro())
            limpar_terminal()
        else:
            print('ERRO! Digite um dos valores correspondentes.')
            limpar_terminal()
    except ValueError:
        print('ERRO! Insira apenas valores inteiros.')
        limpar_terminal()

def calcular_triangulo_isoceles():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
        if calculo == 1:
            t1 = (input('Digite o valor da base e da altura deste triângulo: '))
            base, altura = map(int, t1.split())
            t1 = TrianguloIsoceles(base, altura)
            print(t1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            t1 = (input('Digite o valor da base e do lado deste triângulo: '))
            base, lado = map(int, t1.split())
            t1 = TrianguloIsoceles(base, lado)
            print(t1.calculo_perimetro())
            limpar_terminal()
        else:
            print('ERRO! Digite um dos valores correspondentes.')
            limpar_terminal()
    except ValueError:
        print('ERRO! Insira apenas valores inteiros.')
        limpar_terminal()

def calcular_triangulo_escaleno():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
        if calculo == 1:
            t1 = (input('Digite o valor dos lados e da base deste triângulo: '))
            lado1, lado2, base = map(int, t1.split())
            t1 = TrianguloEscaleno(lado1, lado2, base)
            print(t1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            t1 = (input('Digite o valor dos deste triângulo: '))
            lado1, lado2, base = map(int, t1.split())
            t1 = TrianguloEscaleno(lado1, lado2, base)
            print(t1.calculo_perimetro())
            limpar_terminal()
        else:
            print('ERRO! Digite um dos valores correspondentes.')
            limpar_terminal()
    except ValueError:
        print('ERRO! Insira apenas valores inteiros.')
        limpar_terminal()

def calcular_triangulo():
    try:
        triangulo = int(input('Digite qual tipo de triângulo deseja calcular: '))
        if triangulo == 1:
            calcular_triangulo_equilatero()
        elif triangulo == 2:
            calcular_triangulo_retangulo()
        elif triangulo == 3:
            calcular_triangulo_isoceles()
        elif triangulo == 4:
            calcular_triangulo_escaleno()
        else:
            print('ERRO! Opção inválida, escolha uma das opções disponíveis')
            limpar_terminal()
    except ValueError:
        print('ERRO! Insira apenas valores inteiros.')
        limpar_terminal()


def calcular_trapezio():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
        if calculo == 1:
            tra1 = input('Digite o valor da base menor, base maiorr, dos dois lados e da altura: ')
            base_menor, base_maior, lado1, lado2, altura = map(int, tra1.split())
            tra1 = Trapezio(base_menor, base_maior, lado1, lado2, altura)
            print(tra1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            tra1 = input('Digite o valor da base menor, base maior, dos dois lados e da altura: ')
            base_menor, base_maior, lado1, lado2, altura = map(int, tra1.split())
            tra1 = Trapezio(base_menor, base_maior, lado1, lado2, altura)
            print(tra1.calculo_perimetro())
            limpar_terminal()
        else:
            print('ERRO! Digite um dos valores correspondentes.')
            limpar_terminal()
    except ValueError:
        print('ERRO! Insira apenas valores inteiros.')
        limpar_terminal()
def calcular_losango():
    try:
        calculo = int(input('Qual cálculo deseja fazer? 1 - Área | 2 - Perímetro\nValor escolhido: '))
        if calculo == 1:
            l1 = input('Digite o valor da diagonal maior e menor, e do lado:')
            diagonal_maior, diagonal_menor, lado = map(int, l1.split())
            l1 = Losango(diagonal_maior, diagonal_menor, lado)
            print(l1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            l1 = input('Digite o valor da diagonal maior e menor, e do lado:')
            diagonal_maior, diagonal_menor, lado = map(int, l1.split())
            l1 = Losango(diagonal_maior, diagonal_menor, lado)
            print(l1.calculo_perimetro())
            limpar_terminal()
        else:
            print('ERRO! Digite um dos valores correspondentes.')
            limpar_terminal()
    except ValueError:
        print('ERRO! Insira apenas valores inteiros.')
        limpar_terminal()
def limpar_terminal():
    input('Digite ENTER para voltar ao menu principal')
    system = platform.system()
    if system == 'Windows':
        os.system('cls') 
    else:
        os.system('clear')