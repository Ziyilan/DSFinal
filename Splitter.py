class Splitter():
	def split(self, dataset, feature):
		from Criterion import Criterion
		c = Criterion()
		dataset = dataset.sort_values(feature)
		best_split = 0
		best_split_impurity = c.gini_impurity(dataset, feature)
		orig_impurity = best_split_impurity
		for i in xrange(1,len(dataset)):
			current_split_impurity = c.gini_impurity(dataset[i:], feature)+c.gini_impurity(dataset[:i], feature)
			if current_split_impurity<best_split_impurity:
				best_split = i
				best_split_impurity = current_split_impurity
		return best_split, best_split_impurity, orig_impurity

# if __name__ == "__main__":
# 	import pandas as pd
# 	s = Splitter()
# 	data = pd.DataFrame({'c1':[1,1,3,2],'c2':[2,3,2,2],'p':[1,1,0,0]})
# 	for each in data.columns:
# 		bs, bi, oi = s.split(data, each)
# 		d = list(data.sort_values(each)[each])
# 		print d
# 		print "Split on '" + each + "' at index " + str(bs) + " between " + str(d[bs-1]) + " and " + str(d[bs]) + " for new impurity " + str(bi)