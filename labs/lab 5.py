# problem 1


L1 = [1, 2, 3, 4]
L2 = [1, 2, 3, 4, 5]
L3 = [2, 2, 3, 4]
L4 = [1, 2, 3]

def list1_starts_with_list2(list1, list2):

    list1_starts_with_list2 = False

    if len(list1) >= len(list2) and list1[0] == list2[0]:

        list1_starts_with_list2 = True

    else:

        list1_starts_with_list2 = False

    return list1_starts_with_list2

print(list1_starts_with_list2(L1, L4))



# problem 2

L1 = [4, 10, 2, 3, 50, 100, 140, 147, 1235]
L2 = [10, 2, 50]

def match_pattern (list1, list2):

    match_pattern = 0
    pattern_matched = False

    for i in range (len(list1) - len(list2)):


        for k in range (len(list2)):

            if list1[i + k] == list2[k]:

                match_pattern += 1

        if match_pattern == len(list2):

            pattern_matched = True
            break

        else:

            match_pattern = 0
            continue


    return pattern_matched

print(match_pattern(L1, L2))




# problem 3
def repeats(list0):
    for i in range(len(list0)-1):
        if list0[i] == list0[i+1]:
            return True
    return False

print(repeats([0,1,2,3,2,4]))
print(repeats([0,1,2,2,4]))

# problem 4 (a)
def print_matrix_dim(M):
    a = len(M)
    for i in range(len(M)-1):
        if len(M[i]) == len(M[i+1]):
            b = len(M[0])
        else:
            return "That's not a matrix."
    return str(a) + "x" + str(b)

M1 = [[0,1],[0,2],[0,3]]
M2 = [[0,1],[0,2],[0,3,0]]
print(print_matrix_dim(M1))
print(print_matrix_dim(M2))

# problem 4 (b)
def mult_M_v(M, v):
    res = []
    for i in range(len(M)-1):
        if len(M[i]) != len(M[i+1]):
            return "That's not a matrix"
    if len(M[0]) != len(v):
        return "Matrix and vector do not match."
    else:
        for i in range(len(M)):
            k = 0
            for j in range(len(M[i])):
                k += M[i][j] * v[j]
            res.append([k])
        return res

M1 = [[2,1],[4,2],[1,3]]
L = [4,1]
print(mult_M_v(M1,L))



# problem 4c

M1 = [[1, 2, 3], [4, 5, 6]]
M2 = [[1, 2], [3, 4], [5, 6]]
M3 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]


def mult(M1, M2):

    res = []

    if len(M1[0]) != len(M2):

        res = "The size of 2 matrices does not match."

    else:

        for i in range (len(M1)):

            res.append([0] * len(M2[0]))

            for j in range (len(M2[0])):

                for k in range (len(M1[0])):

                    res[i][j] += M1[i][k] * M2[k][j]


    return res

print(mult(M1, M3))

