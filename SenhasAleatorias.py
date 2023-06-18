import random
import string

tamanho = int(input("Digite o comprimento da senha: "))

letras_maiusculas = ''
while letras_maiusculas != 's' and letras_maiusculas != 'n':
    letras_maiusculas = input("Incluir letras maiúsculas? (s/n): ")
    if letras_maiusculas != 's' and letras_maiusculas != 'n':
        print("Opção inválida. Responda com 's' para sim ou 'n' para não.")

letras_minusculas = ''
while letras_minusculas != 's' and letras_minusculas != 'n':
    letras_minusculas = input("Incluir letras minúsculas? (s/n): ")
    if letras_minusculas != 's' and letras_minusculas != 'n':
        print("Opção inválida. Responda com 's' para sim ou 'n' para não.")

numeros = ''
while numeros != 's' and numeros != 'n':
    numeros = input("Incluir números? (s/n): ")
    if numeros != 's' and numeros != 'n':
        print("Opção inválida. Responda com 's' para sim ou 'n' para não.")

simbolos = ''
while simbolos != 's' and simbolos != 'n':
    simbolos = input("Incluir símbolos? (s/n): ")
    if simbolos != 's' and simbolos != 'n':
        print("Opção inválida. Responda com 's' para sim ou 'n' para não.")

caracteres = ''

if letras_maiusculas == 's':
    caracteres += string.ascii_uppercase

if letras_minusculas == 's':
    caracteres += string.ascii_lowercase

if numeros == 's':
    caracteres += string.digits

if simbolos == 's':
    caracteres += string.punctuation

if caracteres == '':
    print("Erro: Nenhuma opção selecionada para a geração de senha.")
else:
    senha = ''.join(random.choice(caracteres) for _ in range(tamanho))
    print("Senha gerada:", senha)
