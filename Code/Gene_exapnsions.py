import networkx as nx
import pandas as pd 
import matplotlib.pyplot as plt 
import os 


directory = '/home/andrea/Desktop/magistrale_Qcb/3master_QCB_first_semester_second_year/biological_data_mining_blanzieri/Laboratory_Biological_Data_Mining/Datasets_finals/Expantion' 
nodes=[]
edges = []

human_spec = pd.read_csv('./Datasets_finals/Selected_genes_for_expansion.txt',header= 0)


lista_genes=[]


for dirpath, dirnames, filenames in os.walk(directory): 
    for filename in filenames: 
        #print(dirpath)
        if filename.endswith('.expansion'): 
            print(filename)
            dataset = pd.read_csv(dirpath+"/"+filename,header= 1,skiprows=0)
            for i in range(len(dataset)):
                if dataset.Fabs.iloc[i] >= (2000*0.99):
                    nodes.append(dataset.node.iloc[i])
                    lista_genes.append(dataset.node.iloc[i])
        else:
            dataset_2 = pd.read_csv(dirpath+"/"+filename,skiprows=0,header=1)
            print(filename)
            nodes.append(dataset_2.x.value_counts().idxmax())
            nodes = list(set(nodes))
            for j in range(len(dataset_2)):
                 if dataset_2.Fabs.iloc[j] >= (2000*0.99):
                    momentary = (dataset_2.x.iloc[j],dataset_2.y.iloc[j],int(dataset_2.Fabs.iloc[j])/2000)
                    edges.append(momentary)
                    if dataset_2.x.iloc[j] not in lista_genes:
                        lista_genes.append(dataset_2.x.iloc[j])
                    if dataset_2.y.iloc[j] not in lista_genes:    
                        lista_genes.append(dataset_2.y.iloc[j])


# print(edges)
# print(nodes)

G = nx.DiGraph()
G.add_nodes_from(nodes)
G.add_weighted_edges_from(edges)


color_map =[]
for n in G:
    if n.upper() in list(human_spec['Human_specific']):
        color_map.append('sandybrown')
    else:
        color_map.append('blue')

    
# nx.draw(G,with_labels=True, node_color = color_map)
# plt.show()

node_degree_dict = nx.degree(G)
selected = [x for x in G.nodes() if node_degree_dict[x] > 3]
print(len(selected))
G2 =G.subgraph(selected)

color_map2 =[]
for n in G2:
    if n.upper() in list(human_spec['Human_specific']):
        color_map2.append('sandybrown')
    else:
        color_map2.append('blue')

#nx.draw(G2,with_labels=True, node_color = color_map2)
#plt.show()



listona=[]
for tupla in G2.edges():
    listona.append(tupla[0])
    listona.append(tupla[1])

selected2 = [x for x in G2.nodes() if x in listona]
print(G2.edges())

nodelist=[]
for node in selected2:
    nodelist.extend(list(G.neighbors(n=node)))
    nodelist.append(node)


sub=G.subgraph(nodelist)
color_map3 =[]
for n in sub:
    if n.upper() in list(human_spec['Human_specific']):
        color_map3.append('sandybrown')
    else:
        color_map3.append('blue')


nx.draw(sub,with_labels=True, node_color = color_map3)
plt.show()


graph_1=['grapl', 'lrrc37a', 'lrrc37a3', 'arl17a', 'stag3']

nodelist_graph1=[]

for node in graph_1:
    nodelist_graph1.extend(list(G.neighbors(n=node)))
    nodelist_graph1.append(node)

sub_graph1=G.subgraph(nodelist_graph1)
color_map4 =[]
for n in sub_graph1:
    if n.upper() in list(human_spec['Human_specific']):
        color_map4.append('sandybrown')
    else:
        color_map4.append('blue')

nx.draw(sub_graph1,with_labels=True, node_color = color_map4)
plt.show()


graph_3=['tmem236', 'nrxn3', 'mrc1']

nodelist_graph3=[]

for node in graph_3:
    nodelist_graph3.extend(list(G.neighbors(n=node)))
    nodelist_graph3.append(node)

sub_graph3=G.subgraph(nodelist_graph3)
color_map6 =[]
for n in sub_graph3:
    if n.upper() in list(human_spec['Human_specific']):
        color_map6.append('sandybrown')
    else:
        color_map6.append('blue')

nx.draw(sub_graph3,with_labels=True, node_color = color_map6)
plt.show()



graph_2=['nbpf14','gtf2i','fam156a']

nodelist_graph2=[]

for node in graph_2:
    nodelist_graph2.extend(list(G.neighbors(n=node)))
    nodelist_graph2.append(node)

sub_graph2=G.subgraph(nodelist_graph2)
color_map5 =[]
for n in sub_graph2:
    if n.upper() in list(human_spec['Human_specific']):
        color_map5.append('sandybrown')
    else:
        color_map5.append('blue')

nx.draw(sub_graph2,with_labels=True, node_color = color_map5)
plt.show()


print(lista_genes)
dataframe=pd.DataFrame(lista_genes)
print(dataframe)
dataframe.to_csv('./Datasets_finals/Expansion_genes.csv', index=True)

nodelist_HS=[]
for gene in list(human_spec['Human_specific']):
    nodelist_HS.extend(list(G.neighbors(n=gene.lower())))
    nodelist_HS.append(gene.lower())
    dataframe=pd.DataFrame(nodelist_HS)
    dataframe.to_csv('./Datasets_finals/Expansion_files/'+gene+'.csv', index=True)



dataframe=pd.DataFrame(nodelist_graph1)
dataframe.to_csv('./Datasets_finals/Graph1_5HS.csv', index=True)



dataframe=pd.DataFrame(nodelist_graph2)
dataframe.to_csv('./Datasets_finals/Graph2_3HS.csv', index=True)



dataframe=pd.DataFrame(nodelist_graph3)
dataframe.to_csv('./Datasets_finals/Graph3_3HS.csv', index=True)