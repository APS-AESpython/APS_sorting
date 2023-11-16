from utils import read_txt as rtxt
import time

selected_file, list_of_numbers = rtxt.read_file_content()
print(list_of_numbers)
print("#######################################################")
start_time = time.time()

def binary_search(array, start, end, to_find):
    while start <= end:
        middle = (start + end) // 2
        if array[middle] > to_find:
            end = middle - 1
        elif array[middle] < to_find:
            start = middle + 1
        else:
            return middle
    return start

def binary_insertion_sort(array):
    for i in range(1, len(array)):
        to_insert = array[i]
        to_insert_index = binary_search(array, 0, i - 1, to_insert)
        copy = i
        while copy > to_insert_index:
            array[copy] = array[copy - 1]
            copy -= 1
        array[copy] = to_insert


binary_insertion_sort(list_of_numbers)
print(f'sorted: {list_of_numbers}')
