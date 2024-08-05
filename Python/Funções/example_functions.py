""" 1. Definindo Funções """

# Definindo uma função simples que imprime uma mensagem
def saudacao():
    print("Olá, mundo!")

# Chamando a função
saudacao()  # Saída: Olá, mundo!

""" 2. Funções com Parâmetros """

# Função que aceita um parâmetro e imprime uma mensagem personalizada
def saudacao_nome(nome):
    print(f"Olá, {nome}!")

# Chamando a função com um argumento
saudacao_nome("Alice")  # Saída: Olá, Alice!

""" 3. Funções com Retorno de Valor """

# Função que soma dois números e retorna o resultado
def soma(a, b):
    return a + b

# Chamando a função e armazenando o resultado em uma variável
resultado = soma(3, 4)
print(resultado)  # Saída: 7

""" 4. Funções com Valores Padrão para Parâmetros """

# Função com um parâmetro com valor padrão
def saudacao_nome(nome="Mundo"):
    print(f"Olá, {nome}!")

# Chamando a função sem argumento
saudacao_nome()  # Saída: Olá, Mundo!

# Chamando a função com um argumento
saudacao_nome("Alice")  # Saída: Olá, Alice!

""" 5. Funções com Número Variável de Argumentos """

# Função que aceita um número variável de argumentos
def soma_varios(*numeros):
    return sum(numeros)

# Chamando a função com diferentes números de argumentos
print(soma_varios(1, 2, 3))  # Saída: 6
print(soma_varios(4, 5, 6, 7, 8))  # Saída: 30

""" 6. Funções com Argumentos Nomeados """

# Função que aceita argumentos nomeados
def pessoa_info(nome, idade):
    print(f"Nome: {nome}, Idade: {idade}")

# Chamando a função com argumentos nomeados
pessoa_info(nome="Alice", idade=25)  # Saída: Nome: Alice, Idade: 25
pessoa_info(idade=30, nome="Bob")  # Saída: Nome: Bob, Idade: 30

""" 7. Funções com Número Variável de Argumentos Nomeados """

# Função que aceita um número variável de argumentos nomeados
def pessoa_detalhes(**detalhes):
    for chave, valor in detalhes.items():
        print(f"{chave}: {valor}")

# Chamando a função com diferentes números de argumentos nomeados
pessoa_detalhes(nome="Alice", idade=25, cidade="Recife")  
# Saída: 
# nome: Alice
# idade: 25
# cidade: Recife

""" 8. Funções Lambda (Funções Anônimas) """

# Definindo uma função lambda para somar dois números
soma_lambda = lambda a, b: a + b

# Chamando a função lambda
print(soma_lambda(3, 4))  # Saída: 7

# Função lambda para verificar se um número é par
eh_par = lambda x: x % 2 == 0
print(eh_par(4))  # Saída: True
print(eh_par(5))  # Saída: False

""" 9. Funções como Argumentos de Outra Função """ 

# Função que aplica uma função a cada elemento de uma lista
def aplicar_funcao(lista, funcao):
    return [funcao(x) for x in lista]

# Definindo uma função para ser usada como argumento
def quadrado(x):
    return x ** 2

# Chamando a função com outra função como argumento
numeros = [1, 2, 3, 4, 5]
resultados = aplicar_funcao(numeros, quadrado)
print(resultados)  # Saída: [1, 4, 9, 16, 25]

""" 10. Funções Recursivas """

# Função recursiva para calcular o fatorial de um número
def fatorial(n):
    if n == 1:
        return 1
    else:
        return n * fatorial(n - 1)

# Chamando a função recursiva
print(fatorial(5))  # Saída: 120
