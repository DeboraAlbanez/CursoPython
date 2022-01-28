"""

list = [1,5,3,True, 'Sim']
print(True not in list)



numero = range(1,50) #intervalo de 1 a 49
print(numero)


#Aplicação String
seriado = 'Todo mundo odeia o Chris'
for letra in seriado: #para cada letra dentro de seiado faça:
    print(letra, end='')

#Aplicação com Lista

numeros = [1,2,'oi', True]
for elemento in numeros:
    print(elemento)


#Aplicação com Range

intervalo_num = range(3,11)
for numero in intervalo_num:
    print(numero, end='')


soma =0
num = int(input("Digite um número: "))
for n in range(1, num+1):
    if num % num == 0:
        soma = soma + num
        print(soma)



num = int(input("Digite um número: "))
for num in range (1, num+1):
    print(f'{5*num}')


for numero in range(2,20):
    if numero % 2 == 0:
        print(f'Número par! {numero}')


##para cada letra dentro de fruta, se a letra for igual a 'a', imprime a letra 'a'
#vai imprimir 9 vezes, pois o range é e 1 a 3, entao para cada letra a encontrada, imprime 3 vezes.
fruta = 'abacate'
valor = range(1,4)
for letra in fruta:
    if letra == 'a':
        for num in valor:
            print('Achei a letra a')




string= 'abcdefghijkl'
for letra in string:
    print(letra, end='/')
    if letra =='g':
       continue


heroi = 'Batman'
for valor in enumerate(heroi):
    print(valor)
for contador, letra in enumerate(heroi):
    print(f'A {contador+1} letra e: {letra}')
for valor in enumerate(range(3,7)):
    print(valor)



rua = 'Figueira Branca'
#for letra in enumerate(rua):
 #   print(letra)
for contador, letra in enumerate(rua):
    print(f' A {contador+1} letra é: {letra}')
#for letra in enumerate(range(3,7)):
 #   print(letra)



soma = 0
numero = int(input("Digite um numero: "))
for num in range(1, numero+1):
    if numero % num == 0:
        soma = soma+num
        print(num)
        print(soma)

        numero = int(input('Digite o numero de multiplos de 5 que deseja: '))
        # Recebe numero como inteiro para entrar no range()
        for num in range(1, numero + 1):  # Para cada num no intervalo de 1 a
            # numero+1 faça:
            print(f'{5 * num}')  # Imprime 5 vezes num


soma = 0 # Inicializa variavel soma
numero = int(input('Digite o numero: ')) #Pede o numero para o usuario
for num in range(1,numero+1): #Para cada num dentro do intervalo 1 e
 #numero+1 faça:
    if numero % num == 0: #Se o resto da divisão de numero por num for
 #zero faça:
        soma = soma + num #atualiza soma com num
        print(num) #Imprime a soma final




numero = int(input("Digite um numero: "))

for num in range (1,numero+1):
    print(num*5)


list = ['Boeing 700', 'Boeing 800']

print (len('Boeing 700'))

nome = 'Madalena'

print (len(nome))


n = int(input("Digite um valor de 0 a 10: "))
for num in range(1,n+1):
        if n <= 10:
               break
        else:
            print("Insira um valor válido!")
        break

classic_cars = ["Pierce Arrow", "Oldsmobile", "Mustang"]

for car in classic_cars:
   print(car)

    print(car)



sports_cars = ["Agera", "Regera", "Chiron", "Veyron"]

for car in sports_cars:
    print (car)



num_list = [100,800,330,220,400,900,1110]
for num in num_list:
    if num < 500:
        print(f'Menor que 500' , num)
    else:
        print("Maior que 500", num)


list = range(-4,8)
for numero in list:
    print(numero, end=',')




for i in range(6):
    print(i)



for i in range(2,11,2):
    print(i)



for _ in range(7):
    print("Python is great")



x = True
while x:
    print("Estou rodando")
    x = False



pedido = ''

while pedido != "Quero Sair":
    pedido = input("Você não vai sair? ")
    #enquanto usuário não informar que quer sair, o loop continuará



contador = 0
while contador < 9:
    print(contador, end='')
    contador = contador +1
    if contador == 5:
        break #irá parar imediatamente


contador = 0

while contador <9:
    print(contador, end = '')
    contador = contador +1
    if contador ==5:
        continue

"""

#rua = 'Figueira Branca'
#for letra in enumerate(rua):
 #   print(letra)
#for contador, letra in enumerate(rua):
 #   print(f' A {contador+1} letra é: {letra}')
#for letra in enumerate(range(3,7)):
 #   print(letra)

for key, value in enumerate(["p", "y", "t", "h", "o", "n"]):
    print (key, value)
