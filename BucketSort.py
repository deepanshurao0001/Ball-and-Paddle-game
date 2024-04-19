import time

def insertionSort(b):
    for i in range(1, len(b)):
        up = b[i]
        j = i - 1
        while j >= 0 and b[j] > up:
            b[j + 1] = b[j]
            j -= 1
        b[j + 1] = up
    return b
 
def bucketSort(data,drawData,timeTick):
    arr = []
    slot_num = 10
    for i in range(slot_num):
        arr.append([])
 
    for j in data:
        index_b = int(slot_num * j)
        arr[index_b].append(j)
 
    for i in range(slot_num):
        arr[i] = insertionSort(arr[i])
        drawData(data)
        time.sleep(timeTick)
 
    k = 0
    for i in range(slot_num):
        for j in range(len(arr[i])):
            data[k] = arr[i][j]
            drawData(data)
            time.sleep(timeTick)
            k += 1

    return data