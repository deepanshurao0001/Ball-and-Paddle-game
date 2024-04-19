import time
import random
 
def bogoSort(data,drawData,timeTick):
    n = len(data)
    while (is_sorted(data)== False):
        shuffle(data,drawData,timeTick)
 
def is_sorted(data):
    n = len(data)
    for i in range(0, n-1):
        if (data[i] > data[i+1] ):
            return False
    return True
 
def shuffle(data,drawData,timeTick):
    n = len(data)
    for i in range (0,n):
        r = random.randint(0,n-1)
        data[i], data[r] = data[r], data[i]
        drawData(data)
        time.sleep(timeTick)