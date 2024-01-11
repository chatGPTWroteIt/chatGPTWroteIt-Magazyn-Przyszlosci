from collections import defaultdict

# generating unique combinations of one-side package lengths that will sum up to target number 
def unique_sizes_combinations(unique_numbers, target_sum):
    combinations = [[] for _ in range(target_sum + 1)]
    combinations[0] = [{x:0 for x in unique_numbers}]

    for num in unique_numbers:
        for i in range(num, target_sum + 1):
            for prev_combo in combinations[i - num]:
                new_combo = prev_combo.copy()
                new_combo[num] += 1
                combinations[i].append(new_combo)

    return combinations[target_sum]

def addDict(a,b):
    return {key:value+b[key] for key,value in a}



def multiplyDict(a, num):
    return {key:(value * num) for key, value in a}


def is_optimal(a, supply, length):

    for i in range(0, length):
        s = 0
        for key, value in a.items():
            s += (key[i][1] * value)
            if( s > supply[key[i][0]]):
                return False
    
    return True

def check_optimal(supply, combinations):
    for i in range(0, len(combinations)):
        for j in range(0, len(combinations[i])):
            for key, value in combinations[i][j].items():
               if is_optimal(combinations[i][j], supply, len(supply.keys())) == False:


def dicts_to_keys(dict_list):
    return [tuple(dictionary.items()) for dictionary in dict_list]

def sum_internal(dick):
    return sum([key*value for key,value in dick.items()])

def unpack_package_types(supply):
    package_types = {}
    for x,y,count in supply:
        x, y = min(x,y), max(x,y)
        if x in package_types:
            package_types[x] += count
        else:
            package_types[x] = count
        
        if y in package_types:
            package_types[y] += count
        else:
            package_types[y] = count
    restrains = {(x,y):count}
    return (package_types, restrains)


def affordable_rows(supply, row_lenght):
    #package = unpack_package_types(supply)

    row_types = unique_sizes_combinations(supply.keys(), row_lenght)
    row_types = dicts_to_keys(row_types)
    maximum = sum_internal(supply)//row_lenght + 1

    combinations = [[] for _ in range(maximum)]
    combinations[0] = [{x:0 for x in row_types}]

    for row_type in row_types:
        for i in range(1, maximum):
            # print(row)
            for prev_combo in combinations[i - 1]:
                #print(combinations[i-1])
                new_combo = prev_combo.copy()
                # print(f"{new_combo} for {i}")
                new_combo[row_type] += 1 
                # print(f"new combo {new_combo}")
                combinations[i].append(new_combo)
    return combinations

# a = affordable_rows({200:30, 300:40, 260:20},1200)
b = {200:3, 300:2}
a = affordable_rows(b,600)

print(a)

# {200:30, 300:40, 260:20}

#for i in range(3000):
#   if i % 100 == 0:
#        print(i)
#    a = affordable_rows({200:30, 300:40, 260:20},1200)

#print(affordable_rows({200:30, 300:40, 260:20},1200))



