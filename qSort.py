#----------------------------------------------------
# Quik Sort                            
# Implementaçao em Python do Algoritmo Quik Sort 
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow
# Versao 0.1 
# Data 17/07/2018
#-----------------------------------------------------
from util import swap
from util import my_cmp
from util import partition
from MedianSort import selectKth
from InsertionSort import insertion
import BFPRT

def sort(A):
    qSort(A,0,len(A)-1)


def qSort(A, left, right):
    minSize = 3
    if left < right:
        pivotIndex = selectPivotIndex(A,left,right)
        pivotIndex = partition(A,left,right,pivotIndex)    
        if pivotIndex - 1 - left <= minSize:
            insertion(A,left, pivotIndex -1)
        else:
            qSort(A,left,pivotIndex-1)
        if right -pivotIndex - 1 <= minSize:
            insertion(A, pivotIndex +1,right)    
        else:
            qSort(A,pivotIndex+1, right)
            

def selectPivotIndex(ar,left,right):
    return BFPRT.selectMedian(ar,left,right)
