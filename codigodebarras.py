class Codigodebarras(object):
    # def __init__(self,codigoNumeral):
    #     self.codigoNumeral = codigoNumeral
    # @property
     def VerificaPadrao(self,codigoNumeral):

        if  not self.codigoNumeral.isnumeric():
            print("Código de barras inválido, caractere que não é um número.")
            quit()

        if len(self.codigoNumeral) == 12:
            w = (3,1,3,1,3,1,3,1,3,1,3,1)
            soma = 0
            for i in range(0,len(self.codigoNumeral)):
                soma += w[i] * int(self.codigoNumeral[i])
            if soma % 10 != 0:
                print("Código de barras inválido.")
                quit()
            else:
                return UPC

        elif len(self.codigoNumeral) == 13:
            w = (1,3,1,3,1,3,1,3,1,3,1,3,1)
            soma = 0
            for i in range(0,len(self.codigoNumeral)):
                soma += w[i] * int(self.codigoNumeral[i])
            if soma % 10 != 0:
                print("Código de barras inválido.")
                quit()
            else:
                return EAN
        else:
            return 0
