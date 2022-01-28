"""
#Acesso Brinquedo Parque

altura = float(input("Digite sua altura: "))

if altura < 1.6:
    print(f'Brinquedo não permitido para sua altura')
else:
    print(f'Acesso permitido!')



#Média Final

Nota1 = int(input("Digite a primeira nota: "))
Nota2 = int(input("Digite a segunda nota: "))
Nota3 = int(input("Digite a terceira nota: "))
Nota4 = int(input("Digite a quarta nota: "))
MediaFinal = ((Nota1 + Nota2 + Nota3 + Nota4)/ 4)

if MediaFinal >= 5:
    print(f' {MediaFinal}  - Aprovado! ')
else:
    print(f' {MediaFinal}  - Reprovado! ')



#MaiorNumero

N1 = int(input("Digite 1 número: "))
N2 = int(input("Digite 1 número: "))

if N1 > N2:
    print(f'O maior número é?: {N1}')
else:
    print(f'O maior número é: {N2}')



N = int(input("Digite um número: "))

if N < 0:
    print(f' Número negativo! {N} ')
else:
    print(f' Número positivo! {N} ')



SEXO = input("Digite F para feminino e M para Masculino: \n")

if SEXO == 'F':
    print("Feminino")
elif SEXO == 'M':
    print("Masculino")
else:
    print("Sexo inválido! ")



Vogal = ["a", "e", "i", "o", "u"]
Letra = input('Digite uma letra: ')

if Letra in Vogal:
    print("Vogal")
else:
    print("Consoante")



NOTA1 = int(input("Digite a primeira nota: "))
NOTA2 = int(input("Digite a segunda nota: "))
MEDIA = (NOTA1 +NOTA2)/2

if MEDIA >= 7 and MEDIA < 10:
    print("Aprovado")
elif MEDIA == 10:
    print("Aprovado com Distinção")
else:
    print("Reprovado")



N1 = int(input("Digite um nº: "))
N2 = int(input("Digite um nº: "))
N3 = int(input("Digite um nº: "))

if N1 > N2 and N1 > N3:
    print(N1)
elif N2 > N1 and N2 > N3:
    print(N2)
else:
    print(N3)




pais = input("Digite um país que vc deseja visitar: ")

if pais ==  "Noruega":
    print("Ah não, muito frio!")
elif pais == "China":
    print("Muito Longe")
elif pais == "Austrália":
    print("Muito canguru! ")
else:
    print("Bora")


login = False
senha = "Caneta1"

key = input("Digite sua senha: ")

if key == senha:
    login = True
else:
    print("Senha incorreta! ")

if login == True:
    print("Bem vindo admin")
else:
    print("Tente novamente! ")



senha = "Caneta1"
key = "Canet"

if key == senha:
    login = True
else:
    print("Senha incorreta")

if login == True:
    print("Bem-vindo admin")
else:
    print("Tente novamente")

n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)

#----verificar para trazer o menor numero
n1 = int(input("Digite um número: "))
n2 = int(input("Digite um número: "))
n3 = int(input("Digite um número: "))

if n1 > n2 and n1 > n3:
    print(n1)
elif n2 > n1 and n2 > n3:
    print(n2)
else:
    print(n3)

if n1 < n2 and n1 < n3:
    print(n1)
elif n2 < n1 and n2 < n3:
    print(n2)
else:
    print(n3)




# CALCULAR AUMENTO EM PORCENTAGEM
salario = float(input("Digite seu salário:"))
acrescimo = float(input("Informe a % do aumento obtido:"))
porcentagem = acrescimo/100
aumento = salario + (porcentagem*salario)
print (f'Seu aumento foi de: {(porcentagem*salario)} ')
print (f'Seu aumento foi de salário atual é : {aumento} ')
"""


# CALCULAR DESCONTO EM PRODUTO
ValorProduto = float(input("Digite o valor do Produto:"))
DescontoProduto = float(input("Informe o desconto:"))
porcentagem = DescontoProduto/100
ValorComDesconto = ValorProduto - (porcentagem*ValorProduto)
print (f'Seu desconto foi de: {(porcentagem*ValorProduto)} ')
print (f'Seu aumento foi de salário atual é : {ValorComDesconto} ')

