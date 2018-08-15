#----------------------------------------------------
# Blum-Froyd-Pratt-Riverst-Tarjan
# Implementaçao em Python do Algoritmo BFPRT
# Presente no livro Algoritmos  O Guia Essencial
# de Heineman, Pollice e Selkow ex 4-6  
# Versao 0.1 
# Data 01/07/2018
#-----------------------------------------------------
from util import swap
from util import my_cmp
from util import partition

def medianOfFour(ar,left,gap):
    pos1 = left
    pos2 = pos1 + gap
    pos3 = pos2 + gap
    pos4 = pos3 + gap
    a1 = ar[pos1]
    a2 = ar[pos2]
    a3 = ar[pos3]
    a4 = ar[pos4]

    if my_cmp(a1,a2) <= 0:
        if my_cmp(a2,a3) <= 0:
            if my_cmp(a2,a4) <= 0:
                if my_cmp(a3,a4) > 0:
                    ar[pos3],ar[pos4] = swap(ar[pos3],ar[pos4])
            else:
                ar[pos2],ar[pos3] = swap(ar[pos2],ar[pos3])
        else:
            if my_cmp(a1,a3) <= 0:
                if my_cmp(a3,a4) <= 0:
                    if my_cmp(a2,a4) <= 0:
                        ar[pos2],ar[pos3] = swap(ar[pos2],ar[pos3])
                    else:
                        ar[pos3],ar[pos4] = swap(ar[pos3],ar[pos4])
            else:
                if my_cmp(a1,a4) <= 0:
                    if my_cmp(a2,a4) <= 0:
                        ar[pos2],ar[pos3] = swap(ar[pos2],ar[pos3])
                    else:
                        ar[pos3],ar[pos4] = swap(ar[pos3],ar[pos4])
                else:
                    ar[pos1],ar[pos3] = swap(ar[pos1],ar[pos3])
    else:
        if my_cmp(a1,a3) <= 0:
            if my_cmp(a1,a4) <= 0:
                if my_cmp(a3,a4) > 0:
                    ar[pos3],ar[pos4] = swap(ar[pos3],ar[pos4])
            else:
                ar[pos1],ar[pos3] = swap(ar[pos1],ar[pos3])
        else:
            if my_cmp(a2,a3) <= 0:
                if my_cmp(a3,a4) <= 0:
                    if my_cmp(a1,a4) <= 0:
                        ar[pos1],ar[pos3] = swap(ar[pos1],ar[pos3])
                    else:
                        ar[pos3],ar[pos4] = swap(ar[pos3],ar[pos4])
                else:
                    if my_cmp(a2,a4) <= 0:
                        if my_cmp(a1,a4) <= 0:
                            ar[pos1],ar[pos3] = swap(ar[pos1],ar[pos3])
                        else:
                            ar[pos3],ar[pos4] = swap(ar[pos3],ar[pos4])
                    else:
                        ar[pos2],ar[pos3] = swap(ar[pos2],ar[pos3])

def _insertion(ar,low,right,gap):
    for loc in range(low+gap, right +1,gap):
        i = loc - gap
        value = ar[loc]
        while (i >= low) & my_cmp(ar[i],value > 0):
            ar[i + gap] = ar[i]
            i -= gap
        ar[i+gap] = value

def medianOfMedias(ar, left, right, gap):
    span = 4 * gap
    num = (right - left + 1) // span
    if num == 0:
        _insertion(ar,left,right,gap)
        num = (right - left + 1) // gap
        return left + gap*(num - 1)//2            

    s = left
    while s+span < right:
        medianOfFour(ar,s,gap)
        s += span
    if num < 4:
        _insertion(ar,left+span//2,right,span)
        return left + num*span//2
    else:
        return medianOfMedias(ar,left+span//2, s-1,span)

def selectMedian(ar, left, right):
    k = (right-left+1)//2
    while k > 0:
        idx = medianOfMedias(ar,left, right, 1)
        pivotIndex = partition(ar,left,right, idx)
        p = left + k
        if p == pivotIndex:
            return pivotIndex
        elif p < pivotIndex:
            right = pivotIndex - 1
        else:
            k = k - (pivotIndex-left+1)
            left = pivotIndex + 1
    return left








