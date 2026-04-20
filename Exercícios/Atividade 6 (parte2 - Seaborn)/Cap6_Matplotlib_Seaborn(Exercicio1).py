import seaborn as sns
import matplotlib.pyplot as plt

#Carrega o dataset iris da internet (embutido no Seaborn)
ds_iris = sns.load_dataset('iris')

#Filtra somente a espécie setosa
df_setosa = ds_iris[ds_iris['species'] == 'setosa']

#Salva o dataframe no seu computador
#df_setosa.to_csv('iris_setosa_dataset.csv', index=False)

#Remove a coluna categórica ('species') e calcula a matriz de correlação
corr = df_setosa.drop(columns=['species']).corr()

# Plota o heatmap com os valores de correlação
plt.figure(figsize=(7, 5))
sns.heatmap(corr,
    annot=True,       # exibe os valores numéricos dentro dos quadrados
    fmt='.2f',        # formatação com 2 casas decimais
    cmap='coolwarm',  # paleta de cores divergente (azul para negativo, vermelho para positivo)
    vmin=-1,  # Trava a escala de -1 a 1 por questões de padronização matemática, mantendo o zero no centro (neutro), independentemente dos limites dos dados.
    vmax=1   
)

plt.title('Correlação — Iris Setosa')
plt.tight_layout()
plt.show()
