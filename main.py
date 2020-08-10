# -*- coding: utf-8 -*-
"""
Created on Mon Aug 10 12:39:38 2020

@author: Aniket Maity
"""

class PriorityQueue(object): 
    def __init__(self): 
        self.queue = [] 
  
    def __str__(self): 
        return ' '.join([str(i) for i in self.queue]) 
  
    # for checking if the queue is empty 
    def isEmpty(self): 
        return len(self.queue) == 0
  
    # for inserting an element in the queue 
    def insert(self, data): 
        self.queue.append(data) 
  
    # for popping an element based on Priority 
    def delete(self): 
        try: 
            max = 0
            for i in range(len(self.queue)): 
                if self.queue[i] > self.queue[max]: 
                    max = i 
            item = self.queue[max] 
            del self.queue[max] 
            return item 
        except IndexError: 
            print() 
            exit()
if __name__ == '__main__': 
    N,K = map(int,input().split())
    myQueue = PriorityQueue()
    listEle = list(map(int,input().split()))
    sumEle = sum(listEle)
    for element in listEle:
        myQueue.insert(element)
#    while(N>0):
#        myQueue.insert(int(input()))
#        N-=1
#    sumEle = sum(myQueue)
    for i in range(K):
        temp = myQueue.delete()
        sumEle-=temp
        temp = int(temp/2)
#        print(temp)
        sumEle+=temp
        myQueue.insert(temp)
    print(sumEle)
