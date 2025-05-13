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
