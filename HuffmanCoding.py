import os
import json
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
reverseDict = {}


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
        reverseDict[newVal] = node.symbol


def getEncodedText(originalText):
    encodedText = ""
    for i in originalText:
        encodedText = encodedText+dict[i]
    return encodedText


def getPaddedEncodedText(encodedText):
    extra_padding = 8 - len(encodedText) % 8
    for i in range(0, extra_padding):
        encodedText += "0"
    padded_info = "{0:08b}".format(extra_padding)
    encodedText = padded_info + encodedText
    return encodedText


def getByteArray(paddedEncodedText):
    if(len(paddedEncodedText) % 8 != 0):
        print("Encoded text not padded properly")
        exit(0)

    b = bytearray()
    for i in range(0, len(paddedEncodedText), 8):
        byte = paddedEncodedText[i:i+8]
        b.append(int(byte, 2))
    return b

def encode(originalText,fileLocation):
    freq = {}
    originalText=originalText.rstrip()
    for i in originalText:
        freq[i] = 0
    for i in originalText:
        freq[i] = freq[i] + 1
    generateHuffmanCodes(freq)
    encodedText=getEncodedText(originalText)
    paddedEncodedText=getPaddedEncodedText(encodedText)
    b= getByteArray(paddedEncodedText)
    f=open(fileLocation+".bin",'wb')
    f.write(bytes(b))
    f.close()
    f=open(fileLocation+"Codes.txt",'w')
    f.write(json.dumps(reverseDict))
    f.close()
    print("compressed")

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

def remove_padding(padded_encoded_text):
    padded_info = padded_encoded_text[:8]
    extra_padding = int(padded_info, 2)
    padded_encoded_text = padded_encoded_text[8:] 
    encoded_text = padded_encoded_text[:-1*extra_padding]
    return encoded_text

def decode_text(encoded_text,file):
    current_code = ""
    decoded_text = ""
    fileLocation, file_extension = os.path.splitext(file)
    f=open(fileLocation+"Codes.txt",'r')
    codes=f.read()
    print(codes)
    reverse_mapping=json.loads(codes)
    for bit in encoded_text:
        current_code += bit
        if(current_code in reverse_mapping):
            character = reverse_mapping[current_code]
            decoded_text += character
            current_code = ""

    return decoded_text


def decode(file):
    with open(file, 'rb') as f:
        bit_string = ""
        byte = f.read(1)
        while(len(byte) > 0):
            byte = ord(byte)
            bits = bin(byte)[2:].rjust(8, '0')
            bit_string += bits
            byte = f.read(1)
        f.close()
        encoded_text = remove_padding(bit_string)
        decompressed_text = decode_text(encoded_text,file)
        print("decoded from huffmann")
        return decompressed_text