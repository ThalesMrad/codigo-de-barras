from Imprime import UPC, EAN
from codigodebarras import Codigodebarras
class ImprimeOCodigo(object):
    def impressao(self,codigoNumeral,padrao):
        padrao.imprime(self,codigoNumeral)

barras = ImprimeOCodigo()
codigoNumeral = input(str("Digite o número do código de barras: "  ))
padrao = VerificaPadrao(codigoNumeral)
barras.impressao(codigoNumeral,padrao)
