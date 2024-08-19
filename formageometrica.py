from abc import ABC, abstractmethod
import math
import os
import platform
class FormaGeometrica2D (ABC):
    @abstractmethod
    def calculo_area (self):
        pass
    @abstractmethod
    def calculo_perimetro (self):
        pass
class FormaGeometrica3D(ABC):
    @abstractmethod
    def calculo_area (self):
        pass
    @abstractmethod
    def calculo_perimetro (self):
        pass
    @abstractmethod
    def calculo_volume (self):
        pass
    def area_lateral (self):
        pass
    
def calcular_quadrado():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
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
        c1 = Circulo(int(input('Digite o valor do raio deste cícrulo: ')))
        calculo = input('Qual cálculo deseja fazer? ')
        if calculo == 1:
            c1.calculo_area()
            limpar_terminal()
        elif calculo == 2:
            print(c1.calculo_perimetro())
            limpar_terminal()
    except:
        print('ERRO! Insira os valores corretamente.')
        limpar_terminal()
def calcular_triangulo():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
        t1 = (input('Digite o valor da base e da altura deste triângulo: '))
        base_str, altura_str = map(int, t1.split())
        t1 = Triangulo(base_str, altura_str)
        if calculo == 1:
            print(t1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            print(t1.calculo_perimetro())
            limpar_terminal()
    except:
        print('ERRO! Insira os valores corretamente.')
        limpar_terminal()
def calcular_trapezio():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
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
        calculo = int(input('Qual cálculo deseja fazer? '))
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

class Triangulo (FormaGeometrica2D):
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
        q1 = Quadrado(int(input('Digite o valor do lado deste quadrado: ')))
        if calculo == 1:
            print(q1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            print(q1.calculo_perimetro())
            limpar_terminal()
    except Exception as e:
        print(f'ERRO! Insira os valores corretamente. {e}')
def calcular_circulo():
    try:
        c1 = Circulo(int(input('Digite o valor do raio deste círculo: ')))
        calculo = int(input('Qual cálculo deseja fazer? (1 - Área, 2 - Perímetro): '))
        if calculo == 1:
            print(c1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            print(c1.calculo_perimetro())
            limpar_terminal()
        else:
            print('Cálculo inválido.')
    except Exception as e:
        print(f'ERRO! Insira os valores corretamente. {e}')

def calcular_triangulo():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
        t1 = (input('Digite o valor da base e da altura deste triângulo: '))
        base_str, altura_str = map(int, t1.split())
        t1 = Triangulo(base_str, altura_str)
        if calculo == 1:
            print(t1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            print(t1.calculo_perimetro())
            limpar_terminal()
    except Exception as e:
        print(f'ERRO! Insira os valores corretamente. {e}')
def calcular_trapezio():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
        tra1 = input('Digite o valor da base menor, base maiorr, dos dois lados e da altura: ')
        base_menor, base_maior, lado1, lado2, altura = map(int, tra1.split())
        tra1 = Trapezio(base_menor, base_maior, lado1, lado2, altura)
        if calculo == 1:
            print(tra1.calculo_area())
            limpar_terminal()
        elif calculo == 2:
            print(tra1.calculo_perimetro())
            limpar_terminal()
    except Exception as e:
        print(f'ERRO! Insira os valores corretamente. {e}')
        limpar_terminal()
def calcular_losango():
    try:
        calculo = int(input('Qual cálculo deseja fazer? '))
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
def limpar_terminal():
    input('Digite ENTER para voltar ao menu principal')
    system = platform.system()
    if system == 'Windows':
        os.system('cls') 
    else:
        os.system('clear')