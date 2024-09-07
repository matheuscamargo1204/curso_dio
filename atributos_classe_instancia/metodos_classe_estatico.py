class Pessoa:
    def __init__(self, nome=None, idade=None):
        self.nome = nome 
        self.idade = idade 
        
    @classmethod
    def criar_de_data_nacimento(cls, ano, mes, dia, nome):
        idade = 2022 -ano
        return cls(nome, idade)
    
    @staticmethod
    def e_maior_idade(idade):
        return idade >= 18
    
    
p = Pessoa.criar_de_data_nacimento(2000, 1, 18, "matheus")
print(p.nome, p.idade)

print(Pessoa.e_maior_idade(18))
print(Pessoa.e_maior_idade(8))