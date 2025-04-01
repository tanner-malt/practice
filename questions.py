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

"""
Question 5
Level 1

Question: Define a class which has at least two methods: getString: to get a string from console input print
String: to print the string in upper case. Also please include simple test function to test the class methods.

Hints: Use init method to construct some parameters
"""
class question_5:
    def __init__(self):
        self.stored : str
    def get_str(self):
        # This func will get a string from console input
        self.stored = input("Please enter string: ")
    def print_uppers(self):
        print(self.stored.upper())

#question5 = question_5()
#question5.get_str()
#question5.print_uppers()


"""
Question 6
Level 2

Question: Write a program that calculates and prints the value according to the given formula: Q = Square root of [(2 * C * D)/H] 
Following are the fixed values of C and H: C is 50. H is 30. D is the variable whose values should be input to your program in a comma-separated sequence. 
Example Let us assume the following comma separated input sequence is given to the program: 100,150,180 
The output of the program should be: 18,22,24

Hints: If the output received is in decimal form, it should be rounded off to its nearest value 
(for example, if the output received is 26.0, it should be printed as 26) In case of input data being supplied to the question,
 it should be assumed to be a console input.

# User Note, I decided to skip console input for this one, 
"""

def execute_q6():
    csl = [100, 150, 180]
    print(h.solve_q6_formula(csl))

#execute_q6()


"""
Question 7
Level 2

Question: Write a program which takes 2 digits, X,Y as input and generates a 2-dimensional array. 
The element value in the i-th row and j-th column of the array should be i*j. Note: i=0,1.., X-1; j=0,1,¡­Y-1. 
Example Suppose the following inputs are given to the program: 3,5 
Then, the output of the program should be: [[0, 0, 0, 0, 0], [0, 1, 2, 3, 4], [0, 2, 4, 6, 8]]

Hints: Note: In case of input data being supplied to the question, it should be assumed to be a console input in a comma-separated form.

"""

def execute_q7():
    recieved = input("Please enter two digits seperated by a comma: ")
    i, j = recieved.split(",")
    h.two_digits_to_iTimejArray(int(i), int(j))

#execute_q7()

"""
Question 8
Level 2

Question: 
Write a program that accepts a comma separated sequence of words as input and prints the words in a comma-separated sequence after sorting them alphabetically.
 Suppose the following input is supplied to the program: without,hello,bag,world Then, the output should be: bag,hello,without,world

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""
def execute_q8():
    input_str = input("Please Enter Comma seperated words: (spaces count!)")
    input_list =input_str.split(",")
    input_list.sort()
    print(','.join(input_list))

#execute_q8()

"""
Question 9
Level 2

Question£º Write a program that accepts sequence of lines as input and prints the lines after making all characters in the sentence capitalized. 
Suppose the following input is supplied to the program: Hello world Practice makes perfect Then, 
the output should be: HELLO WORLD PRACTICE MAKES PERFECT

Hints: In case of input data being supplied to the question, it should be assumed to be a console input.
"""

def execute_q9():
    input_str = input("Please Enter a Sentence: ")
    uppered_str = []
    for char in input_str:
        char.upper()
        uppered_str.append(char.upper())
    uppered_str = "".join(uppered_str)
    print(uppered_str)

#execute_q9()

"""
Level 2

Question: Write a program that accepts a sequence of whitespace separated words as input and prints the words after removing all duplicate words 
and sorting them alphanumerically. Suppose the following input is supplied to the program: hello world and practice makes perfect and 
hello world again Then, the output should be: again and hello makes perfect practice world

Hints: In case of input data being supplied to the question, it should be assumed to be a console input. 
We use set container to remove duplicated data automatically and then use sorted() to sort the data.
"""

def execute_q10():
    input_str = input("Please Enter a Sentence: ")
    listSplited = h.split_by_space(input_str)
    listSplited.sort()
    listSplited = " ".join(listSplited)
    print(listSplited)

#execute_q10()