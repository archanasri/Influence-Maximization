from __future__ import division
from collections import defaultdict
from itertools import combinations
import sys
import random
import math
import matplotlib.pyplot as plt

Data = tuple(open(sys.argv[1], "r"))

SpreadTracker = defaultdict(list)
ParentGraph = []

def Graph(MaxNode):
    GraphGenerated = defaultdict(list)
    Queue = []
    QueueTracker = defaultdict(list)
    for i in range(MaxNode):
        i = i + 1
        for j in range(MaxNode):
            j = j + 1
            if j != i:
                x = random.uniform(0,1)
                y = random.uniform(0,1)
                if x > y:
                    GraphGenerated[str(i) + ':' + str(j)] = 0
    RandomNode = random.randint(0,MaxNode)
    Queue.append(str(RandomNode))
    QueueTracker[str(RandomNode)] = 'T'
    while (len(Queue) > 0):
        Node = Queue[0]
        Queue.remove(Node)
        for Element in GraphGenerated:
            ElementSub = Element.split(':')
            if Node == ElementSub[0]:
                if Element in ParentGraph:
                    GraphGenerated[Element] = 1
                    if ElementSub[1] not in QueueTracker:
                        Queue.append(ElementSub[1])
                        QueueTracker[ElementSub[1]] = 'T'
    Count = 0
    for val in GraphGenerated:
        if GraphGenerated[val] == 1:
            Count = Count + 1
    return RandomNode, Count/len(GraphGenerated)

def main():
    x = []
    y = []
    MaxNode = 0
    for i in range(len(Data)):
        line = Data[i]
        line = line.split()
        if line != []:
            if int(line[0]) > MaxNode:
                MaxNode = int(line[0])
            ParentGraph.append(line[0] + ':' + line[1])
    NumberOfGraphs = 15
    for k in range(NumberOfGraphs):
        print k
        Node, Spread = Graph(MaxNode)
        SpreadTracker[Node] = Spread
    for k in range(15):
        P = k + 1
        Comb = combinations(SpreadTracker.keys(), P)
        Count = 0
        for i in list(Comb):
            Sum = 0.0
            for j in i:
                Sum = Sum + SpreadTracker[j]
            Count = Count + 1
        print k, P, Sum
        x.append(P)
        y.append(Sum/(NumberOfGraphs/2.0))
    plt.plot(x,y)
    plt.show()

if __name__ == "__main__":
    main()
