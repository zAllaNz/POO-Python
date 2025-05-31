class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        if(not self.disponivel):
            aux = "Emprestado"
        else:
            aux = "Disponível"
        return f"Livro: {self.titulo} do Autor: {self.autor} está {aux}"

    def isDisponivel(self):
        return self.disponivel
    
    def emprestar(self):
        self.disponivel = False
        print("Empréstimo efetuado com sucesso!")

    def devolver(self):
        self.disponivel = True
        print("Devolução foi efetuado com sucesso!")
    
class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []

    def emprestar_livro(self, livro):
        if(isinstance(livro, Livro)):
            if(livro.isDisponivel()):
                livro.emprestar()
                self.livros_emprestados.append(livro)
                print("Livro foi emprestado!")
            else:
                print("Livro indisponível.")
        else:
            print("Não é um livro!")
    
    def devolver_livro(self, livro):
        if(isinstance(livro, Livro)):
            if(livro in self.livros_emprestados):
                livro.emprestar()
                self.livros_emprestados.remove(livro)
                print("Livro foi devolvido com sucesso!")
            else:
                print("Não encontramos o livro.")
        else:
            print("Não é um livro!")

    def listar_livros(self):
        for livro in self.livros_emprestados:
            print(livro)

livro1 = Livro("1984", "George Orwell")
livro2 = Livro("O Hobbit", "J.R.R. Tolkien")

usuario = Usuario("João")
usuario.emprestar_livro(livro1)
usuario.emprestar_livro(livro2)

usuario.listar_livros()

usuario.devolver_livro(livro1)
usuario.listar_livros()

print(livro1)  # Deve aparecer como disponível novamente