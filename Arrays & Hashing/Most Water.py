height = [1,8,6,2,5,4,8,3,7]

# brute force solution
# Take every two cobination of numbers, calculate the water and return the most water.

'''
1,8  
1,6
.
.
.
1,7

> Do the same with other combination of heights 
'''
heights = [1,8,6,2,5,4,8,3,7]

def mostWater(heights):

    mostVolume = 0

    for height in range(len(heights)):
        for height2 in range(height+1,len(heights)):
            area = (height2 - height) * min(heights[height],heights[height2])
            mostVolume = max(mostVolume,area)

    return mostVolume

heights = [1,8,6,2,5,4,8,3,7]
print(f'Brute force solution outcome: {mostWater(heights)}')

# Optimal Solution

'''
Approach is to use two pointers.
l,r

if r>l
    l+1
elif l>r
    r-=1
    l+=1
'''

heights = [1,8,6,2,5,4,8,3,7]

def mostWater2(heights):

    outcome = 0

    l,r = 0, len(heights) -1

    while l < r:
        area = (r - l) * min(heights[r],heights[l])

        if heights[l] < heights[r]:
            l += 1
        elif heights[l] > heights[r]:
            r -= 1
        # Edge case: what if they are the same height?
        # Move to the longest height
        elif heights[l] == heights[r]:
            if heights[l+1] < heights[r-1]:
                r -= 1
            elif heights[l+1] > heights[r-1]:
                l += 1

        outcome = max(outcome,area)

    return outcome

print(f'Optimal Solution outcome: {mostWater2(heights)}')           

# Time: O(n)
# Space: (1)
