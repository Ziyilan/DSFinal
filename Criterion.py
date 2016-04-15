class Criterion():
	def gini_impurity(self, dataset, feature):
		total = len(dataset[feature])
		counts = {}
		for datapoint in dataset[feature]:
			counts.setdefault(datapoint, 0)
			counts[datapoint] += 1
		impurity = 0
		for j in dataset[feature]:
			f1 = float(counts[j])/total
			for k in dataset[feature]:
				if j!=k:
					f2 = float(counts[k])/total
					impurity += f1*f2
		return impurity