
""" 1. Laço for """

# Iterando sobre uma lista
numeros = [1, 2, 3, 4, 5]
for numero in numeros:
    print(numero)
# Saída: 1 2 3 4 5

# Iterando sobre uma string
texto = "Python"
for letra in texto:
    print(letra)
# Saída: P y t h o n

# Usando range() para iterar sobre uma sequência de números
for i in range(5):
    print(i)
# Saída: 0 1 2 3 4

# Usando range() com início, fim e passo
for i in range(1, 10, 2):
    print(i)
# Saída: 1 3 5 7 9

""" 2. Laço while """

# Usando while para repetir uma ação até que uma condição seja satisfeita
contador = 0
while contador < 5:
    print(contador)
    contador += 1
# Saída: 0 1 2 3 4

# Exemplo com uma condição de saída
numero = 10
while numero > 0:
    print(numero)
    numero -= 2
# Saída: 10 8 6 4 2

""" 3. break e continue """

# Usando break para sair de um laço antecipadamente
for i in range(10):
    if i == 5:
        break
    print(i)
# Saída: 0 1 2 3 4

# Usando continue para pular para a próxima iteração
for i in range(10):
    if i % 2 == 0:
        continue
    print(i)
# Saída: 1 3 5 7 9

""" 4. Estrutura if """

# Estrutura if simples
numero = 10
if numero > 5:
    print("O número é maior que 5.")
# Saída: O número é maior que 5.

""" 5. Estrutura if-else """

# Estrutura if-else
idade = 18
if idade >= 18:
    print("Você é maior de idade.")
else:
    print("Você é menor de idade.")
# Saída: Você é maior de idade.

""" 6. Estrutura if-elif-else """

# Estrutura if-elif-else
nota = 85
if nota >= 90:
    print("A nota é A.")
elif nota >= 80:
    print("A nota é B.")
elif nota >= 70:
    print("A nota é C.")
else:
    print("A nota é D ou F.")
# Saída: A nota é B.

""" 7. Operadores lógicos e de comparação """

# Usando operadores lógicos e de comparação
numero = 15
if numero > 10 and numero < 20:
    print("O número está entre 10 e 20.")
# Saída: O número está entre 10 e 20.

if numero < 10 or numero > 20:
    print("O número está fora do intervalo de 10 a 20.")
else:
    print("O número está dentro do intervalo de 10 a 20.")
# Saída: O número está dentro do intervalo de 10 a 20.

""" 8. Condicionais em expressões """

# Usando condicionais em expressões
idade = 20
mensagem = "Maior de idade" if idade >= 18 else "Menor de idade"
print(mensagem)
# Saída: Maior de idade
