import networkx as nx
import matplotlib.pyplot as plt
import pandas as pd
from PIL import Image

# install -i https://pypi.tuna.tsinghua.edu.cn/simple networkx
# install -i https://pypi.tuna.tsinghua.edu.cn/simple matplotlib
# module ‘networkx’ has no attribute ‘Graph’ 解决方法 https://blog.csdn.net/Tan_HandSome/article/details/82661420

# a Graph is a collection of nodes (vertices) along with identified pairs of nodes (called edges, links, etc).
# Nodes can be any hashable object e.g., a text string, an image, an XML object, another Graph, a customized node object, etc.

# basic functions: add_node, add_edge, number_of_nodes, number_of_edges
G = nx.Graph()

# add one node at a time
G.add_node("function")
G.add_node(2)

# add a list of nodes
G.add_nodes_from([2, 3, 4])

# add one edge at a time
G.add_edge(1,2)

# add a list of edges
G.add_edges_from([(1, 2), (1, 3)])

# remove all nodes and edges
# G.clear()

print(G.number_of_nodes())
print(G.number_of_edges())

G.clear()

# 320 Start simple
# https://python-graph-gallery.com/320-basic-network-from-pandas-data-frame/

# G.add_nodes_from(["A", "B", "C", "D"])
# G.add_edges_from([("A", "B"), ("A", "D"), ("A", "C"), ("C", "E")])

# standard answer
# df = pd.DataFrame({ 'from':['A', 'B', 'C','A'], 'to':['D', 'A', 'E','C']})
# # In networkx 2.0 from_pandas_dataframe has been removed, instead we use from_pandas_edgelist
# # G = nx.from_pandas_dataframe(df, 'from', 'to')
# G = nx.from_pandas_edgelist(df, 'from', 'to')

# 321 Custom network look
# https://python-graph-gallery.com/321-custom-networkx-graph-appearance/

# df = pd.DataFrame({ 'from':['A', 'B', 'C','A'], 'to':['D', 'A', 'E','C']})
# G = nx.from_pandas_edgelist(df, 'from', 'to')
# nx.draw(G, with_labels=True, node_size=1500, node_color="skyblue", node_shape="s", alpha=0.5, linewidths=40)

# 322 Network layout possibilities
# you can control the layout of your network.
# there is actually an algorithm that calculate the most optimal position of each node.
# several algorithm have been developed and are proposed by NetworkX.
# df = pd.DataFrame({'from': ['A', 'A', 'A', 'A', 'B', 'C', 'C', 'D', 'E'], 'to': ['B', 'C', 'E', 'D', 'G', 'E', 'F', 'G', 'G']})
# G = nx.from_pandas_edgelist(df, 'from', 'to')

# 323 Directed or Undirected network
# Network charts can be split in 2 main categories: directed and undirected networks.
df = pd.DataFrame({'from': ['A'], 'to': ['B']})
dG = nx.from_pandas_edgelist(df, 'from', 'to', create_using=nx.DiGraph())

# nx.draw(G, with_labels=True, font_weight='bold', pos=nx.spectral_layout(G))
nx.draw(dG, with_labels=True, font_weight='bold')
plt.show()

# plt.savefig("path.png")

# 图片处理 https://www.cnblogs.com/denny402/p/5096001.html
# img = Image.open("path.png")
# img.show()