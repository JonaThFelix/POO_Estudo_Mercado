from Classes import ClienteEspecial as ce
from Classes import Item as it

clientee1 = ce('joao', 30, '1239290183', 'qualquer coisa', True)

print(clientee1.pontos)

i1 = it('bola', 123, 20, 10, True)
i2 = it('cadeira', 324, 400, 5, True)
i3 = it('carro', 400, 40000, 3, True)

clientee1.adicionar(i1)
clientee1.adicionar(i1)
clientee1.adicionar(i3)
clientee1.adicionar(i2)

print(clientee1.comprar())

clientee1.adicionar(i1)
clientee1.adicionar(i1)
clientee1.adicionar(i3)
clientee1.adicionar(i2)

print(clientee1.compraespecial())
print(clientee1.pontos)
