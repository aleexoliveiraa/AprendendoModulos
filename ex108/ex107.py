import moeda

preço = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(preço)} é igual a {moeda.moeda(moeda.dobro(preço))}')
print(f'A metade de {moeda.moeda(preço)} é igual a {moeda.moeda(moeda.metade(preço))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumentar(preço, 10))}.')
print(f'Diminuindo 20%, temos {moeda.moeda(moeda.diminuir(preço, 20))}.')
