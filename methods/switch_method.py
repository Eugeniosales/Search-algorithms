from methods.linear_search import linear_search
from methods.binary_search import binary_search
from methods.sentinela_search import sentinela_search
from methods.indexed_search import indexed_search
from methods.interpolation_search import interpolation_search

def switch_method(method, max, key):

    array = []
    for i in range (0, max):
        array.append(i)

    if method == 'Linear':
        steps = linear_search(key, array)
        return steps
        
    elif method == 'Sentinela':
        steps = sentinela_search(key, array)
        return steps

    elif method == 'Binaria':
        steps = binary_search(key, array)
        return steps

    elif method == 'Interpolação':
        steps = interpolation_search(key, array)
        return steps
    
    elif method == 'Indexada':
        steps = indexed_search(key, array)
        return steps
