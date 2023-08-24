# Problem 1


def power(x, n):

    if n == 0:
        return 1

    elif n == 1:
        return x

    else:
        return x * (power(x, n-1))

print(power(2, 5))



# Problem 2


def interleave(L1, L2):

    if len(L1) == 0:
        return []

    else:
        return [L1[0] , L2[0]] + interleave(L1[1:], L2[1:])

print (interleave([1,2,3],[4,5,6]))



# Problem 3


def reverse_rec(L):

    if len(L) == 0:
        return []

    else:
        return [L[-1]] + reverse_rec(L[:-1])


print(reverse_rec([1, 2, 3, 4, 5]))



# Problem 4

zigzag2 = []

def zigzag1(L):

    global zigzag2

    if len(L) == 0:
        return []

    elif len(L) == 1:
        return L[0]

    else:
        zigzag2.append(L[0])
        zigzag2.append(L[-1])
        zigzag1(L[1:-1])

    return zigzag2

print(reverse_rec(zigzag1([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])))



# Problem 5

def paren_left(s):
    if str.find(s,'(') == -1:
        return 0
    else:
        slicing_index = str.find(s,'(')
        slicing_result = s[slicing_index+1 :]
        return 1+ paren_left(slicing_result)

def paren_right(s):
    if str.find(s,')') == -1:
        return 0
    else:
        slicing_index = str.find(s,')')
        slicing_result = s[slicing_index+1 :]
        return 1+ paren_right(slicing_result)

def is_balanced(s):
    if paren_left(s) == paren_right(s):
        return True
    else:
        return False

s = "a(d)j((k)"
b = "())("
print(is_balanced(s))
print(is_balanced(b))



def is_balanced(s):
    '''Return True iff the parentheses in s are balanced.

    '''
    #Idea: find the innermost (...) pair, and remove it, then see if the
    #resultant expression is balanced.

    paren_end = s.find(')')                #The first ')' in the string
    if paren_end == -1:
        return '(' not in s
    paren_start = s[:paren_end].rfind('(') #The first '(' to the right of the
                                           #first ')' in the string
    if paren_start == -1:
        return False

    if paren_end < paren_start:
        return False

    return is_balanced(s[:paren_start] + s[paren_end + 1:])
