import itertools as it

def parse_results_from_statannot(statresult):
    d = {}
    for result in statresult[1]:
        key = tuple(sorted([result.box1, result.box2]))
        d[key] = (result.stat, result.pval)
    return d

def create_hue_pairs(order, hue_order):
	'''Creates all pairs of x and hue for statannot'''
	pairs = []
	for x in order:
	    for combo in it.combinations(hue_order,2):
	        pairs.append(((x, combo[0]), (x, combo[1])))
	return pairs
	       
def create_pairs(order):
	'''Creates all pairs of x for statannot'''
	return [x for x in it.combinations(order,r=2)]
