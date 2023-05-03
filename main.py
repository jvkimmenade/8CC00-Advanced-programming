set1_path = "sample_set1.txt"
set2_path = "sample_set2.txt"


def read_intervals(filepath):
    with open(filepath, 'r') as f:
        intervals = [line.strip() for line in f.readlines()]
    return [tuple(int(bound.strip('[], ')) for bound in interval.split(',')) for interval in intervals]


list1 = read_intervals(set1_path)[0]
list2 = read_intervals(set2_path)[0]


def temp_func(line1, line2):
    intervals1 = [tuple(line1[i:i + 2]) for i in range(0, len(line1), 2)]
    intervals2 = [tuple(line2[i:i + 2]) for i in range(0, len(line2), 2)]
    return intervals1, intervals2


int1, int2 = temp_func(list1, list2)
print(int1)
print(int2)


def has_overlap(I, L):
    for interval in L:
        if I[0] <= interval[1] and interval[0] <= I[1]:
            return 1
    return 0


def count_overlaps(interval_list1, interval_list2):
    i, j = 0, 0
    count = 0

    while i < len(interval_list1) and j < len(interval_list2):
        if interval_list1[i][1] < interval_list2[j][0]:
            i += 1
        elif interval_list2[j][1] < interval_list1[i][0]:
            j += 1
        else:
            count += has_overlap(interval_list1[i], interval_list2)
            i += 1

    return count


def calc_symmetric_similarity(list1, list2):
    ls_12 = count_overlaps(list1, list2) / max(len(list1), len(list2))
    ls_21 = count_overlaps(list2, list1) / max(len(list1), len(list2))
    return (ls_12 + ls_21) / 2
