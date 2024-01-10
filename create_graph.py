import igraph as ig

g = ig.Graph(directed=True)
g.degree(mode="in")
lenght = [0.75+12+1.5,1+2.6+1]
weights=[]

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
        if (i+1)!=1 and (i+1)!=5:
            for j in range(7):
                    for k in range(3):
                        if j!=0:
                            g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j)*10 + (k+1)))
                        if j!=6:
                            g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+2)*10 + (k+1)))
                        
                        if (j+1)%2 != 0:
                            if k!=2:
                                g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+1)*10 + (k+2)))
                        else:
                            if k!=0:
                                g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+1)*10 + k))
        
        else:
                for j in range(7):
                        for k in range(3):
                            if (i+1)*100 + (j+1)*10 + (k+1) == (i+1)*100 + (j+1)*10 + 3 and j>=4:
                                continue

                            if j != 0:
                                g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j)*10 + (k+1)))
                                
                            if j!=6 :
                                if (i+1)*100 + (j+2)*10 + (k+1) == (i+1)*100 + (j+2)*10 + 3 and (j+1)>=4:
                                        continue
                                g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+2)*10 + (k+1)))
                                
                            
                            if (j+1)%2 != 0:
                                if k!=2:
                                    if (i+1)*100 + (j+1)*10 + (k+2) == (i+1)*100 + (j+1)*10 + 3 and j>=4:
                                        continue
                                    g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+1)*10 + (k+2)))
                                    
                            else:
                                if k!=0:
                                    g.add_edge(str((i+1)*100 + (j+1)*10 + (k+1)), str((i+1)*100 + (j+1)*10 + k))
                                    

    g.add_edge("172", "312")
    g.add_edge("312", "172")

    g.add_edge("223", "321")
    g.add_edge("321", "223")

    g.add_edge("263", "351")
    g.add_edge("351", "263")

    g.add_edge("272", "412")
    g.add_edge("412", "272")

    g.add_edge("453", "551")
    g.add_edge("551", "453")

    g.add_edge("423", "521")
    g.add_edge("521", "423")

    g.add_edge("372", "512")
    g.add_edge("512", "372")

    g.add_edge("100","143")
    g.add_edge("100","142")
    g.add_edge("100","152")
    g.add_edge("100","162")
    g.add_edge("100","172")

    g.add_edge("500","543")
    g.add_edge("500","542")
    g.add_edge("500","552")
    g.add_edge("500","562")
    g.add_edge("500","572")     


create_g()
print(g)