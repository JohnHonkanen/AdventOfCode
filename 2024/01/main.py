import time

def read_input(filename):
    with open(filename, 'r', encoding='utf-8-sig') as f:
        column1, column2 = [], []
        for line in f:
            columns = line.split()
            column1.append(int(columns[0]))
            column2.append(int(columns[1]))
    return column1, column2

def find_distance(column1, column2):
    start_time = time.perf_counter()

    sorted1 = sorted(column1)
    sorted2 = sorted(column2)

    print(sum(map(lambda a,b: abs(a-b), sorted1, sorted2)))

    # distance = sum(abs(a - b) for a, b in zip(sorted1, sorted2))
    # print(distance)
    end_time = time.perf_counter()  # Record the end time
    elapsed_time = end_time - start_time  # Calculate elapsed time

    print(f"Elapsed time: {elapsed_time:.6f} seconds")

def find_similarity(column1, column2):
    counts = {}

    for num in column2:
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1


    similarity = 0

    for num in column1:
        if num in counts and counts[num] > 0:
            similarity += num *  counts[num]

    print(similarity)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    column1, column2 = read_input('input.txt')
    find_distance(column1, column2)
    # find_similarity(column1, column2)



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
