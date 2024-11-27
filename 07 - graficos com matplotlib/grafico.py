from matplotlib import pyplot as plt

#plt.style.use('dark_background')

eixo_x_dias = [1, 5, 10, 15, 20, 25, 30]
eixo_y_temp_max = [28, 29, 25, 32, 34, 36, 31]
eixo_y_temp_min = [21, 22, 17, 23, 23, 24, 20]

# título do gráfico
plt.title("Temperaturas máximas e mínimas")
plt.xlabel("Datas")
plt.ylabel("Temperatura")

# criar gráfico -> plot(x,y) e legendas
# plt.plot(eixo_x_dias, eixo_y_temp_max, label='Temp Máx') # linhas feitas com '------' e pontos marcados com 'o'
# plt.plot(eixo_x_dias, eixo_y_temp_min, label='Temp Min' )

    # caso queira criar um gráfico de barras:
plt.bar(eixo_x_dias, eixo_y_temp_max, label='Temp Máx')
plt.bar(eixo_x_dias, eixo_y_temp_min, label='Temp Min' )

# legendas
plt.legend(loc='upper left')

# grid no fundo
#plt.grid(True)

# mudando valores dos eixos
#plt.axis([1,31, 5,45])
plt.xlim([1,31]) # muda apenas o do x
plt.ylim([-5, 50])

#salvar gráfico pelo código
#plt.savefig('grafico2.png')

# mostrar o gráfico
plt.show()
#print(plt.style.available)
#print(plt.axis())