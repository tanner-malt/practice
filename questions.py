import helpers as h
'''
Question 1
Level 1

Question: Write a program which will find all such numbers which are divisible by 7 but are not a multiple of 5, between 2000 and 3200 (both included). 
The numbers obtained should be printed in a comma-separated sequence on a single line.

Hints: Consider use range(#begin, #end) method
'''

# Solution:
def execute_q1():
    '''
    Definition: This function will solve question1.
    '''
    get_list = h.divisible7_not5(2000,3200)
    print(','.join(get_list))

#execute_q1()


'''
Question 2
Level 1

Question: Write a program which can compute the factorial of a given numbers. The results should be printed in a comma-separated sequence on a single line. 
Suppose the following input is supplied to the program: 8 Then, the output should be: 40320

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
'''

def execute_q2():
    '''
    Definition: This function will solve question 2.
    '''
    val = input("Please enter value you wish to compute the factorial of: ")
    valorized = h.compute_factorial(int(val))
    print(h.normalize_number(valorized))

#execute_q2()

"""
Question 3
Level 1

Question: With a given integral number n, write a program to generate a dictionary that contains (i, i*i) such that is an integral number between 1 and n 
(both included). and then the program should print the dictionary. Suppose the following input is supplied to the program: 8 Then, the output should be: 
{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. Consider use dict()
"""

def execute_q3():
    '''
    Definition: This function will request an integer, then we will generate a dictionary from i to that value 
    '''
    val = int(input("Please enter value you wish to build a dictionary with: "))
    print(h.build_dict_with_target(val))

#execute_q3()

"""
Question 4
Level 1

Question: Write a program which accepts a sequence of comma-separated numbers from console and generate a list and a tuple which contains every number. 
Suppose the following input is supplied to the program: 34,67,55,33,12,98 Then, the output should be: 
['34', '67', '55', '33', '12', '98'] ('34', '67', '55', '33', '12', '98')

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. tuple() method can convert list to tuple
"""

def execute_q4():
    """
    Definition: This function will ask for a list of numbers, and generate a list and a tuple which contains every number
    """
    comma_list = input("Please enter a list of comma-seperated numbers: ")
    normalized = comma_list.split(",")
    tuple_list = tuple(normalized)
    print(normalized)
    print(tuple_list)

#execute_q4()