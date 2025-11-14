def make_a_set(lst):
    duplicates = set()

    for i in lst:
        # if it's not, add to set
        duplicates.add(('hi', i))

    #backup
    return duplicates

print(make_a_set([1,2,3,4,4]))
