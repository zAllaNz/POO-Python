class Livro:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor
        self.disponivel = True

    def __str__(self):
        status = "Disponível" if self.disponivel else "Indisponível"
        return f"Livro: {self.titulo}, Autor: {self.autor} está {status}."
    
    def get_titulo(self):
        return self.titulo
    
    def get_disponibilidade(self):
        return self.disponivel
    
    def emprestar(self):
        if(self.disponivel):
            self.disponivel = False
            print("O Livro foi emprestado com sucesso")
            return True
        print("Este livro está indisponível")
        return False

    def devolver(self):
        if(not self.disponivel):
            self.disponivel = True
            print("O Livro foi devolvido com sucesso")
            return True
        print("Este livro já foi devolvido.")
        return False

class Usuario:
    def __init__(self, nome):
        self.nome = nome
        self.livros_emprestados = []
    
    def get_nome(self):
        return self.nome
    
    def emprestar_livro(self, livro):
        if(livro.emprestar()):
            self.livros_emprestados.append(livro)

    def devolver_livro(self, titulo):
        for livro in self.livros_emprestados:
            if(livro.get_titulo() == titulo):
                if(livro.devolver()):
                    self.livros_emprestados.remove(livro)

    def listar_livros(self):
        if(len(self.livros_emprestados) != 0):
            for livro in self.livros_emprestados:
                print(livro)
        else:
            print("Sua lista está vazia.")

class Biblioteca:
    def __init__(self):
        self.livros_disponiveis = []
        self.usuarios = []
    
    def adicionar_livro(self, livro):
        if(isinstance(livro, Livro)):
            self.livros_disponiveis.append(livro)
            print("Este livro foi adicionado com sucesso!")
        else:
            print("Isto não é um livro")

    def registrar_usuario(self, usuario):
        if(isinstance(usuario, Usuario)):
            self.usuarios.append(usuario)
            print("Usuário registrado com sucesso!")
        else:
            print("Não foi possível registrar o usuário")

    def emprestar_livro_para_usuario(self, titulo, nome):
        for livro in self.livros_disponiveis:
            if(livro.get_titulo() == titulo):
                for usuario in self.usuarios:
                    if(usuario.get_nome() == nome):
                        usuario.emprestar_livro(livro)

    def devolver_livro_para_usuario(self, titulo, nome):
        for livro in self.livros_disponiveis:
            if(livro.get_titulo() == titulo):
                for usuario in self.usuarios:
                    if(usuario.get_nome() == nome):
                        usuario.devolver_livro(titulo)

    def listar_livros_disponiveis(self):
        for livro in self.livros_disponiveis:
            if(livro.get_disponibilidade()):
                print(livro)


livro1 = Livro("1984", "George Orwell")
livro2 = Livro("Dom Casmurro", "Machado de Assis")

usuario1 = Usuario("Alice")
usuario2 = Usuario("Bruno")

biblioteca = Biblioteca()
biblioteca.adicionar_livro(livro1)
biblioteca.adicionar_livro(livro2)
biblioteca.registrar_usuario(usuario1)
biblioteca.registrar_usuario(usuario2)

biblioteca.emprestar_livro_para_usuario("1984", "Alice")
usuario1.listar_livros()

biblioteca.listar_livros_disponiveis()

biblioteca.devolver_livro_para_usuario("1984", "Alice")
biblioteca.listar_livros_disponiveis()
