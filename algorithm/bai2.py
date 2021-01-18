x = int(input("Nhap vao gia tri x: "))
y = int(input("Nhap vao gia tri y: "))
print()
res = [x]


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __str__(self):
        return "< data = {}, left = {}, right = {} >".format(self.data, self.left, self.right)

def hasPath(root, arr, x): 
      
    # if root is None there is no path  
    if (not root): 
        return False
      
    # push the node's value in 'arr'  
    arr.append(root.data)      
      
    # if it is the required node  
    # return true  
    if (root.data == x):      
        return True
      
    # else check whether the required node  
    # lies in the left subtree or right  
    # subtree of the current node  
    if (hasPath(root.left, arr, x) or 
        hasPath(root.right, arr, x)):  
        return True
      
    # required node does not lie either in  
    # the left or right subtree of the current  
    # node. Thus, remove current node's value   
    # from 'arr'and then return false      
    arr.pop(-1)  
    return False
  
# function to print the path from root to  
# the given node if the node lies in 
# the binary tree  
def printPath(root, x): 
      
    # vector to store the path  
    arr = []  
      
    # if required node 'x' is present  
    # then print the path  
    if (hasPath(root, arr, x)): 
        for i in range(len(arr) - 1): 
            print(arr[i], end = "->")  
        print(arr[len(arr) - 1]) 
      
    # 'x' is not present in the  
    # binary tree  
    else: 
        print("No Path") 
    return arr

n1 = Node(x)
n1.left = Node(n1.data - 1)
n1.right = Node(n1.data * 2)

n = n1
queue = []

while True:
    queue.append(n.left)
    queue.append(n.right)

    n = queue.pop(0)
    if n.left is None:
        n.left = Node(n.data - 1)
        n.right = Node(n.data * 2)
    if n.data == y:
        arr = printPath(n1, n.data)
        break

res_str = '{}'.format(arr[0])
for i in range(1, len(arr)):
    if arr[i] == arr[i - 1] - 1:
        res_str += '- 1'
    else:
        res_str = '2 * ({})'.format(res_str)

print('{} = {}'.format(res_str,eval(res_str)))