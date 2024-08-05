""" 1. Criação de Lista """

# Criando uma lista vazia
lista_vazia = []

# Criando uma lista com elementos
lista_numeros = [1, 2, 3, 4, 5]

""" 2. Append (Adicionar Elemento no Final) """

# Adicionando um elemento no final da lista
lista_numeros.append(6)
print(lista_numeros)  # Saída: [1, 2, 3, 4, 5, 6]

""" 3. Copy (Copiar a Lista) """

# Copiando uma lista
lista_copia = lista_numeros.copy()
print(lista_copia)  # Saída: [1, 2, 3, 4, 5, 6]

""" 4. Extend (Estender a Lista com Outra Lista) """

# Estendendo a lista com outra lista
lista_numeros.extend([7, 8, 9])
print(lista_numeros)  # Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9]

""" 5. Insert (Inserir Elemento em uma Posição Específica)"""

# Inserindo um elemento na posição 2
lista_numeros.insert(2, 10)
print(lista_numeros)  # Saída: [1, 2, 10, 3, 4, 5, 6, 7, 8, 9]

""" 6. Remove (Remover a Primeira Ocorrência de um Elemento) """

# Removendo a primeira ocorrência do elemento 10
lista_numeros.remove(10)
print(lista_numeros)  # Saída: [1, 2, 3, 4, 5, 6, 7, 8, 9]

""" 7. Pop (Remover e Retornar o Último Elemento ou um Elemento de uma Posição Específica) """

# Removendo e retornando o último elemento
ultimo_elemento = lista_numeros.pop()
print(ultimo_elemento)  # Saída: 9
print(lista_numeros)  # Saída: [1, 2, 3, 4, 5, 6, 7, 8]

# Removendo e retornando o elemento da posição 3
elemento_posicao_3 = lista_numeros.pop(3)
print(elemento_posicao_3)  # Saída: 4
print(lista_numeros)  # Saída: [1, 2, 3, 5, 6, 7, 8]

""" 8. Index (Obter o Índice da Primeira Ocorrência de um Elemento) """

# Obtendo o índice da primeira ocorrência do elemento 5
indice = lista_numeros.index(5)
print(indice)  # Saída: 3

""" 9. Count (Contar a Ocorrência de um Elemento) """

# Contando quantas vezes o elemento 2 aparece na lista
contagem = lista_numeros.count(2)
print(contagem)  # Saída: 1

""" 10. Sort (Ordenar a Lista) """

# Ordenando a lista em ordem crescente
lista_numeros.sort()
print(lista_numeros)  # Saída: [1, 2, 3, 5, 6, 7, 8]

# Ordenando a lista em ordem decrescente
lista_numeros.sort(reverse=True)
print(lista_numeros)  # Saída: [8, 7, 6, 5, 3, 2, 1]

""" 11. Reverse (Inverter a Ordem dos Elementos) """

# Invertendo a ordem dos elementos na lista
lista_numeros.reverse()
print(lista_numeros)  # Saída: [1, 2, 3, 5, 6, 7, 8]

""" 12. Clear (Remover Todos os Elementos) """

# Removendo todos os elementos da lista
lista_numeros.clear()
print(lista_numeros)  # Saída: []

""" 13. List Comprehension (Compreensão de Lista) """

# Criando uma nova lista com o quadrado dos números de 1 a 5
lista_quadrados = [x**2 for x in range(1, 6)]
print(lista_quadrados)  # Saída: [1, 4, 9, 16, 25]
