import math

def divisible7_not5(lower_bound: int, upper_bound: int):
    '''
    Definition: This function will take a lower bound and an upper bound, and will return a list of integers that are divisble by 7, and not by 5.

    Parameters:
    lower_bound -> integer that is smaller than upper bound. The smallest value that will be searched
    upper_bound -> integer. The largest value that will be searched
    '''
    list_of_valids = []
    for i in range(lower_bound, upper_bound+1):
        if (i % 7 == 0) and not (i % 5 == 0):
            list_of_valids.append(str(i))

    return list_of_valids

def compute_factorial(input_val: int):
    '''
    Definition: This will return the integer version of a factorial, given an input integer.

    Parameters:
    input-> an integer
    '''
    base = 1
    while input_val > 0:
        base = input_val * base
        input_val -=1
    return base

def normalize_number(input_val: int) -> str:
    '''
    Definition: This will return a number with commas separating every 3 places

    Parameters:
    input-> an integer
    '''
    input_str = str(input_val)
    char_count = len(input_str)
    
    if char_count <= 3:
        return input_str
    else:
        leading = char_count % 3
        if leading == 0:
            leading = 3
        header = input_str[:leading]
        ending = input_str[leading:]
        vals = [ending[i:i+3] for i in range(0, len(ending), 3)]
        final = [header] + vals
        return ','.join(final)

'''
This was original solution to question 3, but i needed to work on this more, then i realized there was a simpler way
def build_dict_with_target(target: int) -> dict:
    test = {value: value**2 for value in range(target+1)}
    print(test)
    return test
'''

def build_dict_with_target(target: int) -> dict:
    '''
    Definition: This will build a dictionary with some target integer at least 1. 

    Parameters:
    target-> an integer

    Return:
    Will return a dictionary from 1 to the target, for every integer from 1 to the target it will create a key of that integer, with the value being
    the key squared. 
    '''
    new_dict = dict()
    for i in range(1,target+1):
        new_dict[i] = i*i
    return new_dict

def solve_q6_formula(csl: list):
    '''
    Definition: This will plug into the formula presented by question 6 and return the solution

    Parameters:
    csl-> a list of integers

    Returns:
    will give a list for every integer in the provided list
    '''
    c = 50 
    h = 30
    return_list = []
 

    for val in csl:
        return_list.append(round(math.sqrt(2 * c * val/h)))

    return return_list

def two_digits_to_iTimejArray(i, j):
    '''
    Definition: This will take two digits, and return an array that has i * j for the ith and jth positions

    Parameters:
    ijList-> a list of two integers

    Returns:
    a 2D-array that has i * j for the ith and jth positions
    '''
    rows, cols = i , j
    array_2d = [[0 for _ in range(cols)] for _ in range(rows)]

    print(array_2d)
    for ele in range(i):
        for val in range(j):
            array_2d[ele][val] = ele * val

    print(array_2d)

def split_by_space(inpString: str):
    '''
    Definition: This will take a string as the input, and will break it up by white space.

    Parameters:
    inpString-> a string 

    Returns:
    a list that has been seperated by whitespace by the inpString
    '''
    newList = inpString.split(" ")
    return newList