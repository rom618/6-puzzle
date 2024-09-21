from random import choice
import time

# counts the number of nodes created from using expand()
number_of_nodes = 0

# Program stop after this many unique states have been traversed
MAX_MEMORY = 1000

# we define a node class where state is the 6-puzzle state,
# index is the position of the blank square
# node_id is the unique id corresponding to the puzzle state (this helps to check if we already visited a node)
# and prev_node is the pointer to the previous node in the tree
class Node:
    def __init__(self, state, index, prev_node=None):
        self.state=state
        self.index=index
        self.node_id=f"{state[0]}{state[1]}{state[2]}{state[3]}{state[4]}{state[5]}"
        self.prev_node=prev_node

    # set the previous node to the parent node
    def set_prev_node(self, prev_node):
        self.prev_node=prev_node

    # set or change the index position of the blank square
    def set_index(self,index):
        self.index=index

    def set_node_id(self):
        self.node_id=f"{self.state[0]}{self.state[1]}{self.state[2]}{self.state[3]}{self.state[4]}{self.state[5]}"

    # print out the 6-puzzle state of the node
    def __str__(self):
        return f"[{self.state[0]} {self.state[1]} {self.state[2]}]\n[{self.state[3]} {self.state[4]} {self.state[5]}]"

# Returns the children of the given node after moving the blank square up, down, right or left
# the list of children returned is ordered by moving the lower-numbered piece first
def expand(node):

    global number_of_nodes

    children=[] #store the children nodes here
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

        children.append(child)

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


        children.append(child)

        number_of_nodes+=1

    #expand right
    if i%3!=2:
        temp=[]
        for j in node.state:
            temp.append(j)
        child = Node(temp, node.index, node)
        child.state[i]=child.state[i+1]
        child.state[i+1]=0
        child.set_index(i+1)
        child.set_node_id()

        children.append(child)

        number_of_nodes+=1

    #expand left
    if i%3!=0:
        temp=[]
        for j in node.state:
            temp.append(j)
        child = Node(temp, node.index, node)
        child.state[i]=child.state[i-1]
        child.state[i-1]=0
        child.set_index(i-1)
        child.set_node_id()

        children.append(child)

        number_of_nodes+=1

    # order the children by lowest-numbered moved piece '

    children.sort(key=lambda child: child.state[node.index])

    return children

# simple node object for queue
class QueueNode:

    def __init__(self, item = None):
        self.item = item
        self.next = None
        self.previous = None

# Queue class. uses QueueNode object to store objects in the queue
class Queue:

    def __init__(self):
        self.length = 0
        self.head = None
        self.tail = None

    def peek_first(self):
        return self.head.item
    
    def peek_last(self):
        return self.tail.item

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
            self.head = self.tail = new_data
        else:
            self.head.previous=new_data
            new_data.next=self.head
            self.head=new_data
        self.length+=1
    
    # print out queue
    def __str__(self):
        # if queue is empty, return nothing
        if self.length==0:
            return ""
        
        # if queue has more than one element, concatenate the each element to a string
        if self.length!=1:
            temp_node=self.head
            string =f"Queue: \n{temp_node.item}"
            for i in range(self.length-1):
                temp_node=temp_node.next
                if temp_node is not None:
                    temp_string=f"\n\n{temp_node.item}"
                    string=string+temp_string
            return string+"\n"
        
        # if queue only has one element, return head item
        else:
            return f"Queue: \n{self.head.item}\n"

# traces back the path from a node to the root
def trace_node_path(node):
    if node==0:
        return 0
    temp=node
    string=f"{temp}\n\n"
    while temp.prev_node is not None:
        temp=temp.prev_node
        string=f"{temp}\n\n"+string
    return "Path to goal: \n"+string

# finds the depth of a node in the tree
def depth(node):
    temp=node
    i=0
    while temp.prev_node is not None:
        i+=1
        temp=temp.prev_node
    return i

# creates a random 6-puzzle
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
    print("Breadth first search: \n")
    nodes_traversed=set()
    queue = Queue()
    queue.enqueue(initial_state)
    nodes_traversed.add(initial_state.node_id)

    while len(nodes_traversed)!=MAX_MEMORY:
        
        if queue.length==0:
            print(f"solution not found. nodes created: {number_of_nodes}\n")
            return 0
        
        if queue.peek_last().node_id=="012543":
            print(f"found after creating {number_of_nodes} nodes\n")
            return queue.peek_last()
        
        for j in expand(queue.dequeue()):
            if j.node_id not in nodes_traversed:
                queue.enqueue(j)
                nodes_traversed.add(j.node_id)

    print(f"program timed out after creating {number_of_nodes} nodes\n")
    print(nodes_traversed)
    return 0

# depth first search
def dfs(initial_state):
    print("Depth first search: \n")
    nodes_traversed=set()
    queue = Queue()
    queue.enqueue_front(initial_state)
    nodes_traversed.add(initial_state.node_id)

    while len(nodes_traversed)!=MAX_MEMORY:

        if queue.length==0:
            print(f"solution not found. nodes created: {number_of_nodes}\n")
            return 0
        
        if queue.peek_first().node_id=="012543":
            print(f"found after creating {number_of_nodes} nodes\n")
            return queue.peek_first()
        
        for j in expand(queue.dequeue()):
            if j.node_id not in nodes_traversed:
                queue.enqueue_front(j)
                nodes_traversed.add(j.node_id)

    print(f"program timed out after creating {number_of_nodes} nodes\n")
    print(nodes_traversed)
    return 0

# iterative deepening search
def ids(initial_state):
    print("Iterative Deepening search: \n")
    nodes_traversed={}
    queue = Queue()
    queue.enqueue_front(initial_state)
    nodes_traversed.add(initial_state.node_id)

    while len(nodes_traversed)!=MAX_MEMORY:

        if queue.length==0:
            print(f"solution not found. nodes created: {number_of_nodes}\n")
            return 0
        
        if queue.peek_first().node_id=="012543":
            print(f"found after creating {number_of_nodes} nodes\n")
            return queue.peek_first()
        
        for j in expand(queue.dequeue()):
            if j.node_id not in nodes_traversed:
                queue.enqueue_front(j)
                nodes_traversed.add(j.node_id)
                
    print(f"program timed out after creating {number_of_nodes} nodes\n")
    print(nodes_traversed)
    return 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #temp_state=random_6_puzzle()
    temp_state=[3,1,5,4,2,0]
    root = Node(temp_state,find_zero(temp_state))
    print(f"start state: \n{root}\n")

    # BFS
    start = time.perf_counter()
    print(trace_node_path(bfs(root)))
    end = time.perf_counter() - start
    print('{:.6f}s for the calculation\n'.format(end))

    # DFS
    start = time.perf_counter()
    print(trace_node_path(dfs(root)))
    end = time.perf_counter() - start
    print('{:.6f}s for the calculation\n'.format(end))

    # IDS
    start = time.perf_counter()
    trace_node_path(ids(root))
    end = time.perf_counter() - start
    print('{:.6f}s for the calculation\n'.format(end))
