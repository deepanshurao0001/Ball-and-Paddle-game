
import time

def bubble_sort(data,drawData,timeTick):
    for _ in range(len(data)-1):
        for j in range(len(data)-1):
            if data[j] > data[j+1]:
                data[j],data[j+1] = data[j+1],data[j]
                drawData(data)
                time.sleep(timeTick)

