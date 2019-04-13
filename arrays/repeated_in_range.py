# Taken from: https://www.youtube.com/watch?v=GeHOlt_QYz8

# we know that 1<= x <= length array
# all positive integers
def duplicates(array):
	duplicates = set()
	for i in (array):
		if array[abs(i)-1] < 0:
			duplicates.add(abs(i))
		else:
			array[abs(i)-1] *= -1

	for i in range(len(array)):
		array[i] = abs(array[i])

	return duplicates

array = [2, 3, 2, 4, 2, 4, 5, 1, 6, 3]
print('duplicates for array: ', array, ' are: ', duplicates(array)) 
