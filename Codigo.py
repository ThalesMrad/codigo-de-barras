from Imprime import UPC, EAN
from codigodebarras import VerificaPadrao
class ImprimeOCodigo(object):
    def impressao(self,codigoNumeral,padrao):
        padrao.imprime(self,codigoNumeral)

barras = ImprimeOCodigo()
codigoNumeral = input(str("Digite o número do código de barras: "  ))
padrao = VerificaPadrao(codigoNumeral)
if padrao == 0:
    print("Código de barras inválido.")
    quit()
barras.impressao(codigoNumeral,padrao)
