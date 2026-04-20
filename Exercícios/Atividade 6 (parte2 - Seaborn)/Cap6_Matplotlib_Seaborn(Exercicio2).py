import seaborn as sns
import matplotlib.pyplot as plt

ds_titanic = sns.load_dataset('titanic')

# Cálculos de integridade dos dados validos (com e sem idade)
total_passageiros = len(ds_titanic)
sem_idade = ds_titanic['age'].isnull().sum()
com_idade = ds_titanic['age'].notnull().sum()
perc_sem_idade = (sem_idade / total_passageiros) * 100

#Configurações visuais
sns.set_style('whitegrid')
plt.figure(figsize=(9, 6)) 

#Histograma com KDE separado por sexo
sns.histplot(
    data=ds_titanic,
    x='age',         
    hue='sex',        
    kde=True,         
    bins=30,          
    alpha=0.6         
)

plt.title('Distribuição de idades — Titanic por sexo', fontsize=14, pad=15)
plt.xlabel('Idade (anos)') 
plt.ylabel('Quantidade de passageiros')

texto_rodape = (
    f"Nota Metodológica:\n"
    f"*O gráfico acima reflete apenas a distribuição dos {com_idade} passageiros com dados válidos.\n"
    f"\n"
    f"Total de passageiros: {total_passageiros}\n "
    f"Com idade cadastrada: {com_idade} \n "
    f"Sem idade (ignorados): {sem_idade} (Aprox. {perc_sem_idade:.1f}%)"
)

#Inserindo o texto no gráfico
plt.figtext(0.5, 0.02, texto_rodape, ha="center", fontsize=10, color="black", 
            bbox={"facecolor":"whitesmoke", "alpha":0.8, "pad":5, "edgecolor":"gray"})
plt.subplots_adjust(bottom=0.28)
plt.show()
