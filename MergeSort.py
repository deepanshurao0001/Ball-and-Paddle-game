import time

def merge(data, l, m, r,drawData,timeTick):
    n1 = m - l + 1
    n2 = r - m
 
    L = [0] * (n1)
    R = [0] * (n2)
 
    for i in range(0, n1):
        L[i] = data[l + i]
 
    for j in range(0, n2):
        R[j] = data[m + 1 + j]
 
    i = 0 
    j = 0 
    k = l 
 
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            data[k] = L[i]
            i += 1
            drawData(data)
            time.sleep(timeTick)

        else:
            data[k] = R[j]
            j += 1
            drawData(data)
            time.sleep(timeTick)
        k += 1
 
    while i < n1:
        data[k] = L[i]
        i += 1
        k += 1
        drawData(data)
        time.sleep(timeTick)
 
    while j < n2:
        data[k] = R[j]
        j += 1
        k += 1
        drawData(data)
        time.sleep(timeTick)

def mergeSort(data,l,r,drawData,timeTick):
    if l < r:
        m = l+(r-l)//2
 
        mergeSort(data, l, m,drawData,timeTick)
        mergeSort(data, m+1, r,drawData,timeTick)
        merge(data, l, m, r,drawData,timeTick)