class Animal:
    def __init__(self, nome, idade, tipo):
        self.nome = nome
        self.idade = idade
        self.tipo = tipo
        self.adotado = False

    def __str__(self):
        if not self.adotado:
            aux = "Disponível"
        else:
            aux = "Indisponível"

        return f"{self.nome} ({self.tipo}, {self.idade} anos) - {aux}"
    
class Abrigo:
    def __init__(self):
        self.lista = []

    def adicionar_animal(self, animal):
        self.lista.append(animal)

    def listar_animais_disponiveis(self):
        for animal in self.lista:
            if not animal.adotado:
                print(animal)
    
    def adotar_animal(self, nome):
        for animal in self.lista:
            if(animal.nome == nome):
                print(f"{nome} já foi adotado.")
            else:
                animal.adotado = True
                print(f"{nome} foi adotado com sucesso.")
            return
        print(f"Animal chamado {nome} não encontrado.")

abrigo = Abrigo()
abrigo.adicionar_animal(Animal("Thor", 3, "Cachorro"))
abrigo.adicionar_animal(Animal("Mimi", 2, "Gato"))

abrigo.listar_animais_disponiveis()

abrigo.adotar_animal("Thor")
abrigo.listar_animais_disponiveis()
