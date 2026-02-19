import math

# EXERCICIO 1
nome = input('Digite seu nome completo: ')

maiusculo = nome.upper() 
minusculo = nome.lower() 
conta_caracteres_com_espacos= len(nome)
conta_caracteres_sem_espacos = len(nome.replace(' ', ''))

lista = nome.split()

nome_novo = ' '.join(lista[:-1]) + ' do Inatel'
print('Versão Inatel: {}'.format(nome_novo))

print('Maiúsculo: {}'.format(maiusculo))
print('Minúsculo: {}'.format(minusculo))
print('Total de caracteres (com espaços): {}'.format(conta_caracteres_com_espacos))
print('Total de caracteres (sem espaços): {}'.format(conta_caracteres_sem_espacos))
print('Versão Inatel: {}'.format(nome_novo))

#EXERCICIO2
while True:
    entrada = input('Digite um número para calcular a tabuada: ') 
    if entrada.replace('.', '', 1).isdigit(): 
        tabuada = float(entrada) 
        break
    print('Erro! Digite um número válido.')

while True:
    entrada = input('Começar em (inteiro): ')
    if entrada.isdigit():
        iniciar = int(entrada) 
        break
    print('Erro! Digite um número inteiro.')

while True:
    entrada = input('Terminar em (inteiro): ')
    if entrada.isdigit():
        terminar = int(entrada)
        break
    print('Erro! Digite um número inteiro.')

print('\nTabuada do {} (de {} até {}):'.format(tabuada, iniciar, terminar)) 

if iniciar <= terminar:
    passo = 1   #tabuada crescente
else:
    passo = -1  #tabuada decrescente

for i in range(iniciar, terminar + passo, passo): 
    resultado = tabuada * i 
    print('{} x {:2} = {:.1f}'.format(tabuada, i, resultado)) 

#EXERCICIO3
sexo = input('Insira M para Masculino ou F para Feminino: ').strip().upper()
while sexo != 'M' and sexo != 'F':
    print('Entrada inválida!')
    sexo = input('Por favor, insira M para Masculino ou F para Feminino: ').strip().upper()

if sexo == 'M':
    print('Homem')
else:
    print('Mulher')

#EXERCICIO4
while True:
    entrada = input('Distância da viagem (Km): ')
    if entrada.replace('.', '', 1).isdigit():
        distancia = float(entrada)
        if distancia > 0:
            break
    print('Entrada inválida! Digite um número positivo.')

if distancia <= 200:
    preco = distancia * 0.50 
else:
    preco = distancia * 0.45 

print('O preço da passagem é: R$ {:.2f}'.format(preco))

#Exercicio5
while True: 
    entrada = input('Digite um número entre 1000 e 9999: ')
    
    if entrada.isdigit():
        numero = int(entrada)
        
        if 1000 <= numero <= 9999:
            break 
            
    print('Entrada inválida! Tente novamente.')

unidade = numero % 10 
dezena = (numero % 100) // 10 
centena = (numero % 1000) // 100
milhar = numero // 1000

print('Unidade: {}'.format(unidade))
print('Dezena: {}'.format(dezena))
print('Centena: {}'.format(centena))
print('Milhar: {}'.format(milhar))

#Exercicio6
while True:
    entrada = input('Entre com um número decimal: ')
    try:
        numero = float(entrada)  # Aceita decimal
        if numero >= 0:  # Raiz quadrada só de números não negativos
            break
        print('Número deve ser não negativo para raiz quadrada!')
    except ValueError:
        print('Entrada inválida! Digite um número decimal.')

resultado = math.sqrt(numero)

print('A raiz quadrada de {} é {:.4f}'.format(numero, resultado))
print('A função teto de {} é {}'.format(numero, math.ceil(numero)))
print('A função chão de {} é {}'.format(numero, math.floor(numero)))
print('A parte inteira de {} é {}'.format(numero, math.trunc(numero)))
