class tree:
	__slots__ = ['val', 'left', 'right']
	def __init__(self, val):
		self.val = val
		self.left = None
		self.right = None

class node:
	def __init__(self, val):
		self.val = val
		self.pre = None
		self.next = None
	
def getNodeNumRec(root):
	if root is None:
		return 0
	return getNodeNumRec(root.left) + getNodeNumRec(root.rgiht) + 1
	
	
def getNodeNum(root):
	res = 0
	stack = []
	while root or stack:
		if root:
			res += 1
			stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			root = root.right
	return res
	
def getDepthRec(root):
	if root is None:
		return -1
	return max(getDepthRec(root.left), getDepthRec(root.right)) + 1
	
	
# lever traversal
def getDepth(root):
	if root is None:
		return 0
	flag = tree(0)
	queue, res = [root, flag], -1
	while queue:
		cur = queue.pop(0)
		if cur == flag:
			res += 1
			if queue:
				queue.append(flag)
		if cur.left:
			queue.append(cur.left)
		if cur.right:
			queue.append(cur.right)
	return res
	
	
def TraversalRec(root, res, oder):
	if root:
		if oder == 'pre':
			res.append(root.val)
		preorderTraversalRec(root.left, res)
		if oder == 'in':
			res.append(root.val)
		preorderTraversalRec(root.right, res)
		if oder == 'post':
			res.append(root.val)
		
def preorder_inorder_Traversal(root, oder)
	res, stack = [], []
	while stack or root:
		if root:
			if order == 'pre':
				res.append(root.val)
			stack = stack.append(root)
			root = root.left
		else:
			root = stack.pop()
			if oder == 'in':
				res.append(root.val)
			root = root.right
	return res
	
def postorderTraversal(root):
	res, stack, pre = [], [], None
	while stack or root:
		if root:
			stack.append(root)
			root = root.left
		elif stack[-1].right == pre:
			pre = stack.pop()
			res.append(pre.val)
		else:
			root = stack[-1].right
			pre = None
	return res
			

from collections import deque
def levelTraversal(root):
	if root is None:
		return []
	res , q = [root], deque()
	while q:
		cur = q.popleft()
		res.append(cur.val)
		if cur.left:
			q.append(cur.left)
		if cur.right:
			q.append(cur.right)
	return res

def levelTraversalRec(root):
	res = []
	def help(root, level):
		if root:
			if level == len(res):
				res.append([])
			else:
				res[level].append(root.val)
			help(root.left, level + 1)
			help(root.right, level + 1)
				
	help(root, 0)
	return res
	
#将二叉查找树变为有序的双向链表
def convertBST2DLLRec(root):
def convertBST2DLL(root):
	
	
	
	
	
	
	
	
	
	
	
	
	
#求二叉树第K层的节点数	
def getNodeNumKthLevelRec(root):
def getNodeNumKthLevel(root, k):
	if root is None:
		return 0
	dummy = tree(0)
	q , temp, level = [root, dummy] , 0, 0
	while q:
		cur = q.pop(0)
		if cur == dummy:
			if level == k:
				return temp
			else:
				temp = 0
				level += 1
			if q:
				q.append(dummy)
		else:
			temp += 1
		if cur.left: q.append(cur.left)
		if cur.right: q.append(cur.right)
	return temp
	
	
#求二叉树中叶子节点的个数
def getNodeNumLeafRec(root):
	if root is None:
		return 0
	if root.left is None and root.right is None:
		return 1
	return getNodeNumLeafRec(root.left) + getNodeNumLeftRec(root.right)

def getNodeNumLeaf(root):
	if root is None:
		return 0
	res , q = 0, [root]
	while q:
		cur = q.pop(0)
		if cur.left is None and cur.right is None:
			res += 1
		if cur.left: q.append(cur.left)
		if cur.right: q.append(cur.right)
	return res
		
	
def isSameRec(r1, r2):
		return (not r1 and not r2) or (r1 and r2 and r1.val == r2.val and isSameRec(r1.left, r2.left) and isSameRec(r1.right, r2.right))
		
def isSame(r1, r2):
	
	
	
	
	
	
	
	
def isAVLRec(root):
	def help(root):
		if not root:
			return 0
		left = help(root.left)
		right = help(root.right)
		if left == -1 or right == -1 or abs(left - right) > 1:
			return -1
		else:
			return max(left, right) + 1
	return help(root) != -1
	
	
def mirrorRec(root):
	if not root:
		return None
	res_root = tree(root.val)
	res_root.left = mirrorRec(root.right)
	res_root.right = mirrorRec(root.left)
	return res_root

def mirror(root):








def mirrorCopyRec(root):
	if root:
		mirrorCopyRec(root.left)
		mirrorCopyRec(root.right)
		temp = tree(0)
		temp = root.left
		root.left = root.right
		root.right = temp
		
def mirrorCopy(root):
	
	
	
	
	
	
	

def isMirrorRec(r1, r2):
	return (not r1 and not r2) or (r1 and r2 and r1.val == r2.val and isMirrorRec(r1.left, r2.right) and isMirror(r1.right, r2.left))
	
def isMirror(r1, r2):
	
	
	
	
	
	
	
	
	

def LCA(root, r1 , r2):
	targets = set([r1, r2])
	lca , stack, min_depth = None, [], -1
	while root or stack:
		if root:
			if root in targets:
				targets.remove(root)
			if min_depth < 0:
				lca = root
				min_depth = len(stack)
			if not targets:
				break
			stack.append(root)
			root = root.left
		else:
			root = s.pop()
			if mindepth > len(stack):
				lca = root
				mindepth = len(stack)
			root = root.right
	return None if targets else lca
	
	
	
def LCABstRec(root, r1, r2):
	if root is None:
		return None
	if root.val > r1.val and root.val > r2.val:
		return LCABstRec(root.left, r1, r2)
	if root.val < r1.val and root.val < r2.val:
		return LCABstRec(root.right, r1, r2)
	return root
	
	
def LCARec(root, r1, r2):
	if root is None:
		return None
	if root.val == r1.val or root.val == r2.val:
		return root
	left = LCARec(root.left, r1, r2)
	right = LCARec(root.right, r1, r2)
	if not left:
		return right
	elif not right:
		return left
	else: return root
	

def getMaxDistanceRec(root):
	def help(root):
		if root is None:
			return 0, -1
		l1, h1 = getMaxDistanceRec(root.left)
		l2, h2 = getMaxDistanceRec(root.right)
		return max(l1, l2, h1 + h2 + 2), max(h1, h2) + 1
	return help(root)[0]
	
	
def isCompleteBinaryTreeRec(root):
	if root is None:
		return True
	if root.left and not root.right:
		return False
	if root.right and not root.left:
		return False
	return isCompleteBinaryTreeRec(root.left) and isCompleteBinaryTreeRec(root.right)
	
def isCompleteBinaryTree(root):
	if root is None:
		return True
	q = [root]
	while q:
		cur = q.pop(0)
		if (not cur.left) ^ (not cur.right):
			return False
		if cur.left: q.append(cur.left)
		if cur.right: q.append(cur.right)
	return True
	
	
#找出二叉树中最长连续子串(即全部往左的连续节点，或是全部往右的连续节点）
def findLongest(root):
	