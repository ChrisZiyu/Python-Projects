import random
import time
import matplotlib.pyplot as plt

def bubble_sort(my_list):
    start_time = time.time() # start time
    length = len(my_list)
    operations = 0
    for i in range(length):
        for j in range(length-1):
            operations += 1  # Increment the counter for each comparison
            if my_list[j] > my_list[j+1]:
                my_list[j], my_list[j + 1] = my_list[j + 1], my_list[j]
                operations += 1  # Increment the counter for each swap
    end_time = time.time() # end time
    return operations, end_time - start_time

def selection_sort(my_list):
    start_time = time.time() # start time
    n = len(my_list)
    operations = 0
    for i in range(n):
        smallest_idx = i
        for j in range(i, n - 1):
            operations += 1  # Increment the counter for each comparison
            if my_list[j] > my_list[j+1]:
                smallest_idx = j + 1
        if smallest_idx != i:
            my_list[i], my_list[smallest_idx] = my_list[smallest_idx], my_list[i]
            operations += 1  # Increment the counter for each swap
    end_time = time.time() # end time
    return operations, end_time - start_time

def insertion_sort(my_list):
    start_time = time.time() # start time
    length = len(my_list)
    operations = 0
    for i in range(length):
        j = i
        while j > 0 and my_list[j-1] > my_list[j]:
            my_list[j], my_list[j-1] = my_list[j-1], my_list[j]
            j = j-1
            operations += 1  # Increment the counter for each swap
    end_time = time.time() # end time
    return operations, end_time - start_time

def quick_sort(my_list):
    start_time = time.time() # start time
    operations = 0
    if len(my_list) <= 1:
        return operations, 0

    pivot_index = len(my_list) // 2
    pivot = my_list[pivot_index]
    my_list[pivot_index], my_list[-1] = my_list[-1], my_list[pivot_index]

    i, j = 0, len(my_list) - 2

    while i <= j:
        while my_list[i] < pivot:
            i += 1
            operations += 1  # Increment the counter for each comparison
        while my_list[j] > pivot:
            j -= 1
            operations += 1  # Increment the counter for each comparison
        if i <= j:
            my_list[i], my_list[j] = my_list[j], my_list[i]
            i += 1
            j -= 1
            operations += 1  # Increment the counter for each swap

    my_list[i], my_list[-1] = my_list[-1], my_list[i]
    operations += 1  # Increment the counter for each swap

    left = my_list[:i]
    right = my_list[i + 1:]

    left_operations, left_time = quick_sort(left)
    right_operations, right_time = quick_sort(right)

    end_time = time.time() # end time
    return operations + left_operations + right_operations, end_time - start_time + left_time + right_time

listSize = 100
rand_list = [random.randint(0, 101) for val in range(listSize)]
rand_list.sort(reverse=True)

bubble_sort_ops, bubble_sort_time = bubble_sort(rand_list)
selection_sort_ops, selection_sort_time = selection_sort(rand_list)
insertion_sort_ops, insertion_sort_time = insertion_sort(rand_list)
quick_sort_ops, quick_sort_time = quick_sort(rand_list)

print("steps needed for sorting (Bubble Sort): {} Time taken: {}".format(bubble_sort_ops, bubble_sort_time))
print("steps needed for sorting (Selection Sort): {} Time taken: {}".format(selection_sort_ops, selection_sort_time))
print("steps needed for sorting (Insertion Sort): {} Time taken: {}".format(insertion_sort_ops, insertion_sort_time))
print("steps needed for sorting (Quick Sort): {} Time taken: {}".format(quick_sort_ops, quick_sort_time))

# Plotting
plt.figure(figsize=(10,6))

plt.bar(['Bubble Sort', 'Selection Sort', 'Insertion Sort', 'Quick Sort'],
        [bubble_sort_time, selection_sort_time, insertion_sort_time, quick_sort_time],
        color=['blue', 'red', 'green', 'orange'])

plt.xlabel('Sorting Algorithm')
plt.ylabel('Time taken (in seconds)')
plt.title('Completion time vs. Sorting Algorithm (Worst Case)')
plt.show()
