import networkx as nx
import matplotlib.pyplot as plt
import random

def create_graph():
    G=nx.Graph()
    G.add_nodes_from(range(1,101))
    return G

def visualize(G,labeldict,nsize,color):
    nx.draw(G,labels=labeldict,node_size=nsize, node_color=color)
    plt.show()

def assign_bmi(G):
    for each in G.nodes():
        G.node[each]['name']=random.randint(15,40)
        G.node[each]['type']='person'
    
def get_labels(G):
    dict1={}
    for each in G.nodes():
        dict1[each]=G.node[each]['name']
    return dict1

def get_size(G):
    array1=[]
    for each in G.nodes():
        if(G.node[each]['type']=='person'):
            array1.append(G.node[each]['name']*20)
        else:
            array1.append(1000)
    return array1

def add_foci_nodes(G):
    n=G.number_of_nodes()
    i=n+1
    foci_nodes=['gym','eatout','movie_club','karate_club','yoga_club']
    for j in range(0,5):
        G.add_node(i)
        G.node[i]['name']=foci_nodes[j]
        G.node[i]['type']='foci'
        i+=1

def get_colors(G):
    c=[]
    for each in G.nodes():
        if (G.node[each]['type']=='person'):
            c.append('blue')
        else:
            c.append('red')
    return c

def get_foci_nodes():
    f=[]
    for each in G.nodes():
        if (G.node[each]['type']=='foci'):
            f.append(each)
    return f

def get_person_nodes():
    p=[]
    for each in G.nodes():
        if (G.node[each]['type']=='person'):
            p.append(each)
    return p

def add_foci_edges():
    foci_nodes=get_foci_nodes()
    people_nodes=get_person_nodes()
    for each in people_nodes:
        r=random.choice(foci_nodes)
        G.add_edge(each,r)
    
        
    

G=create_graph()
assign_bmi(G)
add_foci_nodes(G)
add_foci_edges()
labeldict=get_labels(G)
visualize(G,labeldict,get_size(G),get_colors(G))
assign_bmi(G)

