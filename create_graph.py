import igraph as ig
from igraph import *

g = ig.Graph(directed=True)
g.degree(mode="in")
# left/right, up/down, wall up/down, biuro/odbiór - hall righ/left, biuro/odbiór - hall up/down
lenght = [0.75+12+1.5, 1+2.6+1, 0.75+0.75, 1, 1.5]
weight=[]

def create_g():
    for i in range(5):
        if (i+1)!=1 and (i+1)!=5:
            for j in range(7):
                for k in range(3):
                    g.add_vertex(str((i+1)*100 + (j+1)*10 + (k+1)))
        else:
            for j in range(7):
                for k in range(3):
                    if j>=4 and (k+1)==3:
                        continue
                    g.add_vertex(str((i+1)*100 + (j+1)*10 + (k+1)))
    g.add_vertex("100")
    g.add_vertex("500")

    for i in range(5):
        
        #H2,3,4
        if (i+1)!=1 and (i+1)!=5:
            for j in range(7):
                    for k in range(3):
                        # up
                        if j!=0:
                            g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j)*10 + (k+1)))
                            weight.append(lenght[1])
                        #down
                        if j!=6:
                            g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+2)*10 + (k+1)))
                            weight.append(lenght[1])
                        #right
                        if (j+1)%2 != 0:
                            if k!=2:
                                g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+1)*10 + (k+2)))
                                weight.append(lenght[0])
                        #left
                        else:
                            if k!=0:
                                g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+1)*10 + k))
                                weight.append(lenght[0])
        
        #H1,5
        else:
                for j in range(7):
                        for k in range(3):
                            # no vertex in biuro and pkt odbioru
                            if (i+1)*100 + (j+1)*10 + (k+1) == (i+1)*100 + (j+1)*10 + 3 and j>=4:
                                continue
                            #up
                            if j != 0:
                                g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j)*10 + (k+1)))
                                weight.append(lenght[1])
                            # down
                            if j!=6 :
                                #not into/in biuro or pkt odbioru
                                if not((i+1)*100 + (j+2)*10 + (k+1) == (i+1)*100 + (j+2)*10 + 3 and (j+1)>=4):
                                        #continue
                                    g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+2)*10 + (k+1)))
                                    weight.append(lenght[1])
                                
                            #right
                            if (j+1)%2 != 0:
                                if k!=2:
                                    #potrzebne???????????????
                                    if not((i+1)*100 + (j+1)*10 + (k+2) == (i+1)*100 + (j+1)*10 + 3 and j>=4):
                                        
                                        g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+1)*10 + (k+2)))
                                        weight.append(lenght[0])
                            #left    
                            else:
                                if k!=0:
                                    g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+1)*10 + k))
                                    weight.append(lenght[0])
                                    

    g.add_edge("172", "312")
    weight.append(lenght[1])
    g.add_edge("312", "172")
    weight.append(lenght[1])

    g.add_edge("223", "321")
    weight.append(lenght[2])
    g.add_edge("321", "223")
    weight.append(lenght[2])

    g.add_edge("263", "351")
    weight.append(lenght[2])
    g.add_edge("351", "263")
    weight.append(lenght[2])

    g.add_edge("272", "412")
    weight.append(lenght[1])
    g.add_edge("412", "272")
    weight.append(lenght[1])

    g.add_edge("453", "551")
    weight.append(lenght[2])
    g.add_edge("551", "453")
    weight.append(lenght[2])

    g.add_edge("423", "521")
    weight.append(lenght[2])
    g.add_edge("521", "423")
    weight.append(lenght[2])

    g.add_edge("372", "512")
    weight.append(lenght[1])
    g.add_edge("512", "372")
    weight.append(lenght[1])

    g.add_edge("100","143")
    weight.append(lenght[3])
    g.add_edge("100","142")
    weight.append(lenght[4]*1.4)
    g.add_edge("100","152")
    weight.append(lenght[4])
    g.add_edge("100","162")
    weight.append(lenght[4])
    g.add_edge("100","172")
    weight.append(lenght[4])

    g.add_edge("500","543")
    weight.append(lenght[3])
    g.add_edge("500","542")
    weight.append(lenght[4]*1.4)
    g.add_edge("500","552")
    weight.append(lenght[4])
    g.add_edge("500","562")
    weight.append(lenght[4])
    g.add_edge("500","572")
    weight.append(lenght[4])

    g.add_edge("543","500")
    weight.append(lenght[3])
    g.add_edge("542","500")
    weight.append(lenght[4]*1.4)
    g.add_edge("552","500")
    weight.append(lenght[4])
    g.add_edge("562","500")
    weight.append(lenght[4])
    g.add_edge("572","500")
    weight.append(lenght[4])

    g.es['weight'] = weight     

