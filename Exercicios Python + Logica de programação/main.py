'''
1. Olá, Mundo!
   Escreva um programa que mostre na tela a mensagem: 'Olá, Mundo!'.
2. Nome do Usuário
   Peça para o usuário digitar o nome dele e exiba: 'Olá, [nome]!'.
3. Soma Simples
   Peça dois números inteiros ao usuário e mostre a soma.
4. Antecessor e Sucessor
   Leia um número inteiro e mostre seu antecessor e seu sucessor.
5. Dobro do Número
   Peça um número e mostre o dobro dele.
6. Conversor de Metros para Centímetros
   Peça um valor em metros e mostre o resultado em centímetros.
7. Maior de Dois Números
   Leia dois números e diga qual é o maior.
8. Par ou Ímpar
   Leia um número e diga se ele é par ou ímpar.
9. Tabuada Simples
   Peça um número e mostre a tabuada dele até 10.
10. Contagem até N
    Leia um número N e faça a contagem de 1 até N.


'''

#1
print("Olá, Mundo!")

#2
nome = input("Digite seu nome: ")
print("Olá " + nome)

#3
num1 = int(input("Digite um número inteiro: "))
num2 = int(input("Digite outro número inteiro: "))

soma = num1 + num2

print(soma)

#4
numero = int(input("Digite um número inteiro: "))

antecessor = numero - 1
sucessor = numero + 1

print(f"O antecessor do número {numero} é: {antecessor}. E o sucessor deste número é {sucessor}.")

#5
n = int(input("Digite um número inteiro"))

dobro = n * 2

print(f'O dobro de {n} é {dobro}')

#6
metros = float(input("Digite o valor em metros"))

centimetros = metros * 100

print(f'{metros} em centimeros fica {centimetros}.')

#7
numero1 = int(input("Digite um número inteiro"))
numero2 = int(input("Digite outro numero inteiro"))

if(numero1 > numero2):
    print(f"O maior entre {numero1} e {numero2} é o {numero1}")
elif numero2 > numero1:
    print(f"O maior entre {numero1} e {numero2} é o {numero2}")
else:
    print("Os dois números são iguais")


#8
numero3 = int(input("Digite um número inteiro:"))

if(numero3 % 2 == 0):
    print(f"O {numero3} é par")
else:
    print(f"O {numero3} é impar")

#9
tabuada = int(input("Digite um número inteiro para vermos sua tabuada: "))

for i in range(1, 11):
    resultado = tabuada * i
    print(f"{tabuada} x {i} = {resultado}")

#10
contador = int(input("Digite um número: "))
i = 1
while i < contador:
    i+=1
    print(i)