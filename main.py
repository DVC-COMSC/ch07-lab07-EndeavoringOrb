import math

inputvalues = input('Enter all elements values: ').split()
numbers1 = list(map(int, inputvalues))
numbers2 = []
for i in range(0,len(numbers1),2):
	numbers2.append(numbers1[i])
for i in range(math.floor((len(numbers1)+1)/2)):
	numbers1.pop(i)
print(numbers1)
print(numbers2)
#(1),2,3,4,5,6,7,8,9,10
#2,(3),4,5,6,7,8,9,10
#2,4,(5),6,7,8,9,10
#2,4,6,(7),8,9,10