# Number validation and conversion to float
#                   
# See README for program description.

import re

def exit_program(input_str):
    if input_str == 'e':
        print("Goodbye!")
        return True
    
def remove_whitespace(string):
    string = string.replace(' ', '')
    string = string.replace('\t', '')
    string = string.replace('\n', '')
    return string
            
def validate_number(num_str):
    '''Checks whether a string can be interpreted as a number.'''
    '''Argument shouldn't contain whitespaces.'''

    # eliminating the possibility of a later IndexError:
    if not num_str:
        return False
    
    # there exits an invalid character at any position in num_str:
    valid = '0123456789.-+()'
    inv_char = False
    for i in range(len(num_str)):
        if num_str[i] not in valid:
            inv_char = True
    
    inv_end = num_str[-1] not in '0123456789.)'
    mult_dots = num_str.count('.') > 1
    uneq_parent = num_str.count('(') != num_str.count(')') is True

    # only unary sign/s or nothing inside parentheis, e.g ((+)), (-+):
    inv_parent_1 = re.match(r'.*[(]+[+-]*[)]+.*', num_str) is not None
    
    # right parenthesis is before left parenthesis or before a digit:
    inv_parent_2 = re.match(r'.*[)].*[(0-9]+.*', num_str) is not None
        
    # a unary is preceded by something other than unary or '('
    inv_bunar = re.match(r'.*[^\+\-\(]+[-+].*', num_str) is not None

    # a dot is followed by something other than a digit or than ')'
    # and it is not the last character (at index num_str[-1]):
    inv_aft_dot = re.match(r'.*[.]+[^)0-9]+.*', num_str) is not None
        
    invals = (inv_char,
              inv_end,
              mult_dots,
              uneq_parent,
              inv_parent_1,
              inv_parent_2,
              inv_bunar,
              inv_aft_dot)
    
    if any(invals):
        return False
    
    return True

def remove_parenthesis(string):
    string = string.replace('(', '')
    string = string.replace(')', '')
    return string

def reduce_sign(string):
    '''Simplifies multiple unary pluses and/or minuses.'''
    '''Normally float() does this, but not when passed a string'''
    prefix_signs = r'\A[+-]+'
    list_signs = re.findall(prefix_signs, string)
    if list_signs:
        to_remove = len(list_signs[0])
        string = string[to_remove:]
        if list_signs[0].count('-') % 2 == 0:
            return string
        else:
            return '-' + string 
    return string

def convert_to_float(num_str):
    if num_str == '.' or num_str == '-.':
        return 0.0
    else:
        try:
            return float(num_str)
        except (SyntaxError, ValueError, TypeError):
            print('Not a number.')
            pass
        return False

# driver code:
def main():
    print('Enter "e" to exit.')
    while True:      
        num_str = input('Input a number to normalize: ')
        if not num_str:
            print('Not a number.')
            continue
        elif exit_program(num_str):
            break
        num_str = remove_whitespace(num_str)
        if validate_number(num_str) == False:
            print('Not a number.')
            continue
        num_str = remove_parenthesis(num_str)
        num_str = reduce_sign(num_str)
        if convert_to_float(num_str) is False:  
            continue
        else:
            num_str = convert_to_float(num_str)
            print('Normalized number of type float:', num_str)

main()
