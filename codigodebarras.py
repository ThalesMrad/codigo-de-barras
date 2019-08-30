from Imprime import UPC,EAN
def VerificaPadrao(codigoNumeral):

    if  not codigoNumeral.isnumeric():
        print("Código de barras inválido, caractere que não é um número.")
        quit()

    if len(codigoNumeral) == 12:
        w = (3,1,3,1,3,1,3,1,3,1,3,1)
        soma = 0
        for i in range(0,len(codigoNumeral)):
            soma += w[i] * int(codigoNumeral[i])
        if soma % 10 != 0:
            print("Código de barras inválido.")
            quit()
        else:
            return UPC

    elif len(codigoNumeral) == 13:
        w = (1,3,1,3,1,3,1,3,1,3,1,3,1)
        soma = 0
        for i in range(0,len(codigoNumeral)):
            soma += w[i] * int(codigoNumeral[i])
        if soma % 10 != 0:
            print("Código de barras inválido.")
            quit()
        else:
            return EAN
    else:
        return 0
