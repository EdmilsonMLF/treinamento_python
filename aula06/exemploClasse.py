class Pessoa:
    nome = ''
    telefone = ''

    def imprimir(self):
        print("Nome: {0}, Telefone: {1}".format(self.nome, self.telefone))

p1 = Pessoa()
p1.nome = 'Maria'
p1.telefone = '3281-0369'

p2 = Pessoa()
p2.nome = 'José'
p2.telefone = '3232-6565'

Pessoa.nome = 'Antônio'

print("Nome: {0}, Telefone: {1}".format(p1.nome, p1.telefone))
print("Nome: {0}, Telefone: {1}".format(p2.nome, p2.telefone))

p1.imprimir()
p2.imprimir()

print(Pessoa.nome)