#----------------------------------------------------
# Binary Search                            
# Implementaçao em Python do Algoritmo Binary Search 
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow
# Versao 0.1 
# Data 07/08/2018
#-----------------------------------------------------
def Search(A,t):
    low = 0
    high = len(A) -1
    while low <= high:
        ix = (low + high)//2
        if t == A[ix]:
            return True
        elif t < A[ix]:
            high = ix -1
        else:
            low = ix +1
    return False
    