class Item:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

    def __str__(self):
        return f"{self.nome} - R${self.preco:.2f}"

    def get_nome(self):
        return self.nome

    def get_preco(self):
        return self.preco
    
class Pedido:
    def __init__(self, cliente):
        self.cliente = cliente
        self.itens = []
        self.finalizado = False

    def __str__(self):
        status = "aberto" if not self.finalizado else "finalizado"
        return f"Cliente {self.cliente}, Itens: {[item.get_nome() for item in self.itens]}, Total: R${self.calcular_total():.2f}, Status {status}"
    
    def adicionar_item(self, item):
        if(not self.finalizado):
            if(isinstance(item, Item)):
                self.itens.append(item)
                print(f"O item {item.get_nome()} foi adicionado a lista!")
            else:
                print(f"Não foi possível adicionar esse item a lista.")
        else:
            print("Seu pedido já foi finalizado, não foi possível realizar essa operação.")
    
    def remover_item(self, item_remover):
        if(not self.finalizado):
            for item in self.itens:
                if(item.get_nome() == item_remover):
                    self.itens.remove(item)
                    print(f"O item {item.get_nome()} foi removido da lista!")
                    return
            else:
                print("Não foi encontrado nenhum item com esse nome na sua lista.")
        else:
            print("Seu pedido já foi finalizado, não foi possível realizar essa operação.")

    def calcular_total(self):
        total = 0
        if(len(self.itens) != 0):
            for item in self.itens:
                total += item.get_preco()
        return total
    
    def listar_item(self):
        if(len(self.itens) != 0):
            for item in self.itens:
                print(item, end=", ")
        else:
            print("Sua lista está vazia")

    def finalizar_pedido(self):
        if(not self.finalizado):
            self.finalizado = True
            print("Seu pedido foi finalizado com sucesso!")
        else:
            print("Seu pedido já foi finalizado.")

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.pedidos = []

    def fazer_pedido(self):
        novo_pedido = Pedido(self.nome)
        self.pedidos.append(novo_pedido)
        print("Você criou um novo pedido!")
        return novo_pedido
    
    def listar_pedidos(self):
        for pedido in self.pedidos:
            print(pedido)
            print("------------------------------")
    

c1 = Cliente("João")
p1 = c1.fazer_pedido()
p1.adicionar_item(Item("X-Burger", 12.0))
p1.adicionar_item(Item("Suco", 5.0))
print(p1.calcular_total())  # Deve imprimir 17.0
p1.finalizar_pedido()
p2 = c1.fazer_pedido()
p2.adicionar_item(Item("X-Salada", 18.0))
p2.adicionar_item(Item("Suco", 5.0))
p2.adicionar_item(Item("Coca Lata", 5.0))
print(p2.calcular_total())  # Deve imprimir 17.0
p2.finalizar_pedido()
c1.listar_pedidos()
