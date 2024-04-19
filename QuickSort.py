import time

def partition(data,head,tail,drawData,timeTick):
    border = head
    pivot = data[tail]

    drawData(data)
    time.sleep(timeTick)

    for j in range(head,tail):
        if(data[j] < pivot):
            drawData(data)
            time.sleep(timeTick)
            data[border],data[j] = data[j],data[border]
            border+=1

    drawData(data)
    time.sleep(timeTick)
    data[border],data[tail] = data[tail],data[border]
    return border

def quick_sort(data,head,tail,drawData,timeTick):
    if head < tail:
        partitionIdx = partition(data,head,tail,drawData,timeTick)
    
        quick_sort(data,head,partitionIdx-1,drawData,timeTick)

        quick_sort(data,partitionIdx+1,tail,drawData,timeTick)
