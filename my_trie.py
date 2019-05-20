import argparse

class Trie(object):
    def __init__(self, char):
        self.children = []
        self.char = char
        self.count = 1
        self.char_is_end = False

def add(root, word):
    word = word.lower()
    node = root
    for char in word:
        children_found = False
        for children in node.children:
            if char == children.char:
                children.count += 1
                children_found = True
                node = children
                break

        if not children_found:
            new_node = Trie(char)
            node.children.append(new_node)
            node = new_node

    node.char_is_end = True

def get(root, word):
    node = root
    for char in word:
        is_present = False
        for children in node.children:
            if children.char == char:
                node = children
                is_present = True
                break
        if not is_present:
            return "no suggestion"
    print_all(node, word)
    return ""

lis = []
def print_all(root, word):
    node = root
    count = 0
    if node.children:
        global lis
        for child in node.children:
            if count>=20:
                break
            lis.append(child.char)
            if child.char_is_end:
                print word+"".join(lis)
                count += 1
                lis = []
            print_all(child, word)

def define_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--file", help="Specify the file containing all the tokens", type=str)
    parser.add_argument("--prefix", help="specify the token whose prefix match is to be done", type=str)
    args = parser.parse_args()
    return args

if __name__=="__main__":
    root = Trie("*")
    args = define_args()
    f = open(args.file)
    for line in f:
        line = line.strip()
        add(root, line)

    res = get(root, args.prefix.lower())
    if res:
        print res
