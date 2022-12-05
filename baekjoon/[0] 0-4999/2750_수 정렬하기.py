n = int(input())

lst = []

for i in range(n):
    lst.append(int(input()))

#print(lst)

#what Sorting to use
#bubble sort
def bubble_sort(arr):
    for i in range(len(arr),0,-1):
        for j in range(0,i-1):
            if lst[j]>lst[j+1]:
                temp = lst[j+1]
                lst[j+1]=lst[j]
                lst[j]=temp
    #print(lst)
    for i in range(n):
        print(lst[i])

#selection sort
def selection_sort(arr):
    for i in range(len(lst)-1):
        least = i
        for j in range(i+1,n):
            if lst[j] < lst[least]:
                least=j
        lst[i], lst[least] = lst[least], lst[i]
    print(lst)

#insertion sort
def insertion_sort(arr):
    for end in range(1, len(arr)):
        for i in range(end, 0, -1):
            if arr[i-1] > arr[i]:
                arr[i-1], arr[i] = arr[i], arr[i-1]
    print(lst)

insertion_sort(lst)
bubble_sort(lst)
selection_sort(lst)