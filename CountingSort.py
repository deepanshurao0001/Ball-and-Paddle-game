import time

def countingSort(data,drawData,timeTick):
    M = max(data)
    count_array = [0] * (M + 1)
    for num in data:
        count_array[num] += 1
 
    for i in range(1, M + 1):
        count_array[i] += count_array[i - 1]
 
    output_array = [0] * len(data)
 
    for i in range(len(data) - 1, -1, -1):
        output_array[count_array[data[i]] - 1] = data[i]
        count_array[data[i]] -= 1
        drawData(output_array)
        time.sleep(timeTick)
 
    drawData(output_array)
    time.sleep(timeTick)