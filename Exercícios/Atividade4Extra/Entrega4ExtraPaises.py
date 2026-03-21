import numpy as np

dataset = np.loadtxt('paises.csv', delimiter=';', dtype=str, encoding='utf-8')
dados = dataset[1:, :]

# --- QUESTÃO 1: Slicing para mostrar País, Região, População e Área ---
print("\n--- QUESTÃO 1: Slicing no dataset ---")
slicing_paises = dados[:, 0:4]

#Formatarção, mais legivel
print(f"{'Country':<25} | {'Region':<25} | {'Population':<12} | {'Area (Sq. Mi.)'}")
print("-" * 85)

# O ciclo percorre todos os itens extraídos no slicing
for p in slicing_paises:
    # f-strings para alinhar as colunas e .strip() para limpar espaços
    print(f"{p[0].strip():<25} | {p[1].strip():<25} | {p[2].strip():<12} | {p[3].strip()}")

 # QUESTÃO 2 - Contar e mostrar as diferentes Regiões do planeta
print("\n--- QUESTÃO 2: Conte e mostre as diferentes Regiões do planeta ---")
regioes_brutas = dados[:, 1] # Extraímos apenas a coluna de regiões (índice 1) de todos os dados
 
# np.char.strip() aplicado ao array inteiro remove espaços de todos os elementos
# np.unique() retorna os valores únicos (sem repetição), já ordenados
regioes_unicas = np.unique(np.char.strip(regioes_brutas))
 
# Contar e exibi cada região única
print(f"Total de regiões diferentes: {len(regioes_unicas)}")
for i, regiao in enumerate(regioes_unicas, start=1):
    print(f"  {i:>2} - {regiao}")

# QUESTÃO 3: Taxa média de alfabetização (Literacy (%))
print("\n--- QUESTÃO 3: Tax Literacy(%) ---")

alfabetizacao = np.array(dados[:, 9], dtype=float) # A alfabetização na coluna [9], converter para float
media_global = np.mean(alfabetizacao)
print('\n*** Considerando que a taxa de alfabetização de alguns países é zero ***')
print(f"Taxa média de alfabetização do planeta: {media_global:.2f}%")

#Assumindo que os paises que tem alfabetização em zero, traz o significado que a informação não
#esta disponivel e com isso teremos uma taxa de alfabetização de 209 paises com dados registrados ao inves
#dos 227 paises por isso o filtro de alfabetização > zero abaixo.
filtro = alfabetizacao > 0
media_global = np.mean(alfabetizacao[filtro])
print('\n*** Assumindo que a a taxa 0 significa informação "não disponível" ***')
print(f"Taxa média de alfabetização do planeta: {media_global:.2f}%")

# QUESTÃO 4: Quantidade de países da América do Norte (NORTHERN AMERICA)
print("\n--- QUESTÃO 4: Quantos países são da NORTHERN AMERICA ---")
# máscara booleana na coluna de regiões [1]
# np.char.strip para garantir que espaços em branco não atrapalhem a comparação
regioes_clean = np.char.strip(dados[:, 1])
mask_na = (regioes_clean == 'NORTHERN AMERICA')
total_na = np.sum(mask_na) # True vale 1 e False vale 0
print(f"Países na América do Norte: {total_na}")

# QUESTÃO 5: País da América do Sul e Caribe com maior GDP ($ per capita)
print("\n--- QUESTÃO 5: País com maior GDP na América do Sul e Caribe ---")
#Transformar toda a coluna de GDP ($ per capita) em float
gdp_all = np.array(dados[:, 8], dtype=float)

#Descobrir o valor máximo APENAS dentro da região desejada,
# Filtrar os GDPs onde a região é LATAM e pegamos o máximo deles
max_gdp_latam = np.max(gdp_all[regioes_clean == 'LATIN AMER. & CARIB'])

#Lógica & para condicao que queremos a linha onde a Região é LATAM E o GDP é igual ao valor máximo que achamos
mask_final = (regioes_clean == 'LATIN AMER. & CARIB') & (gdp_all == max_gdp_latam)
resultado = dados[mask_final]#Extraí o resultado direto da matriz principal 'dados'

# Como o resultado é uma matriz, acessamos o primeiro (e único) item [0]
print(f"País da América do Sul e Caribe com maior GDP: {resultado[0, 0].strip()} | GDP: ${resultado[0, 8]}\n")

