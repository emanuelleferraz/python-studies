from matplotlib import pyplot as plt

# Plotar gráfico de uma função, como f(x) = x³ + 1

x = range(1, 11, 1)
plt.plot(x, [(valor**3) for valor in x])

plt.show()