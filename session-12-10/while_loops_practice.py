
# 1. Use a while loop to print numbers 1-10:
i=1
while i<=10 and i>=1:
	print(i)
	i+=1
# 2. Use a while loop to print the first 10 multiples of 24:
i=1
while i<=10:
	print(i*24)
	i+=1
# 3. Use a while loop to find the average of these numbers:
<<<<<<< HEAD
numbers = [10,42,-2,900,5,8,39]
i=0
sum_1=0
while i<len(numbers):
	sum_1+=numbers[i]
	i+=1
print(sum_1/len(numbers))
=======
numbers = [10,42,-2, 900,5,8,39]
print(numbers[1])
i = 0
total = 0

while i < len(numbers):
	total += numbers[i]
	i+=1

print(total)
average = total/len(numbers)

print(average)
>>>>>>> ae2a66d07524f15dcce27fbe52b54d85ec246ec5
