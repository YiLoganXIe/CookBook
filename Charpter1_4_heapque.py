# Created By Yi Xie 6/26/2019
# Example on Python CookBook

import heapq

nums = [1, 8 , 56, 78, 23, 9, 44, 233, 89]
print(heapq.nlargest(3, nums))		
print(heapq.nsmallest(3, nums))
print((heapq.nlargest(1, nums))[0]) # get the largest number
print("---------------------------------------")
#TODO:What is Labmda?

# how it works?
heap = list(nums)
heapq.heapify(heap)
print(heap)	# it is will form a heap tree
# The first element is always the smallest
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
print(heapq.heappop(heap))
# pop the smallest one and perculate up the current smallest element
print("----------------------------------------")
# However, the best way to find the smallest and the maximun number is using min() max()
# Also sorted() works will if N is not too large 
print(min(nums))
print(max(nums))
print(sorted(nums)[:5])
print(sorted(nums))
print(sorted(nums)[-5:])




