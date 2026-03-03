# Cap.4 - EXERCICIOS
import numpy as np

#Exercicio1
print('Exercicio1')
arr1 = np.ones(8, dtype=int) #trabalhar c/ numeros inteiros acrescentra dtype=int
arr2 = np.random.randint(0, 10, 8) #(l,h,s) l-Low(inclusive), h-high(exclusive), s-(size)
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
    
arr3 = arr1 + arr2 
soma_total = arr3.sum()

print(f"Array Resultante: {arr3}")
print(f"Soma Total: {soma_total}")

if soma_total >= 40:
    matriz = arr3.reshape(4, 2)
    print("Reshape aplicado: 4x2 (Mais linhas que colunas)")
else:
    matriz = arr3.reshape(2, 4)
    print("Reshape aplicado: 2x4 (Mais colunas que linhas)")

print(matriz)

#Exercicio2
print('\nExercicio2')
arr1 = np.arange(0, 52, 2) #Pares de 0 a 51 -> 0(inclusive) a 51(exclusive coloco 52), incremento 2 em 2 
arr2 = np.arange(100, 49, -2) #Pares de 100 até 50 -> 100 inclusive e 49 (exclusive para 50) de -2 a -2
print(f"Array 1: {arr1}")
print(f"Array 2: {arr2}")
 
concatenado = np.concatenate((arr1, arr2))
print(f"Array Concatenado: {concatenado}")

ordenado = np.sort(concatenado)
print(f"Array Ordenado: {ordenado}")

#Exercicio3
print('\nExercicio3')
np.random.seed() # Semente livre para cada jogo ser diferente
campo_real = np.zeros([2, 2])
tabuleiro_visu = np.array([['?', '?'], ['?', '?']]) # Matriz visual de strings

l_bomba = np.random.randint(0, 2)
c_bomba = np.random.randint(0, 2)
campo_real[l_bomba, c_bomba] = 1

#print(f"[DEBUG] A bomba está na Linha {l_bomba}, Coluna {c_bomba}")

# Controle do jogo
jogadas_feitas = [] # Lista para evitar repetição
acertos = 0

print("##### MINI CAMPO MINADO #####\n")
print(tabuleiro_visu) # Mostra o estado inicial

while acertos < 3:
    try:
        lin = int(input("\nEscolha a Linha (0 ou 1): "))
        col = int(input("Escolha a Coluna (0 ou 1): "))

        # Validação 1: Posição repetida
        if (lin, col) in jogadas_feitas:
            print("Você já jogou nessa posição! Escolha outra.")
            continue

        # Validação 2: Fora dos limites da matriz 2x2
        if lin not in [0, 1] or col not in [0, 1]:
            print("Posição inválida! Use apenas 0 ou 1.")
            continue

        # Verificação de Bomba
        if campo_real[lin, col] == 1:
            tabuleiro_visu[lin, col] = '*' # Marca a bomba
            print(tabuleiro_visu)
            print("\n BOOM! Game Over! :( Try Again!\n")
            break
        else:
            # Jogada segura
            tabuleiro_visu[lin, col] = 'v' # 'v' de vazio/visitado
            jogadas_feitas.append((lin, col))
            acertos += 1
            print("Posição segura!")
            print(tabuleiro_visu) # Exibe o tabuleiro atualizado

    except ValueError:
        print("Entrada inválida! Digite apenas números inteiros.")

if acertos == 3:
    print("\nCongratulations! You beat the game! :)\n")

#Exercicio4
print('Exercicio4')
l, c = np.random.randint(1, 11, 2)
mtz = np.random.randint(1, 100, [l, c])

linhas, colunas = mtz.shape 
total_elementos = mtz.size 

paridade = "par" if total_elementos % 2 == 0 else "ímpar"

print(f"Matriz Gerada: {linhas} linhas x {colunas} colunas")
print(f"Total de elementos: {total_elementos}")
print(f"Essa matriz poderia se tornar um vetor unidimensional com número {paridade} de elementos.")

#vetor_exemplo = mtz.reshape(1, total_elementos)
#print(f"Formato do vetor após reshape: {vetor_exemplo.shape}\n")

#Exercicio 5
print("\nExercicio 5")

np.random.seed(10)
mtz = np.random.randint(1, 51, [4, 4])

print("Matriz 4x4:")
print(mtz)

# Média das linhas
media_linhas = mtz.mean(axis=1)

# Média das colunas
media_colunas = mtz.mean(axis=0)

print("Média das Linhas:", media_linhas)
print("Média das Colunas:", media_colunas)

print("Maior média das linhas:", media_linhas.max())
print("Maior média das colunas:", media_colunas.max())

valores, contagens = np.unique(mtz, return_counts=True)

#print("\nFrequência de cada valor:")
#for i in range(len(valores)):
#    print("Valor:", valores[i], "| Ocorrências:", contagens[i])

frequencia_map = dict(zip(valores, contagens))

print("\nRelatório de Frequência (Dicionário):")

for num, qtd in frequencia_map.items():
    print(f"O número {num:2} apareceu {qtd} vez(es)")

filtro_dois = (contagens == 2) 
print(f"\nNúmeros que aparecem exatamente 2 vezes: {valores[filtro_dois]}")
