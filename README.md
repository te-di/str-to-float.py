# str-to-float.py
Coverts a numeric string to float.
Sort of extension to float(&lt;some_numeric_string>).



            Number validation and conversion to float



The program tries to interpret an input of "str" type as a number.
If determined possible, the representation of the number is normalized
and converted to "float" type.


Calculation is not done, which is to say the program doesn't work with
complex expressions that contain, for example, 2 numbers, binary operators
(e.g. doesn't calculate '2+3' to return 5.0, which is what eval() would
do) or math functions.
Such inputs are treated as non-numeric and conversion is not attempted.


Examples of conversion:

input string: '-+3', converted: -3.0

input string: '((-(-3)))', converted: 3.0

input string: '-3(.3)', converted: -3.3
  
  
(Inspired by a calculator)
