def read_intervals(filepath: str) -> list:
    """ Function that reads a file containing a set of intervals and returns a list of which each element is
    a line within the file, containing the interval stored in a tuple.

    :param filepath: The path to the file containing the intervals (str).
    :return: A list of tuples representing the intervals (list).
    """
    with open(filepath, 'r') as f:
        intervals = [line.strip() for line in f.readlines()]
        intervals = [tuple(int(bound.strip('[], ')) for bound in interval.split(',')) for interval in intervals]
        intervals = [[tuple(line[i:i + 2]) for i in range(0, len(line), 2)] for line in intervals]
    return intervals


def has_overlap(interval: tuple, list_of_intervals: list) -> int:
    """ Function that checks if the interval has an overlap with an interval from the
    list of intervals and returns 1 if so, otherwise 0.

    :param interval: Interval that needs to be compared (tuple)
    :param list_of_intervals: list of tuples with an interval (list)
    :return: Integer that indicates overlap; 1 = overlap, 0 = no overlap.
    """
    for tmp_interval in list_of_intervals:
        if interval[0] <= tmp_interval[1] and tmp_interval[0] <= interval[1]:
            return 1
    return 0


def count_overlaps(interval_list1: list, interval_list2: list) -> int:
    """ Function that counts the number of overlaps between interval_list1 and
    interval_list2.

    :param interval_list1: First list.
    :param interval_list2: Second list with which the first list is compared with.
    :return: Integer that stores the number of overlaps.
    """

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


def calc_symmetric_list_similarity(list1: list, list2: list) -> float:
    """ Function that calculates the symmetric similarity metric between two single lists.

    :param list1: List 1 that contains intervals stored in tuples.
    :param list2: List 2 that contains intervals stored in tuples.
    :return: Float number that stores the similarity metric.
    """
    ls_12 = count_overlaps(list1, list2) / max(len(list1), len(list2))
    ls_21 = count_overlaps(list2, list1) / max(len(list1), len(list2))
    return (ls_12 + ls_21) / 2


def similarity(set_1='set1.txt', set_2='set2.txt', outfile='similarity.txt'):
    """ Function that takes two sets of intervals and calculates the similarity metric
    between these. File paths (string) of both text files should be provided each
    containing a set of intervals. Each line within the text files can contain multiple
    intervals formatted as "[x,y], [k,l], ..., [m,n]\n". An output file "similarity.txt" is
    created containing the similarity value rounded on two decimals.

    :param set_1: File path or name (string) of the text file containing the first set.
    :param set_2: File path or name (string) of the text file containing the first set.
    """
    set1 = read_intervals(set_1)
    set2 = read_intervals(set_2)

    if len(set1) != len(set2):
        print("ERROR: sets are not equal in length!")
        return
    else:
        list_similarity_summation = 0
        for list_index in range(len(set1)):
            list_similarity_summation += calc_symmetric_list_similarity(set1[list_index], set2[list_index])

    avg_similarity = list_similarity_summation / len(set1)
    with open(outfile, 'w') as f:
        f.write('{:.2f}'.format(avg_similarity))

    return
