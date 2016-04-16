class Builder():
	def __init__(self):

	def build(self, dataset, predict_on, max_depth=5):
		root = Node()
		s = Splitter()
		features = list(dataset.columns)
		features.remove(predict_on)
		feature = random.choice(features)
		split_index, split_impurity, orig_impurity = Splitter.split(dataset, feature)
		threshold = (1.0/len(dataset))
		root.threshold = threshold
		if (max_depth>0) and (split_index!=0) and ((orig_impurity-split_impurity)>threshold):
			root.feature = feature
			root.left_child = self.build(dataset[:split_index], max_depth-1)
			root.right_child = self.build(dataset[split_index:], max_depth-1)
		else:
			lst = list(dataset[predict_on])
			root.value = max(set(lst), key=lst.count)
			#either this or average over the list
			#in which case we would let the user decide their "pivot point"
		return root