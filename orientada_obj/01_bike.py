class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
    
    def buzinar(self):
        print("plim plim")
    
    def parar(self):
        print("parando a bicicleta...")
        print("bicicleta parada!")
    
    def correr(self):
        print("vrummmm...")
             
    def __str__(self):
        return f"{self.__class__.__name__}: {','.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"
        
        
b1 = Bicicleta("vermelha", "caloi", 2022, 1500)
b1.buzinar()
b1.correr()
b1.parar()
print(b1.cor, b1.modelo, b1.ano, b1.valor)