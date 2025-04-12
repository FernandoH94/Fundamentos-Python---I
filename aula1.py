# Exemplo 1 - Variável e Visualizações das informações
# Declaração de variável
nome = "Fernando"
nome_do_meio = "Henrique"
sobrenome = "de Sousa"
idade = 31
altura = 1.78

#Mostrando as informações das variáveis no Console/Terminal
print(f"Meu nome é {nome} {nome_do_meio} {sobrenome}, tenho {idade} anos e {altura} de altura.")

# Exemplo 2 - Entrada de dados do usuário
nome = input("Digite seu nome: ")
idade = input("Digite: ")

print("Olá,", nome + "! Você tem", idade, "anos.")
print(f"Olá {nome}! Você tem {idade} anos.") 

# Exemplo 3: Entrada de número e cálculo
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))

soma = num1 + num2

print(soma)

# Obtém a informação do tipo de variável armazenada string, inteiro etc..
# trype(variável) 

# Exemplo 4:  Usando varáveis para fazer uma média
nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

print("A média é: ", media)
