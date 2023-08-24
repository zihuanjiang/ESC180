import math

# problem 1
L = [1, 2, 3, 4, 5, 6]
def count_evens(L):

    count = 0

    for i in range (len(L)):

        if L[i] % 2 == 0:
            count += 1

    return count

print(count_evens(L))


# problem 2

L = [1, 2, 3]

def list_to_str(lis):

    string = "["
    for i in range (len(lis)-1):

        string += str(lis[i]) + ", "

    return string + str(lis[len(lis)-1]) + "]"

print(list_to_str(L))




# problem 3

L1 = [1, 2, 3, 4]
L2 = [1, 2, 3, 4, 5]
L3 = [1, 2, 3, 4, 6]
L4 = [1, 2, 3, 4, 6]


def lists_are_the_same(list1, list2):

    same_list = True

    if len(list1) != len(list2):
        same_list = "False"


    else:
        for i in range (len(list1)):
            if list1[i] != list2[i]:
                same_list = "False"
                break

    return same_list

print(lists_are_the_same(L1, L2))
print(lists_are_the_same(L1, L3))
print(lists_are_the_same(L4, L3))


# problem 4


def simplify_fraction(n, m):

    divisor = math.gcd(n, m)

    simplified_fraction = str(int(n/divisor)) + "/" + str(int(m/divisor))

    return simplified_fraction

print(simplify_fraction(80, 100))


# Problem 5

Pi = math.pi

def pi_function(n):
    approximation_pi = 0
    for i in range(0,n+1):
        approximation_pi += (-1)**i/(2*i+1)
    approximation_pi *= 4
    return approximation_pi

def agree_significant_digit(N):
    terms_required = 0
    while int(Pi*(10**(N-1))) != int(pi_function(terms_required)*(10**(N-1))):
        terms_required += 1
    return terms_required

print(agree_significant_digit(2))
print(Pi)
print(pi_function(18))


# Problem 6
''' We already know the use of built-in function math.gcd , and it is implemented on problem 4.'''
print(lists_are_the_same(L1, L2))