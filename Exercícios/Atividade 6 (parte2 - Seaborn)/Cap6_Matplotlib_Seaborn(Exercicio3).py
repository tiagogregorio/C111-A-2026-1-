import seaborn as sns
import matplotlib.pyplot as plt

titanic = sns.load_dataset('titanic')
titanic_clean = titanic.dropna(subset=['age'])

# Boxplot: classe no eixo x, idade no eixo y, separado por sexo
sns.boxplot(data=titanic_clean, x='class', y='age', hue='sex', 
            palette='Set2')
plt.title('Distribuição das idades por classe e sexo - Titanic')
plt.xlabel('Classe do passageiro')
plt.ylabel('Idade (anos)')
plt.legend(title='Sexo')
plt.show()
