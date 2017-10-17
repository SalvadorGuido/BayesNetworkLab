
class Node(object):
    def __init__(self):
        self.name = None
        self.parents = None
        self.prob = None

def createNodes(nodes,network):
    for item in nodes:
        node = Node()
        node.name = item
        node.parents = []
        node.prob = {}
        network.append(node)

# def assignProb(network):
#     for item in network:



bnetwork = []
p = []
q = []
n = list(input().split(','))

for i in range(0, int(input()),1):
    p.append(input())
for i in range(0, int(input()), 1):
    q.append(input())

print(n)
print(p)
print(q)

createNodes(n,bnetwork)
for item in bnetwork:
    print(item.name)