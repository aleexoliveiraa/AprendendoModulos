import moeda

preço = float(input('Digite o preço: R$'))
print(f'O dobro de R${preço:.2f} é igual a R${moeda.dobro(preço):.2f}.')
print(f'A metade de R${preço:.2f} é igual a R${moeda.metade(preço):.2f}.')
print(f'Aumentando 10%, temos R${moeda.aumentar(preço, 10):.2f}.')
print(f'Diminuindo 20%, temos R${moeda.diminuir(preço, 20):.2f}.')
