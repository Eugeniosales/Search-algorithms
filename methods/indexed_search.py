def table_index(index):
    size = len(index)
    if size > 9:
        slots = size // 10
    else:
        slots = 1
    i = 0
    
    table = []
    table.append(i) 
    while i <= size:
        i+=slots   
        table.append(i) 

    return table 

def indexed_search(key, array):
    index = table_index(array) 
    print(index)
    counter = 0
    
    for i in index:
        if key >= i:
            lim_inf = i
        elif key < i: 
            lim_sup = i
        else:
            lim_inf = i
            lim_sup = i
            break
    
    
    for i in range(lim_inf, lim_sup):
        #print(i)
        counter+=1 
        if key == i:    
            return counter
    return (-1)

    