#!/usr/bin/env python3

# twosum([4, 5, 1, 8], 6)
# twosum([3, 5, 2, -4, 8, 11], 7)

def twosum(nums, sum):
    table = {}
    pairs = []

	
    for i in nums:
        if sum - i in table:
            pairs.append((i, sum - i))
        table[i] = i
        
    return pairs
 
    
def main():
    print(twosum([3, 5, 2, -4, 8, 11], 7))


if "__name__" == __main__:
	main()