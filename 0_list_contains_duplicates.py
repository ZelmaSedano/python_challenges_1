def list_contains_duplicates(lst):

    # need to access values, so use range
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            # remember to check the values, not simply the index 
            # lst[i] NOT i
            if lst[i] == lst[j]:
                return True
            
    # backup: if there aren't any duplicates
    return False

print(list_contains_duplicates([1,2,3]))


# 
def list_contains_duplicates(lst):

    # convert the lst into a set, which doesn't have duplidates
    new_lst = set(lst)

    # compare the length of the original lst and the new_lst, if they're the same then the lst doesn't containe duplicates
    # make sure to do the oppposite, since True = duplicates
    return len(new_lst) != len(lst)

print(list_contains_duplicates([1,2,3,3,4]))
