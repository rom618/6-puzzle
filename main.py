# This is a sample Python script.

# Press Ctrl+F5 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def test():
    n1 = Node([1,2,3,4,5,0],5)
    print(n1)
    print(n1.node_id)
    return 0

# we define a node class where state is the 6-puzzle state,
# index is the position of the blank square
# node_id is the unique id corresponding to the puzzle state
# and prev_node is the pointer to the previous node in the puzzle
class Node:
    def __init__(self, state, index, prev_node=None):
        self.state=state
        self.index=index
        self.node_id=3*state[0]+5*state[1]+7*state[2]+11*state[3]+13*state[4]+17*state[5]
        self.prev_node=prev_node

    # set the previous node to the parent node
    def set_prev_node(self, prev_node):
        self.prev_node=prev_node

    # print out the 6-puzzle state of the node
    def __str__(self):
        return f"[{self.state[0]} {self.state[1]} {self.state[2]}]\n[{self.state[3]} {self.state[4]} {self.state[5]}]"



# breadth first search
def bfs():

    return

# depth first search
def dfs():
    return

# iterative deepening search
def ids():
    return
# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    test()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
