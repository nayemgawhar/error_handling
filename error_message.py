def error_message(e):
    if e == "IndexError":
        print('Raised when the index of a sequence is out of range.')
    if e == "NameError":
        print('Variable is not found in the local or global scope.')
    if e == "IndentationError":
        print('Raised when there is an incorrect indentation.')
    if e == "TypeError":
        print('Raised when a function or operation is applied to an object of an incorrect type.')
    if e == "ValueError":
        print('Raised when a function gets an argument of correct type but improper value.')
    if e == "ZeroDivisionError":
        print('Raised when the second operand of a division or module operation is zero.')


    return error_message


