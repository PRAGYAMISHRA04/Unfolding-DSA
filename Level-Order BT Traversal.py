import sys

class Node:
    def __init__(self,data):
        self.right=self.left=None
        self.data = data
class Solution:
    def insert(self,root,data):
        if root==None:
            return Node(data)
        else:
            if data<=root.data:
                cur=self.insert(root.left,data)
                root.left=cur
            else:
                cur=self.insert(root.right,data)
                root.right=cur
        return root
    def levelOrder(self,root):
        if root:
            k=0;l=0;
            print(root.data,end=" ")
            if root.left :
                print(root.left.data,end=" ")
                k=1
            if root.right:    
                print(root.right.data,end=" ")
                l=1 
            if k==1:      
                self.levelOrder(root.left.left)
                self.levelOrder(root.left.right)
            if l==1:
                self.levelOrder(root.right.left)
                self.levelOrder(root.right.right) 
                   #Write your code here
print(" ### Welocme To Level-Order world ###\n !!!! Enter the no. of digits to order !!!!  ")
T=int(input())
myTree=Solution()
root=None
print("Enter the digits to put them in Level- Order Traversal of BST :) ")
for i in range(T):
    data=int(input())
    root=myTree.insert(root,data)
myTree.levelOrder(root)
''' 9
20
50
35
44
9
15
62
11
13
'''
''' 20 9 50 15 35 62 11 44 13'''
