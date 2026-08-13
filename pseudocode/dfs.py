# eddy edmonds Vtech
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class TreeNode:
    def __init__(self,x):
        self.val = x
        self.left = None
        self.right = None

def dfs(node):
    if not node:
        return None
    print(node.val)
    dfs(node.left)
    dfs(node.right)