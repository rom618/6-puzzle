from random import choice

number_of_nodes = 0

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

    # set or change the index position of the blank square
    def set_index(self,index):
        self.index=index

    def set_node_id(self):
        self.node_id=3*self.state[0]+5*self.state[1]+7*self.state[2]+11*self.state[3]+13*self.state[4]+17*self.state[5]

    # print out the 6-puzzle state of the node
    def __str__(self):
        return f"[{self.state[0]} {self.state[1]} {self.state[2]}]\n[{self.state[3]} {self.state[4]} {self.state[5]}]"

def expand(node):

    global number_of_nodes

    list=[] #store the children nodes here
    i=node.index

    #expand up
    if i>=3:
        temp=[]
        for j in node.state:
            temp.append(j)
        child = Node(temp, node.index, node)
        child.state[i]=child.state[i-3]
        child.state[i-3]=0
        child.set_index(i-3)
        child.set_node_id()

        list.append(child)

        number_of_nodes+=1

    #expand down
    if i<=2:
        temp=[]
        for j in node.state:
            temp.append(j)
        child = Node(temp, node.index, node)
        child.state[i]=child.state[i+3]
        child.state[i+3]=0
        child.set_index(i+3)
        child.set_node_id()


        list.append(child)

        number_of_nodes+=1

    #expand left
    if i%3==2:
        temp=[]
        for j in node.state:
            temp.append(j)
        child = Node(temp, node.index, node)
        child.state[i]=child.state[i-1]
        child.state[i-1]=0
        child.set_index(i-1)
        child.set_node_id()

        list.append(child)

        number_of_nodes+=1

    #expand right
    if i%3==0:
        temp=[]
        for j in node.state:
            temp.append(j)
        child = Node(temp, node.index, node)
        child.state[i]=child.state[i+1]
        child.state[i+1]=0
        child.set_index(i+1)
        child.set_node_id()

        list.append(child)

        number_of_nodes+=1

    return list



class QueueNode:

    def __init__(self, item = None):
        self.item = item
        self.next = None
        self.previous = None



class Queue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def peek(self):
        return self.head.item

    def enqueue(self, value):
        newNode = QueueNode(value)
        if self.head is None:
            self.head = self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.previous = self.tail
            self.tail = newNode
        self.length += 1

    def dequeue(self):
        item = self.head.item
        self.head = self.head.next 
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return item

    def enqueue_front(self,data):
        new_data=QueueNode(data)
        if self.head is None:
            self.head=new_data
            self.tail=self.head
        else:
            self.head.previous=new_data
            new_data.next=self.head
            self.head=new_data

def random_6_puzzle():

    digits=[0,1,2,3,4,5]
    puzzle = []

    for i in range(6):
        puzzle.append(choice(digits))
        digits.remove(puzzle[i])
    return puzzle

def find_zero(list):
    for i in range(len(list)):
        if list[i]==0:
            return i

# breadth first search
def bfs(initial_state):
    nodes_traversed=[]
    queue = Queue()
    queue.enqueue(initial_state)
    nodes_traversed.append(initial_state.node_id)
    while len(nodes_traversed)!=100:
        if queue.length==0:
            print(f"solution not found. nodes created: {number_of_nodes}")
            print(nodes_traversed)
            return 0
        if queue.peek().state==[0,1,2,5,4,3]:
            print(f"found after creating {number_of_nodes} nodes")
            print(nodes_traversed)
            print(queue.peek())
            return 1
        for j in expand(queue.dequeue()):
            if not j.node_id in nodes_traversed:
                queue.enqueue(j)
                nodes_traversed.append(j.node_id)
                print(f"{j}\n")
    print(f"program timed out after creating {number_of_nodes} nodes")
    print(nodes_traversed)
    return

# depth first search
def dfs():
    return

# iterative deepening search
def ids():
    return

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    temp_state=random_6_puzzle()
    root = Node(temp_state,find_zero(temp_state))
    print(f"\n{root}\n")
    bfs(root)

