# naming of variables
num_coffee_cups = 2     # recommended
ncc = 2                 #legal, not recommended
ashkahfciavbk = 2       # legal, not recommended
x = 2                   # rarely justifiable

PI = 3.141592
N_COURSE = 6            # capital often refers to the "constant" that are unchangable



########################################################################################################################
# prime function
def is_prime(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(n-2):
        if n %(2+i) ==0:
            return False
    return True


'''
if __name__=='__main__': #This is an infinte loop finding even prime, which does not exist
    i=4
    while not is_prime(i):
        print("Just tried!",i)
        i+=2
    print("found an even prime! It is ",i)

if __name__=="__main__":
    i=4
    while True:
        if is_prime(i):
            break
        print("Just tried!",i)
        i+=2
# not recommanded using "break" rather using "not" instead
# while a break is required, really there is a function and break is returned
'''

def find_large_even_prime():
    i =2
    while True:
        if is_prime(i):
            return i
        i +=2


'''
if __name__=='__main__':
    i=4
    while not is_prime(i):
        print("Just tried!",i)
        i+=2
    print("found an even prime! It is ",i)
'''

def is_prime2(n):
    if n<=1:
        return False
    if n==2:
        return True
    for i in range(n-2):
        if (i+2)>2 and i % 2 ==0:
            continue
        '''it is the same as:
        for i in range(3,n-2,2): and start by line 69'''

        if n %(2+i) ==0:
            return False
    return True



########################################################################################################################
# missing K problem
# A list contains the numbers 1,..., n, in some oreder, except k is missing.
# determine k without going over the list multiple times

def missing_k(L):
    for i in range(1,len(L)+1):
        if i not in L:
            return i


# Nested loops -> loop in loop
N = 5
counter = 0
for i in range(3):
    for j in range(2):
        counter += 1
        # print(i,j,counter)

'''
counter = 0
i = 0
for j in range(2):
    counter += 1
    print(i,j,counter)

i=1
for j in range(2):
    counter += 1
    print(i,j,counter)

i=2
for j in range(2):
    counter += 1
    print(i,j,counter) ''' # seperate loops are not efficient

# a better version of finding k
# we know the sum of a full sequence is: 1+2+...+n = n(n+1)/2
# subtract the sum by every element will get k: n(n+1)/2 -(1+2+...+n) = k


def missing_k2(L):
    cur_sum = 0
    for i in L:
        cur_sum += i            # get the sum of the sequence

    n = len(L) + 1              # get the largest element to compute the sum of a full sequence
    return n*(n+1)/2 - cur_sum  # subtract to get k


                                                                                                                        
########################################################################################################################
# print vs return

def f(n):
    n = n*2
    return n+5


def f_print(n):
    n = n*2
    print(n+5)

'''
if __name__ == "__main__":
    print(f(50))       # good code
    print(f_print(50)) # bad code, f_print(50) will print but will return NULL, print(f_print(50)) will print NULL
    f_print(50)        # the same as print(f(50))

    

import submission
if __name__ == "__main__":
    if submission.f(50) == 105:
        return "Test passed"
    if submission.f_print(50) == 105:
        return "Test passed 2" '''



########################################################################################################################
# finding evens in a list
def first_even(L):
    for e in L:
        if e%2 == 0:
            return e
        

'''
if __name__ == "__main__":
    print(first_even([1,3,5,8,10,12])) #only the first even
'''

def first_two_evens(L):
    res=[]                  # temporary list to store the result
    for e in L:
        if e%2==0:
            res.append(e)   # this will create a list with all evens stored, not efficient
    return res[:2]


def first_two_evens_efficient(L):
    res=[]
    count = 0               # counting how many even number stored in the temporary list
    for e in L:
        if e%2==0:
            res.append(e)
            count += 1
            if count == 0:
                return res  # once return, we stop the loop
    return res              # the list will only have length 0 or 1 if returned here



########################################################################################################################
# login & username
def login(username,password):
    if username == "Ken" and password =="abcd":
        return True
    else:
        return False


# suppose we know the password is of length 4, try to find the password
for letter1 in ["a","b","c","d","e","f"]:
    for letter2 in ["a","b","c","d","e","f"]:
        for letter3 in ["a","b","c","d","e","f"]:
            for letter4 in ["a","b","c","d","e","f"]:
                if login("Ken",letter1+letter2+letter3+letter4):
                    password=letter1+letter2+letter3+letter4
                    if login("Ken", password):
                        real_password = password



########################################################################################################################
# finding if the list have the same element
def has_duplicates1(L):
    for i in range(len(L)):
        if L[i] in L[i+1:]:     # sorting the current element to the rest of the list
            return True         # as the list is not sorted, not efficient
    return False


def has_duplicates2(L):
    sorted_L = sorted(L)            # sort the list, so the same element will be next to each other
    for i in range(1,len(L)):
        if sorted_L[i] == L[i-1]:   # only need to find the element next to each other
            return True
    return False



########################################################################################################################
# id() return a specific id for each specific object
n = 42          # print(id(n))
m = n           # print(id(m))
m = 500         # print(id(m))
L = [42, 500]   # print(id(L))
L1 = L          # These two list will have the same id (store in the same place)
L1[0] = 500     # So, change one of them will also change the other: L1 = L = [500,500] now


# alisaing: several varibales refer to the same object (memory address)
# L and L1 are aliases of each other
# if we change contents of L, the contents of L1 change as well, and vice versa


# objects whose contents can change (eg. lists) are MUTABLE
# objects whose contents cannot change (eg. ints, strs, floats) are IMMUTABLE


def change_list(L):
    L[0] = 5


def dont_change_list(L):
    L = [50] #local variable will not change the list


'''
if __name__ == "__main__":
    L2 = [1,2,3]
    change_list(L2)
    print(L2)           # L2 = [5,2,3]
    L2 = [1,2,3]
    dont_change_list(L2)
    print(L2)           # L2 = [1,2,3]
'''


def dont_change_int(n):
    n = 50
'''
if __name__ == "__main__":
    m = 1
    dont_change_int(m)
    print(m)            # m = 1
'''



########################################################################################################################
# address
a = "ESC180"    # first place "ESC 180" to a memory table, assigned an address; then assigned a to that address
b = "ESC180"    # python notice that "ESC 180" already exists, so python assigned that address to b
                # a and b now shared the same address


d = "ESC"
e = "180"
f = d + e
# print(id(a))
# print(id(f))    It was not the same because f is constructed when the code was wrong
                # It save space but wasted time as if python compares f to all the strings in memory table


'''
nums = list(range(-10,300))     # nums = [-10,-9,-8,...,298,299,300]
for i in nums:
    print(i,id(i),id(i+1)-id(i)) # python pre-load (-5,256) numbers into memory table, difference between the address is 32
'''

a = 169275987957
b = 169275987957
# print(id(a),id(b))  # The id are the same



########################################################################################################################
# address with lists
L1 = [1,2,3]
# first, evaluate the right hand side
# it is a list -- move the contents of the list (1,2,3) to memory
# then, place the list into memory in the format [address content 1, address content 2, ...]
# given L1 in variable the address of the list



L2 = [1,2,3]
# 1,2,3 are pre-loaded
# just assigned the new list into memory in the format [address content 1, address content 2, ...]
# (The address of [1,2,3] here is different from the one above) 
# (python remember these two lists as two different one if L2 is not defined as L2 == L1)
# given L2 in variable the address of the list



L1[0] = 2       # change the content in memory table
L1 = L1 + L2    # creates a new list, and makes L1 refer to the new list
L2.extend(L2)   # changes the contents of the list L2



def add_lists_bad(L1,L2):
    L1 = L1 + L2
# create a new list, 
# set local variable L1 to the addresss of that list, 
# the local variable L1 will be deleted after the function, so no change


def add_list_good(L1,L2):
    L1.extend(L2)


def add_list_good1(L1,L2):
    L1 += L2
# the same as L1.extend(L2), not the same as L1 = L1 + L2



L1 = [1,2,3]
L2 = L1
L2[0] = 5       # change both L1 and L2


# we want to make a copy of L1, and place it in L2
# method one
L1 = [1,2,3]
L2 = [L1[0],L1[1],L1[2]]
L1[0] = 5       #change L1 but not L2, since L2 is created independent of L1

# method two
L1 = [1,2,3]
L2 = L1[:]      # same as L2 = [L1[0],L1[1],L1[2]]

# method three
L1 = [1,2,3]
L2 = []
for e in L1:
    L2.append(e) 

# method four
L1 = [1,2,3]
L2 = []
L2.extend(L1)



########################################################################################################################
# list of list, shallow copy, deep copy
L1 = [[1,2],[3,4]]
L2 = L1[:]
# L2 = [L1[0], L1[1]] just copying the address of L1[0], L1[1]
# but do not create a copy of L1[0], L1[1] 
# a shallow copy of a list of lists of ints
L1[1][0] = 6    # L1 = [[1,2],[6,4]], L2 = [[1,2],[6,4]]    L2 changed
L1[0] = 5       # L1 = [5,[6,4]],     L2 = [[1,2],[6,4]]    L2 unchanged


L1 = [[1,2], [3,4]]
L2 = []

for sublist in L1:
    L2.append(sublist[:])   # a deep copy of a list of lists of ints

L1[1][0] = 6                # L1 = [[1, 2], [6, 4]], L2 = [[1, 2], [3, 4]]


L1 = [[[0]]]
for sublist in L1:
    L2.append(sublist[:])   # a shallow copy of a list of lists of ints, L2 will change by L1 = [[[1]]]

import copy
L2 = copy.deepcopy(L1)      # deep copy



########################################################################################################################
# string

s1 = "praxis"
s2 = "esc180"
s1 = "P" + s1[1:]           # s1 = "Praxis"
s2 = s2[:2] + "C" + s2[3:]  # s2 = "esC180"
s3 = s2                     # s3 = "esC180"

s1 = "praxis"
s1.capitalize()             # s1 = "Praxis"


# reverse a string
def reverse_str(s):
    res = ""
    for i in range(len(s)-1,-1,-1):
        res += s[i]             # adding the temporary string from the back of the original input
    return res

def reverse_str2(s):
    res = ""
    for i in range(len(s)):
        res = s[i] + res        # add the new element at the front of the temporary "reversed" string
    return res

def reverse_str3(s):
    res = ""
    for c in s:
        res = c + res           # same as reverse_str2(s)
    return res



########################################################################################################################
# an anagram of s is a string that contains all the same characters as s
# "praxis forever" and "a prefix rovers" are anagrams

def is_anagram1(s1,s2):
    for c in s1:
        if c == " ":
            continue
        if c not in s2:
            return False    # check if all characters in s1 are in s2
    for c in s2:
        if c == " ":
            continue
        if c not in s1:
            return False    # check if all characters in s2 are in s1
    return True



A = "hdatc".replace("c"," ")    # replace "c" with " "
B = "ahdT".lower()              # lower all characters

def is_anagram(s1,s2):
    return sorted(s1.lower().replace(" ","")) == sorted(s2.lower().replace(" ",""))     # more efficient


num = 180
course_name = "ESC" + str(num)  # we cannot add a string with an int, so we need str()



########################################################################################################################
# given a string s, want to dertermine the longest run of the character c in s
# 'aaaa','a' -> 4;  'aabaaa','a' -> 3

def longest_run(s,c):
    for run in range(len(s), 0 , -1):
        if run*c in s:
            return run
    return 0

def longest_run2(s,c):
    max_run = 0
    run = 0
    for ch in s:
        if ch != c:
            max_run = max(max_run,run)
            run = 0
        else:
            run += 1
    return max(max_run, run) 


def n_as_plus_b(s,n):
    '''return True if s contains exactly n "a"s followed by exactly one "b" '''
    cur_run_a = 0
    for i in range(len(s)):
        if s[i] == "a":
            cur_run_a += 1
        elif s[i] == "b":
            if cur_run_a == n:
                if i == len(s) - 1:     # exactly one 'b' if at the end of the string
                    return True
                if s[i+1] != "b":       # search the next character to not be 'b'
                    return True
        else:
            cur_run_a = 0
    return False



########################################################################################################################
# Tuples
# Like lists, but immutable

t = (2,3,4)

# t[0] = 6          # bug, cannot change the member of tuples

t=([2,3],4)
t[0][0] = 6         # no bug, can change the list inside the tuples, t = ([6,3],4)

t = ("a","b","c")
x, y, z = t         # x = "a", y = "b", z = "c"
# x,y = t           # error


def f():
    return 42,43    # returning a tuple
x,y = f()           # x = 42, y = 43



########################################################################################################################
# dictionary: key, value pair
grades = {"PHY":90,"MAT":80,"CSC":90, "CIV":95}

# get all the subjects in which I got a particular grade
def get_subj_by_grade(grades,grade):
    res = []
    for subj, gr in grades.items():
        if gr == grade:
            res.append(subj)
    return res
# print(get_subj_by_grade(grades,90))


#want:{90:["PHY","CSC"],80:["MAT"],95:["CIV"]}
def get_inv_grades(grades):
    res = {}
    for subj,grade in grades.items():
        if grade in res:
            res[grade].append(subj)
        else:
            res[grade] = [subj]
    return res
# print(get_inv_grades(grades))



########################################################################################################################
# delete in list and dictrionary
'''
# wrong delete example
L = [3,4,2,1,2]
for i in range(len(L)-1):
    if L[i] == 4.0: # romove the second component and there are no five component in L as initial
        del L[i]
'''
# correct version
i = 0
L = [3,4,2,1,2]
while i < len(L):
    if L[i] == 4.0:
        del L[i]
    i += 1


def correct_transcript_bad(grades):
    for course in grades:
        if grades[course] not in ["A","A+"]:
            del grades[course]

def correct_transcript_fixed(grades):
    for course in list(grades.keys()):
        if grades[course] not in ["A","A+"]:
            del grades[course]

def drop_everything_bad(grades):
    grades={} # no effect outside the function

def drop_everything2(grades):
    grades.clear() # does have an effect outside the function

def make_csc_100(grades):
    grades["CSC"] = 100 # has an effect outside the function

def drop_everything3(grades):
    while len(grades)>0:
        del grades[list(grades.keys()[0])]

'''
if __name__=="__main__":
    grades = {"PHY":"A+","CIV":"A+","CSC":"A+","ESC":"B+"}
    correct_transcript_fixed(grades)
    print(grades)
    drop_everything2(grades)
    drop_everything3(grades)
'''



########################################################################################################################
# numpy, optimize, and curve fit
import numpy as np      # define a race, race can be multy dimensional

a = np.array([1,2,3])
b = np.array([[1,2,3],[4,5,6]])

# print(b*2)            # python can perform simple math functions without libraries
# print(np.cos(b))      # some need the numpy libraries

import scipy.optimize as optimize
# need a function f, an initial guess, and two data lists
def f(t,a,b):
    return a+t*b
init_guess=(2,0)
xdata = np.array([1,2,3,4])
ydata = np.array([3.1,4.9,7.0,8.9])
popt,pcov = optimize.curve_fit(f,xdata,ydata,p0=init_guess)



########################################################################################################################
# searching and analysis of runtime comlexity

def find_i(L,e):
    '''Return the index of the first appearance of e in L, or None if e is not in L'''
    # return L.index(e)     -> cannot solve when e is not in L
    for i in range(len(L)): # one op (operation)
        if L[i] == e:       # two ops
            return i        # one op
    return None             # one op

# Worse-case runtime complexity: the runtime in the worst case, for imput of size n
# Worse case: e is not in L
# 3*n + 1 operations
# the runtime will be proportional to 3*n+1
# the runtime in the worst case, for large n, will be proportional to n
# the tight upper bound on the asymptotic runtime
# complexity of find_i is 0(n)



# binary search
def find_i_binary(L,e):
    # need a sorted list
    # currently looking at L[low] ... L[high]
    low = 0
    high = len(L)-1
    while high - low >= 2:
        mid = (low + high) // 2
        if L[mid] > e:
            high = mid - 1
        if L[mid] < e:
            low = mid + 1
        else:
            return mid
    if L[low] == e:
        return low
    if L[high] == e:
        return high

'''
L = [1,5,100,102,105,200,250,500,520]
e = 500
print(find_i_binary(L,e))
'''


########################################################################################################################
# sorting methods
def loc_max(L,end):
    '''return the location of the max in L[:end+1]'''
    cur_max = L[0]
    cur_max_loc = 0
    for i in range(1,end+1):
        if L[i] > cur_max:
            cur_max = L[i]
            cur_max_loc = i
    return cur_max_loc



def sellection_sort(L):
    # O(n^2)
    for i in range(len(L)-1):
        max_i = loc_max(L,len(L)-1-i)
        L[max_i],L[len(L)-1-i] = L[len(L)-1-i], L[max_i]
    # the function modify L, so no need to return

'''
if __name__ == "__main__":
    L1 = [2,5,1,10,7]
    sellection_sort(L1)
    print(L1)
'''


# bubble sort
def bubble_sort(L):
    # O(n^2)
    for i in range(len(L)-1):
        swapped = False
        for j in range(len(L)-1-i):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
                swapped = True
        if swapped == False:
            break


# counting sort
def counting_sort(L):
    max_int = max(L)            # maximum integer in the list
    counts=[0]*(1+max_int)      # create a temporary "counting" list
    for e in L:
        counts[e] += 1          # modify the list to count every number, 
                                # showing how many times they exist in the list
                                # as the number stored at that number index in the "counting" list

    sorted_L = []
    for i in range(0,len(counts)):
        sorted_L.extend([i]*counts[i])  # extend the result list by using the info stored in "counting" list
    L[:] = sorted_L
    return L

'''
if __name__=="__main__":
    L = [1,2,1,0,9,2]
    print(counting_sort(L))
'''

# bozosort
import random
def is_sorted_nondecreasing(L):
    for i in range (len(L)-1):
        if L[i]>L[i+1]:
            return False
    return True


def bozosort(L):
    while not is_sorted_nondecreasing(L):
        i,j = int(len(L)*random.random()),int(len(L)*random.random())
        L[i],L[j] = L[j],L[i]
    return L
'''
if __name__=="__main__":
    L = [1,2,1,0,9,2]
    print(bozosort(L))
'''



########################################################################################################################
# Recursion:  functions that call themselves

def fact(n):
    if n <= 1:
        return 1
    else:
        return n * fact(n-1)


# Recursive function f:
# 1. Base case ( an input where you know the output )
# 2. Recursive step ( the answer in terms of the function f )



# start from 0
# each player can say either +1 or +2
# the first player to get the sum 21 wins

def is_winning_sum(s):
    if s == 21:
        return True
    MOVES = [1,2]
    for move in MOVES:
        if is_winning_sum(s+move):
            return False
# is_winning_sum(s+1) is True or is_winning_sum(s+2) is True:
# is_winning_sum(s) is False
    return True



# write a function with complexity O(n) O(n^2*log(n))
def counter(k):
    if k == 0:
        return
    else:
        counter(k-1)
def f(n):
    return counter(n**2*np.log(n))


# recursion with caching
# fib sequence: 1,1,2,3,5,8,13,....
# O(fib(n))
def fib(n):
    if n <= 2:
        return 1
    return fib(n-1)+fib(n-2)

# problem: fib(n-2) may be call from getting fib(n) and fib(n-1)
# repeatation is not convenient and can be avoid

def fib2(n,cache = {1:1,2:1}):
    if n in cache:
        return cache[n]
    cache[n] = fib2(n-1) + fib2(n-2)
    return cache[n]

# need to really compute every fib number once
# other itermediate computations take just two calls



########################################################################################################################
# print out all passwords over an alphabet
def print_all(alphabet,n,start_str = ''):
    ''' print all combinations of elements of alphabet of length m, with string start_str prepended

    >>> print("abc,2,"zz")
    zzaa zzab zzac zzba zzbb zzbc zzca zzcb zzcc '''

    if n == 0:
        print(start_str)
        return
    for letter in alphabet:
        print_all(alphabet,n-1,start_str+letter)

# print_all("ab",2)
# zero recusion when n = n: calls = 1
# 1 recursion when n = n-1: calls = len(alphabet) = m (def it to be m)
# 2 recursion when n = n-2: calls = m^2
# total calls: 1+m+m^2+...m^n = m^(n+1)/(m-1)
# each calls takes amout of time proportional to m("for letter in alphabet")
# total runtime = m*m^(n+1)/(n-1) = O(m^(n+1))


# prepare a list containing all combination of the alphabet with n characters
def all_combinations(alphabet,n,start_str=""):
    if n == 0:
        return [start_str]
    res = []
    for letter in alphabet:
        res.extend(all_combinations(alphabet,n-1,start_str+letter))
    return res
# print(all_combinations('abc',4))


def get_all_subsets(L):
    if len(L)==0:
        return [[]]
    all0 = get_all_subsets(L[1:])
    res = []
    for subset in all0:
        res.append([L[0]]+subset)
    res.extend(all0)
    return res
# print(get_all_subsets([1,2,3]))



########################################################################################################################
#compute the number of trailing zeros in n! (without explicitly computing n!)
def mutiplicity5(n):
    '''return the mutiplicity of 5 in n, n is a positive integer'''
    count = 0
    while n % 5 == 0:
        count += 1
        n //=5
    return count

def trailing_zeros_fast(n):
    '''return the number of trailing zeros in n!'''
    total = 0
    for i in range(1, n+1):
        total += mutiplicity5(i)
    return total
# print(trailing_zeros_fast(1000))



########################################################################################################################
# more on lists
def is_non_decreasing(L):
    '''return true iff the elements of L are arranged in non-decreasing order
    >>> is_non_decreasing([1,2,2,5])
    True
    >>> is_non_decreasing([1,3,9,6])
    False'''

    for i in range(1, len(L)):
        if L[i] < L[i-1]:
            return False
    return True

'''
if __name__=="__main__":
    print(is_non_decreasing([1,2,2,5]))
    print(is_non_decreasing([1,3,9,6]))
'''

def f(x):
    return x**2

'''
g = f
L= [f,"abc","ab",5]
print(L[0](6))                  # 36
L = [42, 43, [43, 45], "abc"]
print(L[2])                     # [43,45]
print(L[2][0])                  # 43
print([43, 45][1])              # 45
'''

L = [[1,2,3,4],
     [2,3,4,5],
     [3,4,5,6]]
L = [[1,2,3,4],[2,3,4,5],[3,4,5,6]]     # These two arrangement is the same

L = [[[[[[[[[[[[[]]]]]]]]]]]]]
'''
print(L[0])
print(L[0][0])
print(L[0][0][0])
print(L[0][0][0][0])
print(L[0][0][0][0][0])
print(L[0][0][0][0][0][0][0][0][0][0][0][0])
# print(L[0][0][0][0][0][0][0][0][0][0][0][0][0]) out of range, error
'''

########################################################################################################################
# L.insert(ind,element) insert element before index ind
# L.index(element) return the index of the first appeance of element in L, produces an error if there is no element in L

L = [5,6,7,9,10]

L.insert(2,42)          # [5,6,42,7,9,10]
L.insert(0,43)          # [43,5,6,42,7,9,10]
L.insert(len(L),45)     # insert 45 at the last of L: [43,5,6,42,7,9,10,45]
L.append(42)            # insert 42 at the last of L: [43,5,6,42,7,9,10,45,42]


L = [5,6,7,9,10]
# print(L.index(7))     2
#print(L[L.index(7)])   7



########################################################################################################################
L = [5,6,7,9,10]
'''
print(6 in L)           #True
print(8 in L)           #False
print(6 not in L)       #False
print(8 not in L)       #True
print(not (6 in L))     #False, will be slower

e = 6
if e in L:
    print("The element", e, "is in L")
else:
    print("The element", e, "is not in L")
'''



########################################################################################################################
Lrange = []
for i in range(2,10,3):
    Lrange.append(i)
# print(Lrange)           # [2, 5, 8]

L = [5,6,10,12,16,17,18,20]
# print(L[1:8:2])         # [6, 12, 17, 20]

Lslice = []
for i in range(1,8,2):
    Lslice.append(L[i])
# print(Lslice)           # [6, 12, 17, 20]


L = [5,6,10,12,16,17,18,20]
# print(L[:3:2])          # [5, 10]
# print(L[5:])            # [17, 18, 20]
# print(L[::])            # [5, 6, 10, 12, 16, 17, 18, 20]
# print(L[5::1])          # [17, 18, 20]

def slice_list(L,start,end,step):
    res = []
    for i in range(start,end,step):
        res.append(L[i])
    return L



########################################################################################################################
x1, x2 = random.random(), random.random()
# is the point (x1, x2) inside the quarter circle?
# can approximate pi using random function
def approx_pi(n_points):
    count = 0
    for i in range(n_points):
        x1, x2 = random.random(), random.random()
        if x1**2 + x2**2 <1:
            count +=1
    return 4* count/ n_points

'''
if __name__=="__main__":
    print(approx_pi(40000))
'''


########################################################################################################################
# pseudo - random numbers
# a sequence of numbers that have random - like properties
# x, f(x), f(f(x)), f(f(f(x)))

def f(x):
    return 173947957 * x % 59

def my_random():
    global x
    x = f(x)
    return x/59

def init_random():
    global x
    x = 3

if __name__=="__main__":
    init_random()
    # print(my_random())
    # print(my_random())
    # print(my_random())
    # print(my_random())
    # print(my_random())



########################################################################################################################
L = [5, 6, 10,2 ,5 ,20, 15]

def manual_slice_white(L,start,end,step):
    res = []
    i = start
    if step > 0:
        while i < end:
            res.append(L[i])
            i += step
    else:
        while i > end:
            res.append(L[i])
            i += step
    while (step > 0 and i < end) or (step < 0 and i > end):
        res.append(L[i])
        i += step

# extend
# L.extend(L1) appends all the elements of L1 to L

L = [5, 6, 7]
L1 = [3, 4]
L.extend(L1)
# print(L)      [5, 6, 7, 3, 4]

L = [5, 6, 7]
L1 = [3, 4]
L.append(L1)
# print(L)      [5, 6, 7, [3, 4]]



# slicing for extending lists "in the middle"
L = [42, 43, 45]
M = [51, 52]

L[1:1] = M      # from one to one but not include one, and replace empty with M
L[1:2] = M      # from one to two but not include two (43), and replace 43 with M
# print(L)      [42, 51, 52, 52, 43, 45]


L = [42, 43, 45]
M = [51, 52]
L[1] = M
# print(L)      [42, [51, 52], 45]

L = [5, 1, 10, 12, 4]
L.sort()        #change L
# print(L)      [1, 4, 5, 10, 12]

L = [5, 1, 10, 12, 4]
sorted(L)               # do not change L, created new sorted(L) set
# print(L)              [5, 1, 10, 12, 4]
# print(sorted(L))      [1, 4, 5, 10, 12]


# print(sorted(["b", "a", "i"]))    # dictionary order: ['a', 'b', 'i']

# print(sorted([1, "a", "i"]))      # error

# print([1,2,3]+[4,5])              # [1, 2, 3, 4, 5]
#L1=[1,2,3],L2=[4,5],L3=[1,2,3,4,5] # plus do not change the original set
L1=[1,2,3]
L2=[4,5]
L1 += L2        # exactly the same as L1.extend(L2), not exactly the same as L1=L1+L2



########################################################################################################################
# transpose
def transpose(M):
    transposed_matrix = []

    for k in range(len(M[1])):
        transposed_matrix.append([0]*len(M))

    for i in range(len(M)):
        for j in range(len(M[i])):
            transposed_matrix[j][i] = M[i][j]
            print(transposed_matrix)
    return transposed_matrix


########################################################################################################################
def gen_nested_loop(n):
    res = "def gen_password():\n"
    for i in range(n):
        res += " " * i + f"for letter{i}:\n"
    res += " " * (n + 1)
    res += "print("
    for i in range(n-1):
        res += f"letter{i} + "
    res += f"letter{n-1}"
    res += ")"
    return res
code = gen_nested_loop(10)