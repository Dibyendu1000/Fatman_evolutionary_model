import networkx as nx
import matplotlib.pyplot as plt
import random

def create_graph():
    G=nx.Graph()
    G.add_nodes_from(range(1,101))
    return G

def visualize(G,labeldict,nsize):
    nx.draw(G,labels=labeldict,node_size=nsize)
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
        array1.append(G.node[each]['name']*20)
    return array1

G=create_graph()
assign_bmi(G)
labeldict=get_labels(G)
visualize(G,labeldict,get_size(G))
assign_bmi(G)

