# Praticando com o comando if

# programa que solicita ao usuário inserir um número inteiro e retorna se o número é par ou ímpar.

# Programa que solicita ao usuário no console inserir
"""
def multiplo_de_5(numero):
    if numero % 5 == 0:
        return True
    else:
        return False


def multiplo_de_3(numero):
    if numero % 3 == 0:
        return True
    else:
        return False


numero = int(input("Digite um número inteiro: "))
if multiplo_de_5(numero) and multiplo_de_3 (numero):
    print(f" O número {numero} é múltiplo de 5 e de 3.")
elif multiplo_de_5(numero):
    print(f" O número {numero} é múltiplo de 5. ")
elif multiplo_de_3(numero):
    print(f" O número {numero} é multiplo de 3. ")
else:
    print(f" O número {numero} não é multiplo de 5 e nem de 3.")

"""
"""
#Fibonacci

def fibonacci(numero_de_elementos):
    fibonacci = [0,1]
    if numero_de_elementos == 1:
        return 0
    elif numero_de_elementos == 2:
        return [0,1]
    else:
        fibonacci = [0,1]
        for i in range(2, numero_de_elementos):
            novo_elemento_da_lista = fibonacci[-1] + fibonacci[-2]
            fibonacci.append(novo_elemento_da_lista)
        return fibonacci
    
print(fibonacci(int(input(" Digite a quantidade de números de fibonacci que você deseja ver: "))))

"""
"""
def função_sem_sentido(a, b, c):
    print(a + b + c)

função_sem_sentido("I", "es", "go")

def saldo():
    return 1000

nome = "José"
sobrenome = "Silva"

função_sem_sentido(saldo(1500, 4500), nome, sobrenome)

"""

# Crie um programa que solicite ao usuário inserir um número inteiro positivo e o sistema retorna se ele é múltiplo de 5 e retorne uma lista de todos os números positivos menores que o número inserido que são múltiplos de 5.
#checar se é múltiplo de 5

def multiplo_de_5(numero):
    if numero % 5 == 0:
        print(f" O número {numero} é múltiplo de 5. ")
        return True
    else:
        (f" O número {numero} não é múltiplo de 5. ")
        return False
    
# Solicitar ao usuário inserir um número inteiro positivo

def solicitar_numero():
    numero_inserido = int(input("Digite um número inteiro positivo: "))
    if numero_inserido == "":
        print("Você não digitou um número ")
        return solicitar_numero()
    if numero_inserido.isnumeric() == False:
        print("Você não digitou um número. ")
        return solicitar_numero()
    else:
        return int(numero_inserido)
    
    # Lista de múltiplos de 5 menores ou iguais ao número inserido

    def lista_multiplos_5
    
