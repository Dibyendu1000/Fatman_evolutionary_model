import networkx as nx
import matplotlib.pyplot as plt
import random

def create_graph():
    G=nx.Graph()
    G.add_nodes_from(range(1,101))
    return G

def visualize(G,labeldict,nsize,color,t):
    nx.draw(G,labels=labeldict,node_size=nsize, node_color=color)
    plt.savefig('evolution_'+str(t)+'.png')

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
    foci_nodes=['Gym','Eat-Out','Movie Club','Karate Club','Yoga Club']
    for j in range(0,5):
        G.add_node(i)
        G.node[i]['name']=foci_nodes[j]
        G.node[i]['type']='foci'
        i+=1

def get_colors(G):
    c=[]
    for each in G.nodes():
        if (G.node[each]['type']=='person'):
            if(G.node[each]['name']==15):
                c.append('green')
            elif(G.node[each]['name']==40):
                c.append('yellow')
            else:
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

def homophily(G):
    pnodes=get_person_nodes()
    for u in pnodes:
        for v in pnodes:
            if(u!=v):
                diff=abs(G.node[u]['name']-G.node[v]['name'])
                p=float(1)/(diff+10000)
                r=random.uniform(0,1)
                if(r<p):
                    G.add_edge(u,v)
                    
def cmn(u,v,G):
    nu=set(G.neighbors(u))
    nv=set(G.neighbors(v))
    return len(nu & nv)
    
def closure(G):
    array1=[]
    for u in G.nodes():
        for v in G.nodes():
            if(u!=v and (G.node[u]['type']=='person' or G.node[v]['type']=='person')):
               k=cmn(u,v,G)
               p=1-((1-0.01)**k)
               tmp=[]
               tmp.append(u)
               tmp.append(v)
               tmp.append(p)
               array1.append(tmp)
    for each in array1:
        u=each[0]
        v=each[1]
        p=each[2]
        r=random.uniform(0,1)
        if(r<p):
            G.add_edge(u,v)

def change_bmi(G):
    f_nodes=get_foci_nodes()
    for each in f_nodes:
        if(G.node[each]['name']=='Eat-Out'):
            for each1 in G.neighbors(each):
                if(G.node[each1]['name']!=40):
                    G.node[each1]['name']+=1
        elif(G.node[each]['name']=='Gym'):
            for each1 in G.neighbors(each):
                if(G.node[each1]['name']!=15):
                    G.node[each1]['name']-=1
                    
G=create_graph()
assign_bmi(G)
add_foci_nodes(G)
labeldict=get_labels(G)
add_foci_edges()
for t in range(5):
    homophily(G)
    closure(G)
    change_bmi(G)
    visualize(G,labeldict,get_size(G),get_colors(G),t)
    
