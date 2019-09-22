def linear_search(key, array):
    counter = 0
    for i in array:
        if i == key:
            return counter
        counter+=1
    
    return -1