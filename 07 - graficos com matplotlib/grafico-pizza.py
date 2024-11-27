import matplotlib.pyplot as plt

linguagens = ["Python", "C#", "JavaScript", "Ruby"]
quantidades = [300, 150, 270, 40]

cores = ('blue', 'purple', 'yellow', 'red')
distancia = (0.1, 0, 0, 0)

plt.pie(quantidades, labels=linguagens, colors=cores, autopct='%1.1f%%', startangle=90, explode=distancia)

plt.title("Prefências de Linguagens de Programação")
plt.legend(title='Linguagens', loc='best', bbox_to_anchor=(1, 0.8))

plt.show()