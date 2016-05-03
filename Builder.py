class Builder():
	def build(self, dataset, predict_on, max_depth=5, predictors=None, min_leaf_size=5):
		from Node import Node
		import random
		from Splitter import Splitter
		node = Node()
		s = Splitter()
		if predictors==None:
			features = list(dataset.columns)
			features.remove(predict_on)
		else:
			features = predictors
		feature = random.choice(features)
		split_index, split_impurity, orig_impurity = s.split(dataset, feature)
		threshold = (1.0/len(dataset))
		node.split_index = split_index
		if (max_depth>0) and (split_index!=0) and ((orig_impurity-split_impurity)>threshold):
			node.feature = feature
			node.left_child = self.build(dataset.sort_values(feature)[:split_index], predict_on, max_depth-1, predictors, min_leaf_size)
			node.right_child = self.build(dataset.sort_values(feature)[split_index:], predict_on, max_depth-1, predictors, min_leaf_size)
		else:
			lst = list(dataset[predict_on])
			node.value = sum(lst)/float(len(lst))#max(set(lst), key=lst.count)
			print node.value
		return node

# if __name__ == "__main__":
# 	import pandas as pd
# 	b = Builder()
# 	data = pd.DataFrame({'c1':[1,1,3,2],'c2':[2,3,2,2],'p':[1,1,0,0]})
# 	r = b.build(data, 'p')
# 	def print_node_message(n):
# 		if n.value!=None:
# 			print "Node " + str(n) + " has value " + str(n.value)
# 		else:
# 			print "Node is " + str(n)
# 			if n.left_child:
# 				print_node_message(n.left_child)
# 			else:
# 				print "ERROR: No left child for " + str(n)
# 			if n.right_child:
# 				print_node_message(n.right_child)
# 			else:
# 				print "ERROR: No right child for " + str(n)
# 	print_node_message(r)