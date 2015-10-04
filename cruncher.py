from collections import defaultdict

def cruncher (seed):

	init_arr = map(int, list(str(seed)))

	new_seed = count_digits(init_arr)

	if new_seed != seed:
		print new_seed
		cruncher(new_seed)
	else:
		print "Final number: " + str(new_seed)

def count_digits(arr): 
	my_dict = defaultdict(lambda: 0) # sets dict default value

	for x in arr:
		my_dict[x] += 1

	return assembler(dict(my_dict))

def assembler(dic):
	arr = []
	count = 0
	for x in dic:
		arr.append(dic[x])
		arr.append(dic.keys()[count]) # LOL WTF
		count += 1

	return int(''.join(map(str, arr))) 
	
