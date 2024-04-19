import time

def selectionSort(data,drawData,timeTick):
    for ind in range(len(data)):
        min_index = ind
        for j in range(ind + 1, len(data)):
            if data[j] < data[min_index]:
                min_index = j
                drawData(data)
                time.sleep(timeTick)

        (data[ind], data[min_index]) = (data[min_index], data[ind])
        drawData(data)
        time.sleep(timeTick)