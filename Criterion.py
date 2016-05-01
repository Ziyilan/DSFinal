class Criterion():
	def gini_impurity(self, dataset, feature):
		total = len(dataset[feature])
		counts = {}
		for datapoint in dataset[feature]:
			counts.setdefault(datapoint, 0)
			counts[datapoint] += 1
		impurity = 0
		for j in dataset[feature].unique():
			f1 = float(counts[j])/total
			for k in dataset[feature].unique():
				if j!=k:
					f2 = float(counts[k])/total
					impurity += f1*f2
		return impurity

if __name__ == "__main__":
	import pandas as pd
	c = Criterion()
	data = pd.DataFrame({'c1':[1,1,3,2],'c2':[2,3,2,2],'p':[1,1,0,0]})
	for each in data.columns:
		print 'impurity for ' + each + ': ' + str(c.gini_impurity(data, each))