import numpy as np

# 1. Carregamento - dtype=str para aceitar todos os campos
dataset = np.loadtxt('space.csv', delimiter=';', dtype=str, encoding='utf-8')

# 2. Fatiamento para não ver cabeçalho (Linha 0)
dados = dataset[1:, :]

# Questão 1: Porcentagem de missões bem-sucedidas
# Coluna [7] é o 'Status Mission'.
status = dados[:, 7]
sucessos = status[status == 'Success']
porcentagem = (len(sucessos) / len(status)) * 100
print(f"1. Porcentagem de sucesso: {porcentagem:.2f}%")

# Questão 2: Média de gastos (> 0)
# converte a coluna de texto para números reais
custos = np.array(dados[:, 6], dtype=float) 
custos_validos = custos[custos > 0] # Filtra apenas valores disponíveis
print(f"2. Média de gastos: ${np.mean(custos_validos):.2f}")

# Questão 3: Missões realizadas pelos EUA (USA)
# Coluna [2] é a 'Location'.busca em strings vetorizada
locais = dados[:, 2]
usa_filtro = np.char.find(locais, 'USA') != -1
print(f"3. Missões nos EUA: {np.sum(usa_filtro)}")

# Questão 4: Missão mais cara da SpaceX
# Coluna [1] é 'Company Name'   
empresas = dados[:, 1]
# Primeiro, pegamos o valor máximo apenas da SpaceX
max_spacex = np.max(custos[empresas == 'SpaceX']) 

# Empresa == SpaceX E Custo == Max
# O símbolo '&' é obrigatório no NumPy para o 'E' lógico
filtro_vencedoras = (empresas == 'SpaceX') & (custos == max_spacex)
vencedoras = dados[filtro_vencedoras]

print(f"4. Encontrada(s) {len(vencedoras)} missão(ões) mais caras da SpaceX, com custo máximo de ${max_spacex:.2f}:")
for v in vencedoras:
    print(f"   - ID: {v[0]} | Nome: {v[4]}") #v[0] coluna zero (ID) e v[4] coluna nome

# Questão 5: Relatório de Empresas (Nome e Quantidade)
# Usando unique com return_counts 
nomes, quantidades = np.unique(empresas, return_counts=True)
print("\n5. Relatório de Missões:")

for i in range(len(nomes)):
    print(f"Empresa: {nomes[i]:20} | Quantidade: {quantidades[i]}") #reserva 20 caracteres para a | ficar no mesmo lugar
