# create a code challenge that gets the key with the highest value in a dictionary
def max_key_dictionary(dictionary):
    return max(dictionary, key=dictionary.get)

print(max_key_dictionary({'a':1, 'b':2, 'c':3}))
