from collections import defaultdict

# generating unique combinations of one-side package lengths that will sum up to target number 
def unique_sizes_combinations(unique_numbers, target_sum):
    combinations = [[] for _ in range(target_sum + 1)]
    combinations[0] = [{unique_numbers[i][0]:0 for i in range(0, len(unique_numbers))}]

    for n in range(0, len(unique_numbers)):
        num = unique_numbers[n][0]
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
    score = 0
    for i in range(0, length):
        s = 0
        for key, value in a.items():
            s += (key[i][1] * value)
            # ilosc w magazynie
            magazine = supply[key[i][0]]
            if(s > magazine):
                # invalid solution
                score = 10000
                return score
        score += (supply[key[i][0]] - s)
    return score

def countRows(a):
    suma = 0
    for x in a:
        for y in x:
            for key,value in a.items():
                suma+=value
    return suma

def tupleSum(a,b):
    c = ((a[0][0]+b[0][0], a[0][1]+b[0][1]),(a[1][0]+b[1][0], a[1][1]+b[1][1]),(a[2][0]+b[2][0],a[2][1]+b[2][1]))
    return c

def multiplyTuple(a,num):
    total = ((0,0),(0,0),(0,0))
    for _ in range(num):
        total = tupleSum(a, total)
    return total



def findBest(a,supply):
    for x in a:
        for y in x:
                    
            dictSum = ((0,0),(0,0),(0,0))
            for key,value in y.items():
                dictSum = tupleSum(dictSum,key)
                dictSum = multiplyTuple(dictSum, value)
            
    print(dictSum)
    print(supply)



def transform(a, b):
    min_score = 1000
    min_comb = -1
    for x in a:
        for y in x:
            for key,value in y.items():
                tmp = b.copy()
                tsum = 0
                for size,count in key:
                    t = tmp[size] - (count*value)
                    tmp.update({size: t})
                    if(tmp[size] < 0):
                        break
                    tsum += t
                    if min_comb == -1 or min_score > tsum:
                        #print(key,value, tmp)
                        min_score = tsum
                        min_comb = {key:value}
    return min_comb

def dicts_to_keys(dict_list):
    return [tuple(dictionary.items()) for dictionary in dict_list]

def sum_internal(dict_list):
    return sum([key*value for key,value in dict_list.items()])

def sum_internal_tuple(unique_numbers):
    return sum([unique_numbers[i][0]*unique_numbers[i][1] for i in range(0, len(unique_numbers))])

def unpack_package_types(supply):
    package_types = {}
    for x, count in supply:
        x, y = min(x,y), max(x,y)
        if x in package_types:
            package_types[x] += count
        else:
            package_types[x] = count
        
        if y in package_types:
            package_types[y] += count
        else:
            package_types[y] = count
    #restrains = {(x,y):count}

    # print(package_types)
    return (package_types, restrains)


def affordable_rows(supply, row_lenght):
    #supply= unpack_package_types(packages)

    row_types = unique_sizes_combinations(supply, row_lenght)
    row_types = dicts_to_keys(row_types)
    maximum = sum_internal_tuple(supply)//row_lenght + 1

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
#b = {200:3, 300:2, 10
##0:2}
#a = affordable_rows(((200, 3), (300, 2), (100, 4)), 1200)
#print(transform(a, b))

#print(transform(b, a))
# print(countRows(a))
# findBest(a, b)
# print(a)

#print(len(b.keys()))
#check_optimal(b, a)

# {200:30, 300:40, 260:20}

#for i in range(3000):
#   if i % 100 == 0:
#        print(i)
#    a = affordable_rows({200:30, 300:40, 260:20},1200)

#print(affordable_rows({200:30, 300:40, 260:20},1200))



