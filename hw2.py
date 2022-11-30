# Erik Lebek
# Cite any sources you used to help with the homework including TAs and classmates

def string3(string):
    """
    Given a string, return a new string made of 3 copies of the last 2 chars of the original string.
    The string length will be at least 2.
    """
    return string[len(string)-2:]+string[len(string)-2:]+string[len(string)-2:]


def has123(nums):
    """
    Given an list of ints, return True if the sequence of numbers
    1, 2, 3 appears in the list somewhere.
    """
    b = False
    for i in range(len(nums)): 
        if nums[i] == 1:
            try:
                if nums[i+1] == 2:
                    try:
                        if nums[i+2] == 3:
                            b = True
                    except:
                        continue
            except:
                continue
    return b

# string 2 count_code
def hascode(string):
    """
    Return the number of times that the string "code" appears anywhere in the given string,
    except we'll accept any letter for the 'd', so "cope" and "cooe" count.
    """
    count = 0
    for i in range(len(string)):
        try:
            if string[i] == "c" and string[i+1] == "o" and string[i+3 == "e"]:
                count += 1
        except:
            continue
    return count

def samecatdog(string):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
   *** This can be simplfied using a Python string method ***
    """
    ccount = 0
    dcount = 0
    for i in range(len(string)):
        try:
            if string[i] == "c" and string[i+1] == "a" and string[i+2 == "t"]:
                ccount += 1
            if string[i] == "d" and string[i+1] == "o" and string[i+2 == "g"]:
                dcount += 1    
        except:
            continue
    return ccount == dcount


from operator import indexOf


def centered_avg(nums):
    """
    Return the "centered" average of a list of ints, which we'll say is the mean average of the
    values, except ignoring the largest and smallest values in the list. If there are
    multiple copies of the smallest value, use just one copy, and likewise for the largest value.
    Use floor division to produce the final average. You may assume that the list is length 3 or more.
      """
    sum = 0
    max = 0
    min = nums[0]
    min_removed = False
    max_removed = False
    for num in nums:
        if num > max:
            max = num
        elif num < min:
            min = num
    for i in range(len(nums)):
        
        if nums[i] == min and not min_removed:
            min_removed = True
            continue
        elif nums[i] == max and not max_removed:
            max_removed = True
            continue
        else:
            sum+=nums[i]
    return sum // (len(nums)-2)

# Test functions
assert string3("Hello") == 'lololo', 'string3(Hello) expected lololo'
print("correct")
assert string3("ab") == 'ababab', 'string3(ab) expected ababab'
print("correct")
assert string3("Hi") == 'HiHiHi', 'string3(Hi) expected HiHiHi'
print("correct")

assert has123([1, 1, 2, 3, 1]) is True, '[1, 1, 2, 3, 1] has 123'
print("correct")
assert has123([1, 1, 2, 4, 1]) is False, '[1, 1, 2, 3, 1] does not have 123'
print("correct")
assert has123([1, 1, 2, 1, 2, 3]) is True, '[1, 1, 2, 1, 2, 3] has 123'
print("correct")

assert hascode("aaacodebbb") == 1, 'aaacodebbb has code'
print("correct")
assert hascode("aaacodebbb") == 1, 'codexxcode has code'
print("correct")
assert hascode("cozexxcope") == 2, 'cozexxcope has code'
print("correct")

assert samecatdog("catdog") is True, 'catdog appear same number of times'
print("correct")
assert samecatdog("catcat") is False, 'catcat does not appear same number of times'
print("correct")
assert samecatdog("1cat1cadodog") is True, '1cat1cadodog appear the same number of times'
print("correct")

assert centered_avg([1, 2, 3, 4, 100]) == 3, 'average [1, 2, 3, 4, 100] is 3'
print("correct")
assert centered_avg([1, 1, 5, 5, 10, 8, 7]) == 5, 'average [1, 1, 5, 5, 10, 8, 7] is 5'
print("correct")
assert centered_avg([-10, -4, -2, -4, -2, 0]) == -3, 'average [-10, -4, -2, -4, -2, 0] is -3'
print("correct")


# Problems found on https://codingbat.com/python
