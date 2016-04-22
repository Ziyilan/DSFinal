class RandomForestRegressor():
	def __init__(self, train_data, predict_on, n_trees=20, max_depth=5):
		self.train_data = train_data
		self.n_trees = n_trees
		self.max_depth = max_depth
		self.trees = []
		self.predict_on = predict_on
		self.criterion = Criterion()
		b = Builder()
		for n in xrange(n_trees):
			self.trees.append(b.build(train_data, predict_on, max_depth))

	def predict(self, test_data):
		def pt_prediction(node, data):
			if node.value:
				return node.value
			else:
				train_data = self.train_data.sort(node.feature)[node.feature]
				split_value = train_data[split_index]
				if datapoint[node.feature] < split_value:
					return pt_prediction(node.left_child, data)
				else:
					return pt_prediction(node.right_child, data)

		predictions = []
		for datapoint in test_data:
			pt_predictions = []
			for root in self.trees:
				pt_predictions.append(pt_prediction(root), datapoint)
			predictions.append(max(set(pt_predictions), key=pt_predictions.count))
		return pd.DataFrame(predictions)