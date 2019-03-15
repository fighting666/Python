# -*- coding: utf-8 -*-
import networkx as nx
import matplotlib.pyplot as plt

# # python做网络关系图基础
# # 添加一个点
# DG = nx.DiGraph()  # 有向图
# G = nx.Graph()  # 无向图
# DG.add_node('A')  # 添加一个节点
# G.add_edge(2,3)  #添加一条边
# # 作图，设置节点名显示,节点大小，节点颜色
# nx.draw(DG, with_labels=True, node_size=900, node_color='green')
# plt.show()

# # 双节点，有方向A–>B
# DG = nx.DiGraph()
# DG.add_node('A')  # 添加一个节点
# DG.add_node('B')
# DG.add_edge('A', 'B')  # 添加边，有方向，A-->B
# # 作图，设置节点名显示,节点大小，节点颜色
# nx.draw(DG, with_labels=True, node_size=900, node_color='green')
# plt.show()

# # 添加更多节点
# colors = ['red', 'green', 'blue', 'yellow']
# DG = nx.DiGraph()
# # 一次性添加多节点，输入的格式为列表
# DG.add_nodes_from(['A', 'B', 'C', 'D'])
# # 添加边，数据格式为列表
# DG.add_edges_from([('A', 'B'), ('A', 'C'), ('A', 'D'), ('D', 'A')])
# # 作图，设置节点名显示,节点大小，节点颜色
# nx.draw(DG, with_labels=True, node_size=900, node_color=colors)
# plt.show()


# G = nx.krackhardt_kite_graph()
# nx.draw_networkx(G)
# plt.show

#-----------------------------------------------------------------------------------------------------------#
