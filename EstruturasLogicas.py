"""
#AND - TODAS CONDIÇÕES PRECISAM SER VERDADEIRAS

sensor = 58 #range entre 68 e 75

if sensor >= 68 and sensor <= 75:
    print("Sensor OK")
else:
    print("Problema")

agua = True
comida = False

if agua and comida:
    print("Happy")
else:
    print("Bad Dog")

#OR - UMA DAS CONDIÇÕES PRECISA SER VERDADEIRA

pizza = True
lasanha = False

if pizza or lasanha:
    print("Preciso comer mais salada! ")
else:
    ("Estou com fome")

num = 21

if num % 2 == 0 or num < 10:
    print ("é par ou menor que 10")
else:
    print("Ímpar ou maior ou igual a 10")



#IS COMPARAÇÃO VALORES

login = False
#print(login is True) #False, porque está declarado como falso.
#print(login is False) #True

if login is False:
    print('logado')
else:
    print('deslogado')


#NOT - INVERSÃO DE VALOR

login = True

if not login: #Não falso, verdadeiro
    print('deslogado')
else:
    print('logado')



#Exercício Cadastro em um site

login = False
print("Faça seu cadastro! ")
user = input("Crie seu usuário:  ")
password = input("Crie sua senha: ")

print ("----------Login-------------------")
if input("Usuário:") == user and input("Password: ") == password:
    login = True

if login == True:
    print("Bem-Vindo à Cultura Inglesa")
else:
    print("Tente novamente")


login = False
print("Faça seu cadastro! ")
user = input("Crie seu usuário:  ")
password = input("Crie sua senha: ")

print ("----------Login-------------------")
if input("Usuário:") == user and input("Password: ") == password:
    login = True

if not login :
    print("Bem-Vindo à Cultura Inglesa")
else:
    print("Tente novamente")

"""

##Fórmula de Bhaskara

a = int(input("Digite O valor da letra A: "))
b = int(input("Digite O valor da letra B: "))
c = int(input("Digite O valor da letra C: "))
delta = (b**2)-(4*a*c)
x1 = (-b+delta**0.5)/(2*a)
x2 = (-b-delta**0.5)/(2*a)

print(f'As raízes são: {x1} e {x2}')

