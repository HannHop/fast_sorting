# Hanna Hopkowicz macro sem 6
import random
import time
from files import *

def check_is_sorted(arr):
    i = 1
    is_sorted = 1
    while i < len(arr)-1 and is_sorted:
        if arr[i - 1] > arr[i]:
            is_sorted = 0
            print("Array is UNSORTED!")
        i = i + 1
    if is_sorted:
        print("Array is SORTED :)")


def shell_sort(arr):  # 'default' shell sequence N/2^k, k>=1
    n = len(arr)
    h = n // 2
    while h > 0:
       # print("h: ", h)
        for i in range(h, n):
            x = arr[i]
            j = i
            while j >= h and x < arr[j - h]:
                arr[j] = arr[j - h]
                j = j - h
            arr[j] = x
        h = h//2


def shell_sort_2(arr):  # using sequence experimentally derived by Ciura
    sequence = [701, 301, 132, 57, 23, 10, 4, 1]
    n = len(arr)
    for h in sequence:
       # print("h: ", h)
        for i in range(h, n):
            x = arr[i]
            j = i
            while j >= h and x < arr[j - h]:
                arr[j] = arr[j - h]
                j = j - h
            arr[j] = x


def shell_sort_3(arr):  # using Hibbard's sequence 2^k - 1
    n = len(arr)
    h = 1
    k = 2
    while h < n:
        h = 2 ** k - 1
        k = k + 1

    while h > 0:
       # print("h: ", h)
        for i in range(h, n):
            x = arr[i]
            j = i
            while j >= h and x < arr[j - h]:
                arr[j] = arr[j - h]
                j = j - h
            arr[j] = x
        h = 2**k - 1
        k = k - 1


def quick_sort_1(arr, left_index, right_index):  # pivot <- most left element
    #print(arr)
    if left_index < right_index:
        pivot = arr[left_index]
        s = left_index
        for i in range(left_index + 1, right_index):  # rearrange elements in arr
            if arr[i] < pivot:
                s = s + 1
                arr[s], arr[i] = arr[i], arr[s]
        arr[s], arr[left_index] = arr[left_index], arr[s]
        quick_sort_1(arr, left_index, s)  # call recursively for left part up to 1 before pivot
        quick_sort_1(arr, s + 1, right_index)  # call recursively for right part, from 1 after pivot to end


def insertion_sort(arr, left_index, right_index):
    for i in range(left_index + 1, right_index):
        j = i
        while j > 0 and arr[j-1] > arr[j]:  # search for smaller element than last element on left (sorted) sublist
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
            j = j - 1
            #print(arr)



def quick_insert(arr, left_index, right_index):  # randomize pivot and swap it with most left element
    #print(arr)
    if left_index < right_index:
        if right_index - left_index < 10:  # when array smaller than ten is considered, use insertion sort
            insertion_sort(arr, left_index, right_index)
            return
        pivot = arr[left_index]
        s = left_index
        for i in range(left_index + 1, right_index):  # rearrange elements in arr
            if arr[i] < pivot:
                s = s + 1
                arr[s], arr[i] = arr[i], arr[s]
        arr[s], arr[left_index] = arr[left_index], arr[s]
        quick_insert(arr, left_index, s)  # call recursively for left part up to 1 before pivot
        quick_insert(arr, s + 1, right_index)  # call recursively for right part, from 1 after pivot to end



def quick_sort_2(arr, left_index, right_index):  # pivot <- random element
    #print(arr)
    if left_index < right_index:
        x = random.randint(left_index, right_index - 1)  # -1 to not go outside range
        pivot = arr[x]
        arr[x], arr[left_index] = arr[left_index], arr[x]
        s = left_index
        for i in range(left_index + 1, right_index):  # rearrange elements in arr
            if arr[i] < pivot:
                s = s + 1
                arr[s], arr[i] = arr[i], arr[s]
        arr[s], arr[left_index] = arr[left_index], arr[s]
        quick_sort_2(arr, left_index, s)  # call recursively for left part up to 1 before pivot
        quick_sort_2(arr, s + 1, right_index)  # call recursively for right part, from 1 after pivot to end



def quick_sort_3(arr, left_index, right_index):  # pivot <- median of three
    #print(arr)
    if left_index < right_index:
        three_val = [random.randint(left_index, right_index - 1) for _ in range(3)]
        three_val = [[arr[x], x] for x in three_val]
        quick_sort_1(three_val, 0, 3)
        #print("three: ", three_val)
        pivot = three_val[1][0]
        arr[three_val[1][1]], arr[left_index] = arr[left_index], arr[three_val[1][1]]
        s = left_index
        for i in range(left_index + 1, right_index):  # rearrange elements in arr
            if arr[i] < pivot:
                s = s + 1
                arr[s], arr[i] = arr[i], arr[s]
        arr[s], arr[left_index] = arr[left_index], arr[s]
        quick_sort_3(arr, left_index, s)  # call recursively for left part up to 1 before pivot
        quick_sort_3(arr, s + 1, right_index)  # call recursively for right part, from 1 after pivot to end


# ints
#set_ = arr_rand_32k_str
#set_ = arr_rand_64k_str
#set_ = arr_rand_128k_str
#set_ = arr_rand_512k_str
#set_ = arr_rand_1024k_str
# strings
#set_ = arr_rand_128k_int
set_ = arr_rand_512k_int
#set_ = arr_rand_1024k_int
#set_ = arr_rand_2048k_int
#set_ = arr_rand_4096k_int

start = time.perf_counter()
#quick_sort_1(set_, 0, len(set_))
#quick_sort_2(set_, 0, len(set_))
#quick_sort_3(set_, 0, len(set_))
#quick_insert(set_, 0, len(set_))
#shell_sort_3(set_)
#shell_sort_2(set_)
shell_sort(set_)
stop = time.perf_counter()
print(shell_sort.__name__+" has taken:", stop - start, "seconds")
check_is_sorted(set_)

