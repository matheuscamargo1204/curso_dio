class Pessoa:
    def __init__(self, nome, ano_nascimento):
        self._nome = nome
        self._ano_nascimento = ano_nascimento
        
    @property
    def idade(self):
        _ano_atual = 2024
        return _ano_atual - self._ano_nascimento

pessoa = Pessoa("matheus", 2000)
print(f"nome: {pessoa.nome} \t Idade: {pessoa.idade}")