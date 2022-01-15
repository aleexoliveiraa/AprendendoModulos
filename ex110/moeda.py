'''Adicione o módulo moeda.py criado nos desafios anteriores,
uma função chamada resumo(), que mostre na tela algumas
nformações geradas pelas funções que já temos no módulo criado até aqui.'''


def metade(preco=0, formato=False):
    '''
        => Retorna a metade de um valor formatado em reais
    :param preco: preço a ser calculado
    :param formato: (opcional) formata como dinheiro
    :return: metade do valor informado
    '''
    resp = preco / 2
    return resp if formato is False else moeda(resp)


def dobro(preco=0, formato=False):
    '''
        => Retorna o dobro de um valor formatado em reais
    :param preco: preço a ser calculado
    :param formato: (opcional) formata como dinheiro
    :return: dobro do valor informado
    '''
    resp = preco * 2
    return resp if not formato else moeda(resp)


def aumentar(preco=0, taxa=0, formato=False):
    '''
        => Retorna um aumento em % de um valor formatado em reais
    :param preco: preço a ser calculado
    :param formato: (opcional) formata como dinheiro
    :param taxa: taxa de aumento
    :return: valor atualizado do valor informado
    '''
    resp = preco * (taxa/100 +1)
    return resp if not formato else moeda(resp)


def diminuir(preco=0, taxa=0, formato=False):
    '''
        => Retorna uma diminuição em % de um valor formatado em reais
    :param preco: preço a ser calculado
    :param formato: (opcional) formata como dinheiro
    :param taxa: taxa de diminuição
    :return: valor atualizado do valor informado
    '''
    resp = preco * (1 - taxa/100)
    return resp if not formato else moeda(resp)


def moeda(preco=0, moeda='R$'):
    '''
        => Configura um valor em moeda, via de regra será em real, mas podendo ser alterado
    :param preco: preço a ser formatado
    :param moeda: (opcional) qual moeda deve ser a formatação, via de regra é real
    :return: retorna o valor formatada.
    '''
    return f'{moeda}{preco:.2f}'.replace('.', ',')


def resumo():
