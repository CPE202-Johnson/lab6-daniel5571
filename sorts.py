import random
import time

def selection_sort(list):
    comparisons = 0                    #not sure if this is correct
    for i in range(len(list)):
        minPosition = i
        for j in range(i+1, len(list)):
            # print(list)
            comparisons +=1
            if list[minPosition] > list[j]:
                minPosition = j
        list[i], list[minPosition] = list[minPosition], list[i]
    return comparisons

def insertion_sort(list):
    comparisons = 0
    for i in range(1, len(list)):
        for k in range(i):
            # print(list)
            comparisons += 1
            if list[i-k] < list[i-k-1]:
                list[i-k], list[i-k-1] = list[i-k-1], list[i-k]
            else:
                break
    return comparisons

# print(insertion_sort([8, 7, 6, 5, 4, 3, 2, 1]))

def main():
    # Code coverage NOT required for main
    # Give the random number generator a seed, so the same sequence of
    # random numbers is generated at each run
    random.seed(1234)

    # Generate 5000 random numbers from 0 to 999,999
    randoms = random.sample(range(1000000), 5000)
    start_time = time.time()
    comps = selection_sort(randoms)
    stop_time = time.time()
    print(comps, stop_time - start_time)

if __name__ == '__main__':
    main()

