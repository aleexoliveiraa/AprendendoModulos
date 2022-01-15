'''Adapte o código do desafio #107, criando uma função adicional
chamada moeda() que consiga mostrar os números como um valor monetário formatado.'''


def metade(preco=0):
    resp = preco / 2
    return resp


def dobro(preco=0):
    resp = preco * 2
    return resp


def aumentar(preco=0, taxa=0):
    resp = preco * (taxa/100 +1)
    return resp


def diminuir(preco=0, taxa=0):
    resp = preco * (1 - taxa/100)
    return resp


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
