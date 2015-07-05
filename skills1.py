"""Skills Assessment: Lists.

To work on an item, uncomment the entire function (including the docstring)
and then run this script. It should output an error that the newly-uncommented
function is now failing its tests.

Edit the function body until you have a solution and the test passes, and then
move on to the next function.

This assessment is DUE TO YOUR ADVISOR BY SUNDAY EVENING.
"""

def all_odd(number_list):
    """Return a list of only the odd numbers in the input list.

        >>> all_odd([1, 2, 7, -5])
        [1, 7, -5]

        >>> all_odd([2, -6, 8])
        []

    """
    odd_list= []
    for i in range(len(number_list)):
        if (number_list[i]%2) != 0:
           odd_list.append(number_list[i])  
    return odd_list
print all_odd([1,2,7,-5])
print all_odd([2, -6, 8])  


def all_even(number_list):
    """Return a list of only the even numbers in the input list.

        >>> all_even([2, 6, -1, -2])
        [2, 6, -2]

        >>> all_even([-1, 3, 5])
        []

    """
    even_list= []
    for i in range(len(number_list)):
        if (number_list[i]%2) == 0:
           even_list.append(number_list[i])  
    return even_list
print all_even([2,6,-1,-2])
print all_even([-1, 3, 5])


def print_indeces(my_list):
    """Print the index of each list item, followed by the item itself.
    Do this without using a counting variable. I.e. don't do something
    like this:

    count = 0
    for item in list:
        print count
        count = count + 1

    Output should look like this:

    >>> print_indeces(["Toyota", "Jeep", "Volvo"])
    0 Toyota
    1 Jeep
    2 Volvo

    """
    for i in range(len(my_list)):
        print i, my_list[i]    
print_indeces(["Toyota","Jeep","Volvo"])


def long_words(word_list):
    """Return all words in input list that are longer than 4 characters.

        >>> long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
        ['hello', 'bacon', 'bacon']

        >>> long_words(["all", "are", "tiny"])
        []

    """
    words_longer_than_4chars=[]
    for i in range(len(word_list)):
        if len(word_list[i]) > 4:
            words_longer_than_4chars.append(word_list[i])
    return words_longer_than_4chars
print long_words(["hello", "hey", "spam", "spam", "bacon", "bacon"])
print long_words(["all", "are", "tiny"])
          


def smallest_int(number_list):
    """Find the smallest integer in a list of integers and return it.

        >>> smallest_int([-5, 2, -5, 7])
        -5

    if the input list is empty, return None:

        >>> smallest_int([]) is None
        True

    """
    if number_list == []:
        return None
        print True    
    else:
        minimum = number_list[0] 
        
        for i in range(len(number_list)-1): 
            if number_list[i] > number_list[i+1]:
                minimum = number_list[i+1]
            else:
                minimum = number_list[i] 
        return minimum

print smallest_int([-5, 2, -5, 7])
print smallest_int([])



def largest_int(number_list):
    """Find the largest integer in a list of integers and return it.

        >>> largest_int([-5, 2, -5, 7])
        7

    if the input list is empty, return None:

        >>> largest_int([]) is None
        True

    """

    
    if number_list == []:
        return None
        print True    
    else:
        maximum = number_list[0] 

        for i in range(len(number_list)-1): 
            if number_list[i] < number_list[i+1]:
                maximum = number_list[i+1]
            else:
                maximum = number_list[i] 
        return maximum

print largest_int([-5,2,-5,7])
print largest_int([])



def halvesies(number_list):
    """Return list of numbers from input list, each divided by two.

        >>> halvesies([2, 6, -2])
        [1.0, 3.0, -1.0]

    If any of the numbers are, make sure you don't round off the half:

        >>> halvesies([1, 5])
        [0.5, 2.5]

    """
    for i in range(len(number_list)):
        number_list[i] = number_list[i]/float(2)
    return number_list    
halvesies([2,6,-2])
halvesies([1,5])         


def word_lengths(word_list):
    """Return the length of words in the input list.

        >>> word_lengths(["hello", "hey", "hello", "spam"])
        [5, 3, 5, 4]

    """
    len_list = []
    for i in range(len(word_list)):   
      len_list.append(len(word_list[i]))
    return len_list
print word_lengths(["hello", "hey", "hello", "spam"])     


def sum_numbers(number_list):
    """Return the sum of all of the numbers in the list.

    Python has a built-in function, `sum()`, which already does this -- but for
    this exercise, you should not use it.

        >>> sum_numbers([1, 2, 3, 10])
        16

    Any empty list should return the sum of zero:

        >>> sum_numbers([])
        0

    """
    total = 0
    if number_list == []:
       return 0 
    else:   
        for x in range(len(number_list)):
            total  += number_list[x]
        return total
print sum_numbers([1,2,3,10])
print sum_numbers([])

def mult_numbers(number_list):
    """Return product (result of multiplication) of the numbers in the list.

        >>> mult_numbers([1, 2, 3])
        6

    Obviously, if there is a zero in the input, the product will be zero:

        >>> mult_numbers([10, 20, 0, 50])
        0

    As explained at http://en.wikipedia.org/wiki/Empty_product, if the list is
    empty, the product should be 1:

        >>> mult_numbers([])
        1

    """
    mult = 1
    if number_list == []:
       print '1'
    else:    
        for x in range(len(number_list)):
            mult *= number_list[x]
        return mult
print mult_numbers([1,2,3])
print mult_numbers([10,20,0,50])
print mult_numbers([])

def join_strings(word_list):
    """Return a string of all input strings joined together.

    Python ha a built-in method on lists, `join` -- but this exercise, you
    should not use it.

        >>> join_strings(["spam", "spam", "bacon", "balloonicorn"])
        'spamspambaconballoonicorn'

    For an empty list, you should return an empty string:

        >>> join_strings([])
        ''

    """
    adding_strings = ''
    for i in range(len(word_list)):
        #print word_list[i]
        adding_strings += word_list[i]
    return adding_strings
print join_strings(["spam", "spam", "bacon", "balloonicorn"])
print join_strings([])


def average(number_list):
    """Return the average (mean) of the list of numbers given.

        >>> average([2, 12, 3])
        5.666666666666667

    There is no defined answer if the list given is empty. It's fine if
    this raises an error when given an empty list.
    """

    total = 0
    for x in range(len(number_list)):
        avg = 1
        total  += number_list[x]
        average = total/float(len(number_list))
    return average
print average([2,12,3])



##############################################################################
# END OF SKILLS TEST; YOU CAN STOP HERE OR YOU CAN WORK ON ADVANCED PROBLEMS


def advanced_join_strings(list_of_words):
    """Return a single string with each word from the input list
     separated by a comma.

         >>> advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
         'Labrador, Poodle, French Bulldog'

     If there's only one thing in the list, it should return just that
     thing, of course:

         >>> advanced_join_strings(["Pretzel"])
         'Pretzel'

    """
    adding_strings = ''
    for i in range(len(list_of_words)):
        adding_strings += list_of_words[i]
        if i != len(list_of_words)-1:
            adding_strings = adding_strings +', '

    return adding_strings

print advanced_join_strings(["Labrador", "Poodle", "French Bulldog"])
print advanced_join_strings(["Pretzel"])


##############################################################################
# You can ignore everything after here

if __name__ == "__main__":
    import doctest
    print
    result = doctest.testmod()
    if not result.failed:
        print "*** %s TESTS PASSED. GOOD WORK!" % result.attempted
    print