def calculate_shortest_path_weight(start_point, end_point):
    if start_point == end_point:
        return 0
    
    shortest_path_indices = g.get_shortest_paths(g.vs.find(name=start_point), to=g.vs.find(name=end_point), output="vpath")[0]
    shortest_path_ids = [g.vs[idx]["name"] for idx in shortest_path_indices]

    shortest_path_edges = list(zip(shortest_path_indices[:-1], shortest_path_indices[1:]))
    shortest_path_weights = [g.es[g.get_eid(edge[0], edge[1])]["weight"] for edge in shortest_path_edges]

    shortest_path_string = " -> ".join(shortest_path_ids)
    print(f"The shortest path is: {shortest_path_string}")

    sum_of_weights = sum(shortest_path_weights)
    print(f"Sum of weights along the shortest path: {sum_of_weights}")
    return shortest_path_string

def convert_package_id(tabPackageId):
    vertex_list=[]
    for index,string in enumerate(tabPackageId, start=1):
        hall = string[1]
        alley = string[3]
        shelf = string[5:7]

        if int(alley)%2 != 0:
            if int(shelf) <= 8:
                vertex_to_find = int(hall)*100 + int(alley)*10 + 1
            else:
                vertex_to_find = int(hall)*100 + int(alley)*10 + 2
        else:
            if int(shelf) <= 8:
                vertex_to_find = int(hall)*100 + int(alley)*10 + 3
            else:
                vertex_to_find = int(hall)*100 + int(alley)*10 + 2
        #print(vertex_to_find)
        vertex_list.append((vertex_to_find,shelf))
    return vertex_list


from sys import maxsize 
from itertools import permutations
def travellingSalesmanProblem(list, s): 
    # store all vertex apart from source vertex 

    vertex = [] 
    list_ve = [] 
    list_she = [] 
    for i in list:
        list_1,list_2 = i
        list_ve.append(list_1)
        list_she.append(list_2)

    for i in list_ve: 
        if i != s:
            vertex.append(i)
 
    # store minimum weight Hamiltonian Cycle 
    min_path = maxsize
    route=[]
    next_permutation = permutations(vertex)
    for i in next_permutation:
 
        #store current Path weight(cost)
        current_pathweight = 0

        curr_route=[]
        #compute current path weight 
        k = s
        for j in i:
            current_pathweight += calculate_shortest_path_weight(k, j)
            #current_pathweight += int(list_she)
            curr_route.append(j)
            k = j

        
        
        current_pathweight += calculate_shortest_path_weight(k, "500")
        curr_route.append("500")
 
        #update minimum
        if current_pathweight<min_path:
            min_path=current_pathweight
            route=curr_route
    return (min_path,route)


def get_palette(package_list):
    packages_Idshelf = convert_package_id(package_list)
    travellingSalesmanProblem(packages_Idshelf,"100")
    ################################### jak dalej palety?
    
create_g()
print(g)
#print(g.es['weight'])
calculate_shortest_path_weight("111","131")

list = convert_package_id(["H102A02","H103A09"])

for i in list:
    print(i)