# Dicionários - Chave/Valor

element = {
    'Z': 3,
    'nome': 'Lítio',
    'grupo': 'Metais Alcalinos',
    'densidade': 0.534
}

print(f"Elemento: {element['nome']}")
print(f"Densidade: {element['densidade']}")
print(f"O dicionário possui {len(element)} elementos.")

# Atualizar uma entrada
element['grupo'] = 'Alcalinos'
print(element)

# Adicionar uma entrada
element['período'] = 1
print(element)

# Exclusão de itens em dicionários
# del element['período']
# print(element)

# Excluir todos os itens
# element.clear() 
# print(element)

# del element
# print(element)

print(element.items())
for i in element.items():
    print(i)
    
print(element.keys())
for i in element.keys():
    print(i)

print(element.values())
for i in element.values():
    print(i)
    
for i, j in element.items():
    print(f"{i}: {j}")