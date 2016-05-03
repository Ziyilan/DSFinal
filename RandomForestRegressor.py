class RandomForestRegressor():
	def __init__(self, train_data, predict_on, n_trees=20, max_depth=5, predictors=None):
		from Builder import Builder
		self.train_data = train_data
		self.n_trees = n_trees
		self.max_depth = max_depth
		self.predict_on = predict_on
		self.trees = []
		self.avg = sum(train_data[predict_on])/float(len(train_data))
		b = Builder()
		for n in xrange(n_trees):
			print "starting tree " + str(n+1)
			self.trees.append(b.build(train_data, predict_on, max_depth, predictors))
			print "finished tree " + str(n+1)

	def predict(self, test_data):
		import pandas
		def pt_prediction(node, data, dataset=self.train_data):
			if node.value!=None:
				return node.value
			else:
				dataset = dataset.sort_values(node.feature)
				split_value = dataset[node.feature].iloc[node.split_index]
				if data[node.feature] < split_value:
					return pt_prediction(node.left_child, data, dataset[:node.split_index])
				else:
					return pt_prediction(node.right_child, data, dataset[node.split_index:])

		predictions = []
		# indices = []
		for index, datapoint in test_data.iterrows():
			# indices.append(index)
			pt_predictions = []
			for root in self.trees:
				pt_predictions.append(pt_prediction(root, datapoint))
			pred = sum(pt_predictions)/(len(pt_predictions))
			predictions.append(pred)#max(set(pt_predictions), key=pt_predictions.count))
		return pandas.Series(predictions)