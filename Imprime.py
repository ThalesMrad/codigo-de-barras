
class UPC(object):
    def imprime(self,codigoNumeral):
            # w = (3,1,3,1,3,1,3,1,3,1,3,1)
            # soma = 0
            # for i in range(0,len(codigoNumeral)):
            #     soma += w[i] * int(codigoNumeral[i])
            # if soma % 10 != 0:
            #     print("Código de barras inválido.")
            #     quit()

            matrizUPC = [[],[],[],[],[],[],[],[],[],[]]
            matrizUPC[0] = [0,0,0,1,1,0,1]
            matrizUPC[1] = [0,0,1,1,0,0,1]
            matrizUPC[2] = [0,0,1,0,0,1,1]
            matrizUPC[3] = [0,1,1,1,1,0,1]
            matrizUPC[4] = [0,1,0,0,0,1,1]
            matrizUPC[5] = [0,1,1,0,0,0,1]
            matrizUPC[6] = [0,1,0,1,1,1,1]
            matrizUPC[7] = [0,1,1,1,0,1,1]
            matrizUPC[8] = [0,1,1,0,1,1,1]
            matrizUPC[9] = [0,0,0,1,0,1,1]
            print("_",end = '')

            for i in range(0,5):
                for j in range(0,6):
                    if matrizUPC[int(codigoNumeral[i])][j] == 0:
                        print(" ",end = '')
                    else:
                        print("|",end = '')

            print("_",end = '')

            for i in range(6,12):
                for j in range(0,6):
                    if matrizUPC[int(codigoNumeral[i])][j] == 0:
                        print("|",end = '')
                    else:
                        print(" ",end = '')

            print("_")
class EAN(object):
    def imprime(self,codigoNumeral):
            # w = (1,3,1,3,1,3,1,3,1,3,1,3,1)
            # soma = 0
            # for i in range(0,len(codigoNumeral)):
            #     soma += w[i] * int(codigoNumeral[i])
            # if soma % 10 != 0:
            #     print("Código de barras inválido.")
            #     quit()

            matrizParidade = [[],[],[],[],[],[],[],[],[],[]]
            matrizParidade[0] = [1,1,1,1,1,1]
            matrizParidade[1] = [1,1,0,1,0,1]
            matrizParidade[2] = [1,1,0,0,1,0]
            matrizParidade[3] = [1,1,0,0,0,1]
            matrizParidade[4] = [1,0,1,1,0,0]
            matrizParidade[5] = [1,0,0,1,1,0]
            matrizParidade[6] = [1,0,0,0,1,1]
            matrizParidade[7] = [1,0,1,0,1,0]
            matrizParidade[8] = [1,0,1,0,0,1]
            matrizParidade[9] = [1,0,0,1,0,1]
            matrizPar = [[],[],[],[],[],[],[],[],[],[]]
            matrizPar[0] = [0,1,0,0,1,1,1]
            matrizPar[1] = [0,1,1,0,0,1,1]
            matrizPar[2] = [0,0,1,1,0,1,1]
            matrizPar[3] = [0,1,0,0,0,0,1]
            matrizPar[4] = [0,0,1,1,1,0,1]
            matrizPar[5] = [0,1,1,1,0,0,1]
            matrizPar[6] = [0,0,0,0,1,0,1]
            matrizPar[7] = [0,0,1,0,0,0,1]
            matrizPar[8] = [0,0,0,1,0,0,1]
            matrizPar[9] = [0,0,1,0,1,1,1]
            matrizImpar = [[],[],[],[],[],[],[],[],[],[]]
            matrizImpar[0] = [0,0,0,1,1,0,1]
            matrizImpar[1] = [0,0,1,1,0,0,1]
            matrizImpar[2] = [0,0,1,0,0,1,1]
            matrizImpar[3] = [0,1,1,1,1,0,1]
            matrizImpar[4] = [0,1,0,0,0,1,1]
            matrizImpar[5] = [0,1,1,0,0,0,1]
            matrizImpar[6] = [0,1,0,1,1,1,1]
            matrizImpar[7] = [0,1,1,1,0,1,1]
            matrizImpar[8] = [0,1,1,0,1,1,1]
            matrizImpar[9] = [0,0,0,1,0,1,1]

            print("_",end = '')

            for i in range(1,7):
                if matrizParidade[int(codigoNumeral[0])][i-1] == 1:
                    for j in range(0,7):
                        if matrizImpar[int(codigoNumeral[i])][j] == 0:
                            print(" ",end = '')
                        else:
                            print("|",end = '')
                    #print('a',end = '')
                else:
                    for j in range(0,7):
                        if matrizPar[int(codigoNumeral[i])][j] == 0:
                            print(" ",end = '')
                        else:
                            print("|",end = '')

            print("_",end = '')

            for i in range(7,13):
                for j in range(0,7):
                    if matrizImpar[int(codigoNumeral[i])][j] == 0:
                        #print(int(codigoNumeral[i]))
                        print(" ",end = '')
                    else:
                        print("|",end = '')

            print("_")
