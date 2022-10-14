def find_smallest_interval(numbers) :
 numbers.sort()
 return numbers[1]-numbers[0]





numbers=[12,3,4,89,23,7]

print(find_smallest_interval(numbers))