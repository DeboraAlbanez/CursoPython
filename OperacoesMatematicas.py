"""
num1 = int(input("Primeiro numero: "))
num2 = int(input("Segundo numero: "))

print(f' Soma: {num1 + num2}')

print(f' Subtração: {num1 - num2}')

print(f' Multiplicação: {num1 * num2}')

print(f' Divisão: {num1 / num2}') #10/3 = 3.3333 - Float

print(f' Divisão (inteiro): {num1 // num2}') #resultado arredondado para inteiro

print(f' Potenciação: {num1 ** num2}')


#Operação com Strings

nome = 'Geremias '
print(nome * 3)

sobrenome = 'da Silva'
NomeCompleto = nome + sobrenome
print(NomeCompleto)

print(True * False)
print(True * True)


print(bool('urso'))
print(float('urso'))



N1 = int(input("Digite a N1: "))
N2 = int(input("Digite a N2: "))
N3 = int(input("Digite a N3: "))
N4 = int(input("Digite a N4: "))
MEDIA = (N1 + N2 + N3 + N4)/4
print (f' A média das Notas é: {MEDIA}')


Celsius = float(input("Digite a temperatura em Celsius: "))
F = (Celsius * 1.8) + 32
K = Celsius + 273.15

print(f' Temperatura em ºF: {F}')
print(f'Temperatura em K:  {K}')



Celsius = float(input("Digite a temperatura em Celsius: "))
F = Celsius * 1.8 + 32
K = Celsius + 273.15

print(f' Temperatura em ºF: {F}')
print(f'Temperatura em K:  {K}')



nome = "Mark"
print(int(nome)) #não é possível transformar letras em números


frase = "EU SOU SEU PAi"
print(frase[-1::])


#Personagem Ficção

CorCabelo = input("Digite a Cor do Cabelo:  ")
CorPele = input("Digite a Cor de pele:  ")
Classe = input("Escolha entre: 1-Guerreiro / 2-Mago /3-Arqueiro \n Digite: ")
Idade = int(input("Digite a idade: "))
Altura = float(input("Digite a altura: "))
HabilidadeEspecifica = input("Digite a habilidade: ")

print(f' Personagem Escolhido:  \n '
      f'Cabelo: {CorCabelo} \n'
      f'Pele: {CorPele} \n'
      f'Classe: {Classe} \n'
      f'Idade: {Idade} \n'
      f'Altura: {Altura} \n'
      f'Habilidade: {HabilidadeEspecifica} \n')
"""

#Calculadora

op = int(input("Escolha uma operação: \n "
      "1 - Soma \n "
      "2 - Subtração \n"
      "3 - Divisão \n"
      "4 - Multiplicação \n"
      "5 - Potência \n"
      "Escolha: "))
num1 = int(input("Digite o primeiro número: "))
num2 = int(input("Digite o segundo número: "))

if op == 1:
    print(f'Soma: {num1 + num2}')
elif op == 2:
    print(f'Subtração: {num1 - num2}')
elif op == 3:
    print(f'Divisão: {num1 / num2}')
elif op == 4:
    print(f'Multiplicação: {num1 * num2}')
elif op == 5:
    print(f'Potência: {num1 ** num2}')
else:
      ("Opção inválida. Escolha uma opção válida! ")