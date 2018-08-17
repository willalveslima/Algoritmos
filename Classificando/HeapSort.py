#----------------------------------------------------
# Heap Sort                            
# Implementaçao em Python do Algoritmo Heap Sort 
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow
# Versao 0.1 
# Data 27/07/2018
#-----------------------------------------------------
from util import swap
from util import my_cmp

def sort(A):
    heapSort(A,len(A))

def heapify(ar, idx, max):
    left = 2*idx + 1
    right = 2*idx + 2
    largest = 0
    if left < max and my_cmp(ar[left],ar[idx]) > 0:
        largest = left
    else:
        largest = idx
    if(right < max and my_cmp(ar[right],ar[largest]) > 0):
        largest = right
    if largest != idx:
        ar[idx],ar[largest] = swap(ar[idx],ar[largest])
        heapify(ar,largest,max)

def buildHeap(ar,n):
    i=0
    for i in range(n//2-1,-1,-1):
        heapify(ar,i,n)

def heapSort(ar,n):
    i =0
    buildHeap(ar,n)
    for i in range(n-1,0,-1):
        ar[0],ar[i] = swap(ar[0],ar[i])
        heapify(ar,0,i)
