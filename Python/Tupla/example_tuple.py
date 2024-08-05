""" 1. Criação de Tuplas """

# Criando uma tupla vazia
tupla_vazia = ()

# Criando uma tupla com elementos
tupla_numeros = (1, 2, 3, 4, 5)

""" 2. Acessando Elementos da Tupla """

# Acessando o primeiro elemento
primeiro_elemento = tupla_numeros[0]
print(primeiro_elemento)  # Saída: 1

# Acessando o último elemento
ultimo_elemento = tupla_numeros[-1]
print(ultimo_elemento)  # Saída: 5

""" 3. Fatiamento (Slicing) da Tupla """

# Fatiando a tupla do segundo ao quarto elemento
sub_tupla = tupla_numeros[1:4]
print(sub_tupla)  # Saída: (2, 3, 4)

""" 4. Concatenação de Tuplas  """

# Concatenando duas tuplas
tupla_concatenada = tupla_numeros + (6, 7, 8)
print(tupla_concatenada)  # Saída: (1, 2, 3, 4, 5, 6, 7, 8)

""" 5. Repetindo Tupla """

# Repetindo uma tupla
tupla_repetida = tupla_numeros * 2
print(tupla_repetida)  # Saída: (1, 2, 3, 4, 5, 1, 2, 3, 4, 5)

""" 6. Verificando a Existência de um Elemento """

# Verificando se o número 3 está na tupla
existe = 3 in tupla_numeros
print(existe)  # Saída: True

""" 7. Desempacotamento de Tuplas """

# Desempacotando elementos da tupla
a, b, c, d, e = tupla_numeros
print(a, b, c, d, e)  # Saída: 1 2 3 4 5

# Desempacotando parte da tupla
a, *resto = tupla_numeros
print(a)      # Saída: 1
print(resto)  # Saída: [2, 3, 4, 5]

"""
8. Funções Built-in para Tuplas
8.1 Len (Tamanho da Tupla)
"""

# Obtendo o tamanho da tupla
tamanho = len(tupla_numeros)
print(tamanho)  # Saída: 5

""" 8.2 Max (Maior Elemento) """

# Obtendo o maior elemento da tupla
maior_elemento = max(tupla_numeros)
print(maior_elemento)  # Saída: 5

""" 8.3 Min (Menor Elemento) """

# Obtendo o menor elemento da tupla
menor_elemento = min(tupla_numeros)
print(menor_elemento)  # Saída: 1

""" 8.4 Sum (Soma dos Elementos) """

# Somando todos os elementos da tupla
soma_elementos = sum(tupla_numeros)
print(soma_elementos)  # Saída: 15

"""" 8.5 Count (Contar a Ocorrência de um Elemento) """

# Contando quantas vezes o elemento 2 aparece na tupla
contagem = tupla_numeros.count(2)
print(contagem)  # Saída: 1

""" 8.6 Index (Obter o Índice de um Elemento) """

# Obtendo o índice da primeira ocorrência do elemento 4
indice = tupla_numeros.index(4)
print(indice)  # Saída: 3
