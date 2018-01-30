#Amar Uprety
#Data Structures
#April 4 2016
import timeit
import random



def quickSort(alist):
   quickSortHelper(alist,0,len(alist)-1)

def quickSortHelper(alist,first,last):
   if first<last:

       splitpoint = partition(alist,first,last)

       quickSortHelper(alist,first,splitpoint-1)
       quickSortHelper(alist,splitpoint+1,last)


def partition(alist,first,last):
   pivotvalue = alist[first]

   leftmark = first+1
   rightmark = last

   done = False
   while not done:

       while leftmark <= rightmark and alist[leftmark] <= pivotvalue:
           leftmark = leftmark + 1

       while alist[rightmark] >= pivotvalue and rightmark >= leftmark:
           rightmark = rightmark -1

       if rightmark < leftmark:
           done = True
       else:
           temp = alist[leftmark]
           alist[leftmark] = alist[rightmark]
           alist[rightmark] = temp

   temp = alist[first]
   alist[first] = alist[rightmark]
   alist[rightmark] = temp


   return rightmark



def shortBubbleSort(alist):
    exchanges = True
    passnum = len(alist)-1
    while passnum > 0 and exchanges:
       exchanges = False
       for i in range(passnum):
           if alist[i]>alist[i+1]:
               exchanges = True
               temp = alist[i]
               alist[i] = alist[i+1]
               alist[i+1] = temp
       passnum = passnum-1

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]

        mergeSort(lefthalf)
        mergeSort(righthalf)

        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1

        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1

        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1

def main():
    alist=[]
    b=0
    for i in range(0,100):
        b=random.randrange(1,1000)
        alist.append(b)
    start=timeit.default_timer()
    quickSort(alist)
    stop=timeit.default_timer()
    t1=stop-start
    print ("Quick Sort's runtime",t1)
    alist=[]
    for i in range(0,100):
        b=random.randrange(1,1000)
        alist.append(b)
    start1=timeit.default_timer()
    shortBubbleSort(alist)
    stop1=timeit.default_timer()
    t2=stop1-start1
    print ("Bubble Sort's runtime", t2)
    alist=[]
    for i in range(0,100):
        b=random.randrange(1,1000)
        alist.append(b)
    
    start2=timeit.default_timer()
    mergeSort(alist)
    stop2=timeit.default_timer()
    t3=stop2-start2
    print ("Merge Sort's Runtime", t3)

main()
