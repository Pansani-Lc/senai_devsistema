class Veiculo:
    def _init_(self,marca,modelo, chassi, placa, cor, ano,):
        self.marca = marca
        self.modelo = modelo 
        self.chassi= chassi 
        self.placa = placa 
        self.cor = cor 
        self.ano = ano 

    def detalhes(self):
        print ('Essa é a marca'
               
               
                {self.marca},do modelo: {self.modelo}, \
        da cor: {self.cor} e do ano: {self.ano}')

        

class Carro(Veiculo):

    def _init_(self, marca, modelo, chassi, placa, cor, ano):
        return super()._init_(marca, modelo, chassi, placa, cor, ano)