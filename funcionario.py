class Funcionario:
    def __init__(self, nome, salario):
        self.nome = nome
        self.salario_base = salario
        self.ativo = True
    
    def __str__(self):
        return f"{self.nome} - R${self.calcular_salario():.2f}"
    
    def get_nome(self):
        return self.nome
    
    def get_ativo(self):
        return self.ativo
    
    def calcular_salario(self):
        return self.salario_base
    
    def demitir(self):
        if(self.ativo):
            self.ativo = False
            print(f"Funcionário {self.nome} foi demitido.")
    
class Gerente(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 1.2
    
class Desenvolvedor(Funcionario):
    def calcular_salario(self):
        return self.salario_base * 1.1
    
class Estagiario(Funcionario):
    def calcular_salario(self):
        return self.salario_base + 300
    
class Empresa:
    def __init__(self):
        self.funcionarios = []

    def admitir(self, funcionario):
        if(isinstance(funcionario, Funcionario)):
            self.funcionarios.append(funcionario)
            print("Funcionario admitido com sucesso!")
        else:
            print("Não foi possível admitir essa pessoa")

    def demitir(self, nome):
        for funcionario in self.funcionarios:
            if(funcionario.get_nome() == nome and funcionario.get_ativo()):
                funcionario.demitir()
                return
        else:
            print("Essa pessoa não está na lista de funcionários.")

    def folha_pagamento(self):
        for funcionario in self.funcionarios:
            if(funcionario.get_ativo()):
                print(funcionario)

    def listar_funcionarios(self, ativos=True):
        for funcionario in self.funcionarios:
            if(funcionario.get_ativo()):
                print(funcionario.get_nome())
            elif(ativos):
                print(funcionario.get_nome())

empresa = Empresa()

empresa.admitir(Gerente("Ana", 5000))
empresa.admitir(Desenvolvedor("Carlos", 4000))
empresa.admitir(Estagiario("João", 1500))

empresa.listar_funcionarios()
empresa.folha_pagamento()

empresa.demitir("Carlos")
empresa.listar_funcionarios(False)
