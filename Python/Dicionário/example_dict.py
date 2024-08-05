""" 1. Criação de Dicionários """

# Criando um dicionário vazio
dicionario_vazio = {}

# Criando um dicionário com elementos
dicionario_alunos = {
    "Alice": 24,
    "Bob": 22,
    "Carlos": 23
}

""" 2. Acessando Valores """

# Acessando o valor associado à chave "Alice"
idade_alice = dicionario_alunos["Alice"]
print(idade_alice)  # Saída: 24

# Acessando o valor com o método get()
idade_bob = dicionario_alunos.get("Bob")
print(idade_bob)  # Saída: 22

# Usando get() com valor padrão se a chave não existir
idade_diana = dicionario_alunos.get("Diana", "Não encontrado")
print(idade_diana)  # Saída: Não encontrado

""" 3. Adicionando ou Atualizando Elementos """

# Adicionando um novo par chave-valor
dicionario_alunos["Diana"] = 21
print(dicionario_alunos)  # Saída: {'Alice': 24, 'Bob': 22, 'Carlos': 23, 'Diana': 21}

# Atualizando o valor associado à chave "Alice"
dicionario_alunos["Alice"] = 25
print(dicionario_alunos)  # Saída: {'Alice': 25, 'Bob': 22, 'Carlos': 23, 'Diana': 21}

""" 4. Removendo Elementos """

# Removendo um elemento com del
del dicionario_alunos["Bob"]
print(dicionario_alunos)  # Saída: {'Alice': 25, 'Carlos': 23, 'Diana': 21}

# Removendo um elemento com pop()
idade_carlos = dicionario_alunos.pop("Carlos")
print(idade_carlos)  # Saída: 23
print(dicionario_alunos)  # Saída: {'Alice': 25, 'Diana': 21}

# Removendo o último par chave-valor adicionado com popitem()
ultimo_item = dicionario_alunos.popitem()
print(ultimo_item)  # Saída: ('Diana', 21)
print(dicionario_alunos)  # Saída: {'Alice': 25}

""" 5. Verificando a Existência de uma Chave """

# Verificando se a chave "Alice" está no dicionário
existe_alice = "Alice" in dicionario_alunos
print(existe_alice)  # Saída: True

# Verificando se a chave "Carlos" está no dicionário
existe_carlos = "Carlos" in dicionario_alunos
print(existe_carlos)  # Saída: False

""" 6. Percorrendo o Dicionário """

# Percorrendo as chaves do dicionário
for chave in dicionario_alunos:
    print(chave)  # Saída: Alice

# Percorrendo as chaves e valores do dicionário
for chave, valor in dicionario_alunos.items():
    print(f"{chave}: {valor}")  # Saída: Alice: 25

""" 7. Métodos úteis de Dicionários """
""" 7.1 keys() (Obtendo as Chaves) """

# Obtendo todas as chaves do dicionário
chaves = dicionario_alunos.keys()
print(chaves)  # Saída: dict_keys(['Alice'])

""" 7.2 values() (Obtendo os Valores) """

# Obtendo todos os valores do dicionário
valores = dicionario_alunos.values()
print(valores)  # Saída: dict_values([25])

""" 7.3 items() (Obtendo os Pares Chave-Valor) """

# Obtendo todos os pares chave-valor do dicionário
itens = dicionario_alunos.items()
print(itens)  # Saída: dict_items([('Alice', 25)])

""" 7.4 update() (Atualizando o Dicionário com Outro Dicionário) """

# Atualizando o dicionário com outro dicionário
dicionario_novos_alunos = {"Eva": 20, "Frank": 22}
dicionario_alunos.update(dicionario_novos_alunos)
print(dicionario_alunos)  # Saída: {'Alice': 25, 'Eva': 20, 'Frank': 22}
