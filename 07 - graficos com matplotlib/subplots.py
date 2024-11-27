import matplotlib.pyplot as plt

# Subplots - Gráficos distintos sendo exibidos na mesma tela

# Criar uma figura e uma grade de subplots (subgráficos)
# fig, axs = plt.subplots(nrows=1, ncols=2)

# # Adicionar dados aos subplots
# # Esquerdo
# axs[0].plot([1, 2, 3, 4, 5], [1, 3, 4, 2, 5], linewidth=2, color='red', label='Esquerda')
# axs[0].set_title("Subplot do lado esquerdo. ")

# # Direito
# axs[1].barh(['A', 'B', 'C', 'D'], [8, 15, 6, 7], color='orange')
# axs[1].set_title("Subplot do lado direito.")

# axs[0].legend()

fig, axs = plt.subplots(2,2, figsize=(10,8)) #polegadas 

# Adicionar dados aos subplots
# Superior Esquerdo
axs[0, 0].plot([1, 2, 3, 4, 5], [1, 3, 4, 2, 5], linewidth=2, color='green', label='Esquerda')
axs[0, 0].set_title("Subplot do lado superior esquerdo. ")

# Superior Direito
axs[0, 1].barh(['A', 'B', 'C', 'D'], [8, 15, 6, 7], color='orange')
axs[0, 1].set_title("Subplot do lado superior direito.")

# Inferior Esquerdo
axs[1, 0].bar(['A', 'B', 'C', 'D'], [8, 15, 6, 7], color='#069AF3')
axs[1, 0].set_title("Subplot do lado inferior esquerdo.")

# Inferior Direito
axs[1, 1].pie([30, 20, 40], labels=['A', 'B', 'C'])
axs[1, 1].set_title("Subplot do lado inferior direito. ")

fig.suptitle("Aula de Subplots com Matplotlib")
fig.tight_layout(pad=2.0)

plt.show()