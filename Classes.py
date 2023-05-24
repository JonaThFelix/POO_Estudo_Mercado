class Cliente:
  def __init__(self, nome, idade, CPF, endereco, bomcliente):
    self.nome = nome
    self.idade = idade
    self.CPF = CPF
    self.endereco = endereco
    self.bomcliente = bomcliente
    self.carrinho = []

  def adicionar(self, item):
    if item.disponibilidade == False or item.quantidade == 0:
      print('Não é possivel adicionar o item')
    else:
      self.carrinho.append(item)
      
  def cancelar(self, item, codigo):
    i = 0
    while i < len(self.carrinho):
      if self.carrinho.codigo == codigo:
        self.carrinho.pop(i)
        break
      i = i + 1

  def comprar(self):
    soma = 0
    i = 0

    while i < len(self.carrinho):
      soma = soma + self.carrinho[i].valor
      self.carrinho[i].quantidade = self.carrinho[i].quantidade - 1
      i = i + 1
    self.carrinho.clear()
    return soma, soma / i
      

class Item:
  def __init__(self, nome, codigo, valor, quantidade, disponibilidade):
    self.nome = nome
    self.codigo = codigo
    self.valor = valor
    self.quantidade = quantidade
    self.disponibilidade = disponibilidade


class ClienteEspecial(Cliente):
  def __init__(self, nome, idade, CPF, endereco, bomcliente):
    Cliente.__init__(self, nome, idade, CPF, endereco, bomcliente)
    self.pontos = 0
    self.saldo = 0

  def compraespecial(self):
    soma = 0
    i = 0

    while i < len(self.carrinho):
      soma = soma + self.carrinho[i].valor
      self.carrinho[i].quantidade = self.carrinho[i].quantidade - 1
      i = i + 1

    self.pontos = self.pontos + soma // 100 
    soma = soma * 0.95
    self.saldo = self.saldo + soma
    return soma, soma / i

  def comprapontos(self, item, pontos):
    if self.pontos < pontos:
      print('Saldo insuficiente')
      return
    custo = item.valor
    custo = custo - pontos
    
    novoitem = Item(item.nome, item.codigo, custo, item.quantidade, item.disponibilidade)
    self.adicionar(item)
    self.comprar()

class Funcionario(ClienteEspecial):
  def __init__(self, nome, idade, CPF, endereco, bomcliente, setor, id, salario):
    ClienteEspecial.__init__(self, nome, idade, CPF, endereco, bomcliente)
    self.setor = setor
    self.id = id
    self.salario = salario

  def renovarestoque(self, item, quantidade):
    item.quantidade = item.quantidade + quantidade

  def gerenciaritem(self, item):
    item.disponibilidade = not item.disponibilidade
