import seaborn as sns
import matplotlib.pyplot as plt

ds_mpg = sns.load_dataset('mpg').dropna(subset=['horsepower'])
#Cria a nova coluna com a conversão
ds_mpg['consumo_L_100km'] = 235.215 / ds_mpg['mpg']

sns.set_style('darkgrid')
#Criando a tela (Figure) com 1 linha e 2 colunas (Axes)
#figsize=(14, 6) deixa a imagem mais larga para caberem os dois
fig, axes = plt.subplots(1, 2, figsize=(14, 6))

# --- GRÁFICO 1 (Esquerda) em MPG ---
sns.regplot(
    data=ds_mpg, 
    x='horsepower', 
    y='mpg',
    scatter_kws={'alpha': 0.4, 's': 20}, 
    line_kws={'color': 'red', 'linewidth': 2},
    ax=axes[0]  # direciona o gráfico para a posição 0 (esquerda)
)
axes[0].set_title('Relação entre Potência e Consumo (Milhas Por Galão - MPG)', fontsize=12)
axes[0].set_xlabel('Potência (Horsepower - CV)\nGráfico 1')
axes[0].set_ylabel('Milhas Por Galão (Menor = Pior)')

# --- GRÁFICO 2 (Direita): Convertido para L/100km ---
sns.regplot(
    data=ds_mpg, 
    x='horsepower', 
    y='consumo_L_100km',
    scatter_kws={'alpha': 0.4, 's': 20}, 
    line_kws={'color': 'green', 'linewidth': 2}, # verde para diferenciar
    ax=axes[1]  # Direciona o gráfico para a posição 1 (direita)
)
axes[1].set_title('Consumo Real (L/100km)', fontsize=12)
axes[1].set_xlabel('Potência (Horsepower - CV)\nGráfico 2')
axes[1].set_ylabel('Litros a cada 100 km (Maior = Gasta mais)')

plt.suptitle('Gráfico 1 - Milhas por Galão e Grafico 2 - Litros por 100km', 
             fontsize=16, fontweight='bold')

# tight_layout() garante que os gráficos não fiquem espremidos um por cima do outro
plt.tight_layout()
plt.show()
