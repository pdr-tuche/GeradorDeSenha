from email import charset
import random
# inicio tratamento do ASCII
especiais =[]
for elem in range(33,48): #primeiro especiais
    especiais.append(elem)
for elem in range(58,65):
    especiais.append(elem)
for elem in range(91,97):
    especiais.append(elem)
for elem in range(123,127):
    especiais.append(elem)

especiais.remove(39)
especiais.remove(40)
especiais.remove(41)
especiais.remove(44)
especiais.remove(46)
especiais.remove(58)
especiais.remove(59)
especiais.remove(91)
especiais.remove(92)
especiais.remove(93)
especiais.remove(96)
especiais.remove(124)
especiais.remove(126)
especiais.remove(125)
especiais.remove(123)

numeros = []
minusculos = []
maiusculos = []
for elem in range(48,58): #numeros
    numeros.append(elem)
for elem in range(65,91): #minusculos
    maiusculos.append(elem)
for elem in range(97,123): #maiusculos
    minusculos.append(elem)
# final do tratamendo ASCII

todos = especiais + numeros + minusculos + maiusculos
todos.sort()

#pra garantir pelo menos um deles:
aleatorioNumero = random.choice(numeros)
aleatorioMaiusculo = random.choice(maiusculos)
aleatorioEspecial = random.choice(especiais)

palavra= random.choices(todos, weights=None, k=5) # 5 algarismos aleatorios
#incluindo ao final da senha pelo menos 1 de cada obrigatorio:
palavra.append(aleatorioEspecial)
palavra.append(aleatorioMaiusculo)
palavra.append(aleatorioNumero)

#definição da senha em string
senha=""
for algarismos in palavra:
    senha += chr(algarismos)
print(senha)