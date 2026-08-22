#Q-1. Invert Binary Tree
#TC-> O(n)  SC-> O(n)
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# def invertTree(root: TreeNode) -> TreeNode:
#     if not root:
#         return None

#     root.left, root.right = root.right, root.left
    
#     invertTree(root.left)
#     invertTree(root.right)
    
#     return root

# from collections import deque

# def printTree(root: TreeNode):
#     if not root:
#         print("Empty Tree")
#         return
    
#     queue = deque([root])
#     result = []
    
#     while queue:
#         node = queue.popleft()
#         if node:
#             result.append(node.val)
#             queue.append(node.left)
#             queue.append(node.right)
#         else:
#             result.append(None)
            
#     while result and result[-1] is None:
#         result.pop()
        
#     print(result)

# def createTree(arr: list) -> TreeNode:
#     if not arr:
#         return None
    
#     nodes = [TreeNode(val) if val is not None else None for val in arr]
#     kids = nodes[::-1]
#     root = kids.pop()
    
#     for node in nodes:
#         if node:
#             if kids: node.left = kids.pop()
#             if kids: node.right = kids.pop()
            
#     return root
# if __name__ == "__main__":
#     input_list = [4, 2, 7, 1, 3, 6, 9]
#     root = createTree(input_list)
#     inverted_root = invertTree(root)
#     printTree(inverted_root)