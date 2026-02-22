# Cap.3 - EXERCICIOS

#Exercicio1
times = ['Real Madrid', 'Manchester', 'Barcelona', 'PSG', 'Liverpool']

print(f"Os 3 primeiros colocados: {times[:3]}") 
print(f"Os ultimos dois colocados: {times[-2:]}") 
print(f"Lista com os times em ordem alfabética: {sorted(times)}") 

if 'Barcelona' in times:
    posicao = times.index('Barcelona') + 1 #Inicia com indice 0, por isso o +1
    print(f"O Barcelona está na {posicao}ª posição.")
else:
    print("O Barcelona não está na lista.")

#Exercicio2
loja1 = {'iPhone 15', 'Galaxy S24', 'Moto G84'}
loja2 = {'iPhone 18', 'Galaxy S24', 'POCO X3 Pro'}

total_modelos = loja1 | loja2 # OU ' | ' (União dos conjuntos)
print(f"Modelos no total: {total_modelos}")

em_ambas = loja1 & loja2 # & Intersecçao
print(f"Disponíveis em ambas as lojas: {em_ambas}")

#Exerccicio3
aluno = {}
aluno['nome'] = input("Digite o nome do aluno: ")

while True:
    try:
        media = float(input("Digite a média (0 a 100): "))
        if 0 <= media <= 100:
            aluno['media'] = media
            break 
        else:
            print("Erro: A média deve estar entre 0 e 100.")

    except ValueError:
        print("Entrada inválida! Por favor, digite apenas números.")

if aluno['media'] >= 50:
    aluno['situacao'] = 'AP'
else:
    aluno['situacao'] = 'RP'

for k, v in aluno.items(): 
    print(f"{k}: {v}")

#Exercício4
    pessoas = []

for i in range(3):
    nome = input(f"Nome da {i+1}ª pessoa: ")
    while True:
        try: 
            peso = float(input(f"Peso da {i+1}ª pessoa(Kg): "))
            if peso > 0:
                break
            else:
                print("Erro: O peso deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")
        
    pessoas.append({'nome': nome, 'peso': peso})

pesada = max(pessoas, key=lambda p: p['peso'])
leve = min(pessoas, key=lambda p: p['peso'])

print(f"Pessoa mais pesada: {pesada['nome']} com {pesada['peso']} kg")
print(f"Pessoa mais leve: {leve['nome']} com {leve['peso']} kg")

#Exercicio5
pessoas = []
n = int(input("Quantas pessoas deseja cadastrar? "))

for i in range(n):
    nome = input("Nome: ")
    while True:
        try: 
            idade = int(input("Idade: "))
            if idade > 0 and idade<150:
                break
            else:
                print("Erro: A idade deve ser maior que zero.")
        except ValueError:
            print("Entrada inválida! Por favor, digite apenas números.")

    while True:
        sexo = input("Sexo (M/F): ").upper().strip()
        if sexo in ['M', 'F']:
            break
        else:
            print (f"Entre com M para Masculino ou F para Feminino.")

    pessoas.append({'nome': nome, 'idade': idade, 'sexo': sexo})

soma_idades = sum(p['idade'] for p in pessoas)
media = soma_idades / n
print(f"Média de idade: {media:.2f} anos")

mulheres_jovens = 0
for p in pessoas:
    if p['sexo'] == 'F' and p['idade'] < 20: 
        mulheres_jovens += 1

print(f"Quantidade de mulheres com menos de 20 anos: {mulheres_jovens}")
