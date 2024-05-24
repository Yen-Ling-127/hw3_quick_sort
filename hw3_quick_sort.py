from termcolor import colored
color_set = ["red", "yellow", "green", "blue"]

def quicksort(data_set,depth=1,direct=None):
    color = color_set[depth-1]
    
    if len(data_set) <= 1:
        result = data_set
        print(colored(f"Depth: {depth}, {direct if direct else 'Initial'}, Sorted data: {result}" ,color))
        return data_set
    
    pivot = data_set[0]
    left = []
    middle = []
    right = []
    
    for x in data_set:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    if direct == None:
        print(f"Depth: {depth}, Pivot: {pivot}, Left: {left}, Right: {right}")
    else:
        print(f"Depth: {depth}, {direct} of Depth {depth-1}, Pivot: {pivot}, Left: {left}, Right: {right}")
    result = quicksort(left,depth+1,"Left") + quicksort(middle,depth+1,"Pivot") + quicksort(right,depth+1,"Right")
    
    print(colored(f"Depth: {depth}, {direct if direct else 'Initial'}, Sorted data: {result}" ,color))
    return result

data_set = [33, 67, 8, 13, 54, 119, 3, 84, 25, 42]
print(f"Before: {data_set}\n")

sorted_data_set = quicksort(data_set)
print(f"\nAfter: {sorted_data_set}")
