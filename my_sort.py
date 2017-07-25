
def sort_list(a_list):
	"""
	Input -> a list of ints
	Returns a sorted list (low to high)
	"""
	for pass_num in range(len(a_list) -1, 0, -1):
		for i in range(pass_num):
			if a_list[i] > a_list[i+1]:
				temp = a_list[i]
				a_list[i] = a_list[i+1]
				a_list[i+1] = temp

def even_list(a_list):
	return [x for x in a_list if (x%2==0)]

def odd_list(a_list):
	return [x for x in a_list if (x%2==1)]

def my_sort(a_list):
	"""
	Input -> a list of integers.
	output -> sorted list. Odd nums first, then even
	"""
	sorted_list = []
	sort_list(a_list)

	return odd_list(a_list) + even_list(a_list)



#a = [1,2,3,4,5,6,7,8,9,10]
#b = [1,2]
#c = [90,45,66]

#print(my_sort(a))
#print(my_sort(b))
#print(my_sort(c))