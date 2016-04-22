import Criterion
class Splitter():
	def split(self, dataset, feature):
		c = Criterion()
		dataset = dataset.sort(feature)
		best_split = 0
		best_split_impurity = c.gini_impurity(dataset, feature)
		orig_impurity = best_split_impurity
		for i in xrange(1,len(data)):
			current_split_impurity = c.gini_impurity(dataset[i:], feature)+c.gini_impurity(dataset[:i], feature)
			if current_split_impurity<best_split_impurity:
				best_split = i
				best_split_impurity = current_split_impurity
		return best_split, best_split_impurity, orig_impurity