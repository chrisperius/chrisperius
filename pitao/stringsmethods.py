# String Methods
# Exemplo de método replace()
a = input('Forneça uma palavra: ')

def troca_a(palavra):
    return palavra.replace('a', '@').replace('á', '@')

print(troca_a(a))

# Método len() para contar o tamanho da string

def tamanho_do_texto(texto):
    return len(texto)

def contador():
    text = input('frase: ')
    # f 'string...{variável} ' melhor forma de concatenar
    return 'O número de letras da frase é: ' + str(len(text))

print(contador())



# Usar o método count() para contar quantas vezes uma letra aparece na frase.

def contador_de_a():
    texto = input(" Digite um texto: ")
    return f"A letra 'a' aparace {texto.count('a')} vezes na frase. "

print(contador_de_as())