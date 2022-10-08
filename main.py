inputvalues = input('Enter all elements values: ').split()
numbers1 = list(map(int, inputvalues))
numbers2 = []
for i in range(0,len(numbers1)-1,2):
	numbers2.append(i)
	numbers1.pop(i)