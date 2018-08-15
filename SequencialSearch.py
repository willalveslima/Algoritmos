#----------------------------------------------------
# Sequencial Search                            
# Implementaçao em Python do Algoritmo Sequencial Search 
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow
# Versao 0.1 
# Data 07/08/2018
#-----------------------------------------------------
def Search(A,t):
    for i in range(0,len(A) -1):
        if A[i] == t:
            return True
    return False
#teste