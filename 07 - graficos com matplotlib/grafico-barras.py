import matplotlib.pyplot as plt

# Temperaturas:
# almenara = [32, 30, 27, 28, 29, 24]
# joaima = [27, 26, 29, 25, 22, 22]
# santo_antonio = [17, 19, 15, 20, 25, 26]

# Homicídios:
almenara = [5, 2, 0, 0, 2, 1]
joaima = [2, 1, 2, 4, 3, 6]
santo_antonio = [2, 3, 5, 0, 1, 1]

datas = [5, 10, 15, 20, 25, 30]

# criando posições distintas para cada cidade
# posicoes_almenara = list(range(len(datas)))
# posicoes_santo_antonio = [pos + 0.25 for pos in posicoes_almenara]
# posicoes_joaima = [pos + 0.50 for pos in posicoes_almenara]

# plt.barh(datas, almenara, height=0.25, color='r', label='Almenara')
plt.bar(datas, almenara, color='r', label='Almenara')
plt.bar(datas, santo_antonio, color='b', bottom=almenara, label='Santo Antônio do Jacinto')
plt.bar(datas, joaima, bottom=[a + b for a, b in zip(almenara, santo_antonio)], color='g', label='Joaima')

plt.legend()
plt.xlabel("Datas")
plt.ylabel("Homicídios")
plt.title("Homicídios nas Cidades em Dias Determinados")
#plt.xticks(ticks=posicoes_almenara, labels=datas)

plt.show()