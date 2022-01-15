'''Modifique as funções que form criadas no desafio 107 para que elas
aceitem um parâmetro a mais, informando se o valor retornado por elas vai ser ou não formatado
pela função moeda(), desenvolvida no desafio 108.'''


def metade(preco=0, formato=False):
    resp = preco / 2
    return resp if formato is False else moeda(resp)


def dobro(preco=0, formato=False):
    resp = preco * 2
    return resp if not formato else moeda(resp)


def aumentar(preco=0, taxa=0, formato=False):
    resp = preco * (taxa/100 +1)
    return resp if not formato else moeda(resp)


def diminuir(preco=0, taxa=0, formato=False):
    resp = preco * (1 - taxa/100)
    return resp if not formato else moeda(resp)


def moeda(preco=0, moeda='R$'):
    return f'{moeda}{preco:.2f}'.replace('.', ',')
