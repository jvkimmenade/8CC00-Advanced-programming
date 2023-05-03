# def import_interval_set(filename="sample_set1.txt"):

filename="sample_set1.txt"
f = open(filename, "r")
interval_set = []

for line in f:
    interval_list = line.strip()
    interval_list = interval_list.replace("[", "").replace("]", "").split(",")
    # interval_list = list(map(int, interval_list))
    # interval_list = [interval_list[i:i + 2] for i in range(0, len(interval_list), 2)]
    # interval_set.append(interval_list)
f.close()
    # return interval_set


# interval1 = import_interval_set("sample_set1.txt")[0][0]
# interval2 = import_interval_set("sample_set2.txt")[0][0]

# def check_overlap_between_intervals(interval1,interval2):