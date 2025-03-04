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