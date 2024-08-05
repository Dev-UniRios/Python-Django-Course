""" 1. Criação de Conjuntos """

# Criando um conjunto vazio
conjunto_vazio = set()

# Criando um conjunto com elementos
conjunto_numeros = {1, 2, 3, 4, 5}

# Criando um conjunto a partir de uma lista
conjunto_a_partir_de_lista = set([1, 2, 2, 3, 4])
print(conjunto_a_partir_de_lista)  # Saída: {1, 2, 3, 4}

""" 2. Adicionando Elementos """

# Adicionando um elemento ao conjunto
conjunto_numeros.add(6)
print(conjunto_numeros)  # Saída: {1, 2, 3, 4, 5, 6}

""" 3. Removendo Elementos """

# Removendo um elemento do conjunto (se o elemento não existir, ocorre erro)
conjunto_numeros.remove(6)
print(conjunto_numeros)  # Saída: {1, 2, 3, 4, 5}

# Removendo um elemento do conjunto com discard (se o elemento não existir, não ocorre erro)
conjunto_numeros.discard(5)
print(conjunto_numeros)  # Saída: {1, 2, 3, 4}

# Removendo e retornando um elemento arbitrário do conjunto
elemento_removido = conjunto_numeros.pop()
print(elemento_removido)  # Saída: 1 (ou qualquer outro elemento)
print(conjunto_numeros)  # Saída: {2, 3, 4} (sem o elemento removido)

# Limpando todos os elementos do conjunto
conjunto_numeros.clear()
print(conjunto_numeros)  # Saída: set()

""" 4. Operações de Conjunto """
""" 4.1 União """

conjunto_a = {1, 2, 3}
conjunto_b = {3, 4, 5}

# União de dois conjuntos
uniao = conjunto_a.union(conjunto_b)
print(uniao)  # Saída: {1, 2, 3, 4, 5}

# Usando o operador |
uniao_op = conjunto_a | conjunto_b
print(uniao_op)  # Saída: {1, 2, 3, 4, 5}

""" 4.2 Interseção """ 

# Interseção de dois conjuntos
intersecao = conjunto_a.intersection(conjunto_b)
print(intersecao)  # Saída: {3}

# Usando o operador &
intersecao_op = conjunto_a & conjunto_b
print(intersecao_op)  # Saída: {3}

""" 4.3 Diferença """ 

# Diferença entre dois conjuntos
diferenca = conjunto_a.difference(conjunto_b)
print(diferenca)  # Saída: {1, 2}

# Usando o operador -
diferenca_op = conjunto_a - conjunto_b
print(diferenca_op)  # Saída: {1, 2}

""" 4.4 Diferença Simétrica """

# Diferença simétrica entre dois conjuntos
diferenca_simetrica = conjunto_a.symmetric_difference(conjunto_b)
print(diferenca_simetrica)  # Saída: {1, 2, 4, 5}

# Usando o operador ^
diferenca_simetrica_op = conjunto_a ^ conjunto_b
print(diferenca_simetrica_op)  # Saída: {1, 2, 4, 5}

""" 5. Verificação de Subconjunto e Superconjunto """

conjunto_c = {1, 2}
conjunto_d = {1, 2, 3}

# Verificando se conjunto_c é subconjunto de conjunto_d
e_subconjunto = conjunto_c.issubset(conjunto_d)
print(e_subconjunto)  # Saída: True

# Verificando se conjunto_d é superconjunto de conjunto_c
e_superconjunto = conjunto_d.issuperset(conjunto_c)
print(e_superconjunto)  # Saída: True

""" 6. Iterando sobre um Conjunto """

# Iterando sobre os elementos de um conjunto
for elemento in conjunto_b:
    print(elemento)
# Saída: 3 4 5 (a ordem pode variar)

""" 7. Copiando um Conjunto """

# Copiando um conjunto
conjunto_original = {1, 2, 3}
conjunto_copiado = conjunto_original.copy()
print(conjunto_copiado)  # Saída: {1, 2, 3}
