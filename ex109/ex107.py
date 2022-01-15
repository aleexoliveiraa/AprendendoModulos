import moeda

preço = float(input('Digite o preço: R$'))
print(f'O dobro de {moeda.moeda(preço)} é igual a {moeda.dobro(preço, True)}')
print(f'A metade de {moeda.moeda(preço)} é igual a {moeda.metade(preço, True)}')
print(f'Aumentando 10%, temos {moeda.aumentar(preço, 10, True)}.')
print(f'Diminuindo 20%, temos {moeda.diminuir(preço, 20, True)}.')
