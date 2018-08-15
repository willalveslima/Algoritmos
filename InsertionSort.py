#----------------------------------------------------
# Insertion Sort                            
# Implementaçao em Python do Algoritmo Insertion Sort 
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow
# Versao 0.1 
# Data 01/07/2018
#-----------------------------------------------------
def sort(A):
    for i in range(1,len(A)):
        insert(A, i,A[i])
def insert(A, pos, value):
    gardValue = value
    i= pos -1
    while(i >= 0 and A[i] > gardValue):
        A[i +1] = A[i]
        i = i - 1
    A[i +1] = gardValue

def insertion(A,left,right):
    for i in range(left,right+1):
        insert(A, i,A[i])