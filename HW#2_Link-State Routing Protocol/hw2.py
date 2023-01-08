'''
無討論同學
'''
import sys
import os

weights = []  # router weights
node_number = -1    # number of routers


# read weights
with open(sys.argv[1], 'r') as f:
    node_number = int(f.readline())
    for i in range(node_number):
        line = f.readline().replace('\n', '')
        link = line.split(' ')
        link = list(map(int, link))
        weights.append(link)


def Dijkstra(N, W, source_node: int):    # number of nodes, weights, source node (0 ~ N-1)
    s = source_node-1  # source node

    # initialization
    D = [-1]*N  # current estimate of cost
    predecessor = [-2]*N  # predecessor node along path from source to v
    D[s] = 0
    predecessor[s] = s

    # Dijkstra
    explored = []  # explored nodes

    while len(explored) < N:
        # extract min
        min_node = 0
        while (min_node < N) and (min_node in explored or D[min_node] == -1):
            min_node += 1
        if min_node == N:  # check whether complete earlier
            break
        for i in range(N):
            if i not in explored and (D[i] < D[min_node] and D[i] != -1):
                min_node = i
        explored.append(min_node)

        # update estimated cost of adjacent nodes
        for v in range(N):
            # unexplored adjacent nodes of min node
            if v not in explored and W[min_node][v] != -1:
                if (D[v] == -1) or (D[v] > D[min_node]+W[min_node][v]):
                    D[v] = D[min_node]+W[min_node][v]
                    predecessor[v] = min_node

    # traceback
    traceback = predecessor

    for i in range(len(explored)):
        while W[s][traceback[explored[i]]] == -1:   # not adjacent node of source
            traceback[explored[i]] = predecessor[traceback[explored[i]]]
        if W[s][traceback[explored[i]]] != -1 and traceback[explored[i]] == s:
            traceback[explored[i]] = explored[i]
        if traceback[traceback[explored[i]]] != traceback[explored[i]]:
            traceback[explored[i]] = traceback[traceback[explored[i]]]
    for t in range(N):
        traceback[t] += 1

    return D, traceback


# write output file
if len(sys.argv) < 3:
    # part1
    output_filename1 = os.path.splitext(sys.argv[1])[0]+'_GenTable.txt'
    with open(output_filename1, 'w', newline='\n') as f:
        for i in range(node_number):
            distance, next_hop = Dijkstra(node_number, weights, i+1)
            f.write(f'Routing table of router {i+1}:\n')
            for v in range(node_number):
                f.write(f'{distance[v]} {next_hop[v]}\n')
else:
    # part2
    rm = int(sys.argv[2])  # node to be removed

    # revise weight matrix
    for i in range(node_number):
        weights[rm-1][i] = -1
        weights[i][rm-1] = -1

    output_filename2 = os.path.splitext(
        sys.argv[1])[0]+'_RmRouter'+sys.argv[2]+'.txt'
    with open(output_filename2, 'w', newline='\n') as f:
        for i in range(node_number):
            if (i+1) != int(sys.argv[2]):
                distance, next_hop = Dijkstra(node_number, weights, i+1)
                f.write(f'Routing table of router {i+1}:\n')
                for v in range(node_number):
                    f.write(f'{distance[v]} {next_hop[v]}\n')
