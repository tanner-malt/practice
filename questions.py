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
    print(valorized)
    print(h.normalize_number(valorized))

execute_q2()
