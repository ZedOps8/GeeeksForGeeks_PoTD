class Solution:
    def topK(self, nums, k): 
        um = {} # create an empty dictionary to store the count of each number
        n = len(nums) # get the length of the input array
        for i in range(n): # iterate through the array
            if nums[i] in um: # if the number is already in the dictionary
                um[nums[i]] += 1 # increment its count by 1
            else: # if the number is not in the dictionary
                um[nums[i]] = 1 # add it to the dictionary with a count of 1
        a = [0] * (len(um)) # create a new array with length equal to the number of unique numbers
        j = 0 # initialize a counter
        for i in um: # iterate through the dictionary
            a[j] = [i, um[i]] # store the number and its count in the new array
            j += 1 # increment the counter
        a = sorted(a, key = lambda x : x[0], reverse = True) # sort the array in descending order of numbers
        a = sorted(a, key = lambda x : x[1], reverse = True) # sort the array in descending order of counts
        res = [] # create an empty array to store the result
        for i in range(k): # iterate the indices from 0 to k-1
            res.append (a[i][0]) # append the number at the ith index to the result array
        return res # return the result array
