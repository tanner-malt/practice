'''
Question 1
Level 1

Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: Consider use range(#begin, #end) method
'''

# Solution:
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

def execute_q1():
    '''
    Definition: This function will solve question1.
    '''
    get_list = divisible7_not5(2000,3200)
    print(','.join(get_list))

#execute_q1()


'''
Question 2
Level 1

Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
'''
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

def normalize_number(input_val: int):
    '''
    Definition: This will return a number with commas seperating every 3 places

    Parameters:
    input-> an integer
    '''
    commas = len(str(input_val))
    if commas <= 3:
        return input_val
    else:
        missed = len(str(input_val)) % 3
        header = str
        print(missed)
        return missed

def execute_q2():
    '''
    Definition: This function will solve question 2.
    '''
    val = input("Please enter value you wish to compute the factorial of: ")
    valorized = compute_factorial(int(val))
    print(valorized)
    print(normalize_number(valorized))

execute_q2()
