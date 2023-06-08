from random import choice
import string

valores = string.ascii_letters
valores += string.digits
valores += string.punctuation
valores += 'Ç'
senha = ''
tamanho = int(input('qual vai ser o tamanho da sua senha? '))

for i in range(0, tamanho):
    senha += choice(valores)


print(f'Sua senha é: {senha}')
