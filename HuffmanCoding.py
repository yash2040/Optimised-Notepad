class node:
    def __init__(self, freq, symbol, left=None, right=None):
        # frequency of symbol
        self.freq = freq

        # symbol name (charecter)
        self.symbol = symbol

        # node left of current node
        self.left = left

        # node right of current node
        self.right = right

        # tree direction (0/1)
        self.huff = ''


# utility function to print huffman
# codes for all symbols in the newly
# created Huffman tree
dict = {}


def printNodes(node, val=''):
    # huffman code for current node
    newVal = val + str(node.huff)

    # if node is not an edge node
    # then traverse inside it
    if node.left is not None:
        printNodes(node.left, newVal)
    if node.right is not None:
        printNodes(node.right, newVal)

        # if node is edge node then
        # display its huffman code
    if node.left is None and node.right is None:
        dict[node.symbol] = newVal


# characters for huffman tree

def init(originalText):
    freq = {}
    for i in originalText:
        freq[i] = 0
    for i in originalText:
        freq[i] = freq[i] + 1
    return generateHuffmanCodes(freq)


# list containing unused nodes
global nodes


# converting ccharecters and frequencies
# into huffman tree nodes
def generateHuffmanCodes(freq):
    nodes = []
    for i in freq:
        nodes.append(node(freq[i], i))
    while len(nodes) > 1:
        # sort all the nodes in ascending order
        # based on theri frequency
        nodes = sorted(nodes, key=lambda x: x.freq)

        # pick 2 smallest nodes
        left = nodes[0]
        right = nodes[1]

        # assign directional value to these nodes
        left.huff = 0
        right.huff = 1

        # combine the 2 smallest nodes to create
        # new node as their parent
        newNode = node(left.freq + right.freq, left.symbol + right.symbol, left, right)

        # remove the 2 nodes and add their
        # parent as new node among others
        nodes.remove(left)
        nodes.remove(right)
        nodes.append(newNode)

    # Huffman Tree is ready!
    printNodes(nodes[0])
    return dict
