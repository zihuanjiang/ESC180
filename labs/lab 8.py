## problem one
import numpy as np

def print_matrix(M_lol):
    M_matrix = np.array(M_lol)
    return M_matrix
'''
if __name__=="__main__":
    print(print_matrix([[1,2,4],[1,5,7],[2,3,4]]))
'''


## problem two
def get_lead_ind(row):
    for i in range(len(row)):
        if row[i] != 0:
            return i
    return len(row)
'''
if __name__=="__main__":
    print(get_lead_ind([0,0,0,4]))
    print(get_lead_ind([0,0,0,0,0]))
'''


## problem three
def get_row_swap(M,star_i):
    row_to_swap = star_i
    for i in range(star_i,len(M)):
        if get_lead_ind(M[i]) < get_lead_ind(M[row_to_swap]):
            row_to_swap = i
    return row_to_swap
'''
if __name__=="__main__":
    M = [[5,6,7,8],[0,0,0,1],[0,0,5,2],[0,1,0,0]]
    print(get_row_swap(M,1))
'''


## problem four
def add_rows_coefs(r1,c1,r2,c2):
    result = [0]*len(r1)
    for i in range(len(r1)):
        result[i] = r1[i]*c1 + r2[i]*c2
    return result
'''
if __name__=="__main__":
    R1 = [1,2,3,4,5,6]
    R2 = [2,3,4,5,6,7]
    print(add_rows_coefs(R1,1,R2,1))
'''


## problem five
def eliminate(M,row_to_sub,best_lead_ind):
    for i in range(row_to_sub+1,len(M)):
        support_index = get_lead_ind(M[row_to_sub]) # get the position
        lead_index_row_to_sub = M[row_to_sub][support_index] #get the value
        support_index2 = 1/ lead_index_row_to_sub
        row_to_swap_with_leading_1 = add_rows_coefs(M[row_to_sub],\
        support_index2,M[row_to_sub],0)

        c1 = M[i][best_lead_ind]
        M[i] = add_rows_coefs(row_to_swap_with_leading_1,-c1,M[i],1)
    return M
'''
if __name__=="__main__":
    M = [[5,6,7,8],[0,0,1,1],[0,0,5,2],[0,0,7,0]]
    print(print_matrix(eliminate(M,1,2)))
'''


## problem six
def forward_step(M):
    for i in range(len(M)):
        row_swap_index = get_row_swap(M,i)
        M[i],M[row_swap_index] = M[row_swap_index],M[i]
        #print(print_matrix(M))
        eliminate(M,i,get_lead_ind(M[i]))
        #print(print_matrix(M))
    return M

if __name__=="__main__":
    M = [[0,0,1,0,2],[1,0,2,3,4],[3,0,4,2,1],[1,0,1,1,2]]
    print(print_matrix(forward_step(M)))



## problem seven
def eliminate_back(M,row_to_sub,best_lead_ind):
    for i in range(row_to_sub-1,-1,-1):
        support_index = get_lead_ind(M[row_to_sub]) # get the position
        lead_index_row_to_sub = M[row_to_sub][support_index] #get the value
        support_index2 = 1/ lead_index_row_to_sub
        row_to_swap_with_leading_1 = add_rows_coefs(M[row_to_sub],\
        support_index2,M[row_to_sub],0)

        c1 = M[i][best_lead_ind]
        M[i] = add_rows_coefs(row_to_swap_with_leading_1,-c1,M[i],1)

    dividing_leading_coef(M)

    return M

def backward_step(M):
    for i in range(len(M)-1,-1,-1):
        eliminate_back(M,i,get_lead_ind(M[i]))
    return M

def dividing_leading_coef(M):
    for i in range(len(M)):
        lead_index_i = M[i][get_lead_ind(M[i])]
        if lead_index_i != 1:
            support_index = 1/ lead_index_i
            M[i] = add_rows_coefs(M[i],support_index,M[i],0)
    return M
'''
if __name__=="__main__":
    M = [[1,-2,3,22],[3,10,1,314],[1,5,3,92],]
    print(print_matrix(forward_step(M)))
    print(print_matrix(backward_step(M)))
'''


## problem eight
def build_augmented_matrix(M,b):
    for i in range(len(M)):
        M[i].append(b[i])
    return M

def perform_Gaussian_Elimination(M,b):
    Augmented_matrix = build_augmented_matrix(M,b)
    Augmented_matrix = forward_step(Augmented_matrix)
    Augmented_matrix = backward_step(Augmented_matrix)
    return Augmented_matrix

def solve(M,b):
    M = perform_Gaussian_Elimination(M,b)
    x = [0]*len(M)
    for i in range(len(M)):
        All_row_i_is_zero = True
        for j in range(len(M[i])-1):
            if M[i][j] != 0:
                All_row_i_is_zero = False
        if All_row_i_is_zero == True:
            if M[i][len(M[i])-1] != 0:
                return "No solution"
            else:
                return "Infinite solution"

    for i in range(len(M)):
        support_index_i = get_lead_ind(M[i])
        x[support_index_i] += M[i][len(M[i])-1]
    return x


if __name__=="__main__":
    M = [[1,-2,3],[3,10,1],[1,5,3],]
    b = [22,314,92]
    print(print_matrix(solve(M,b)))

    M1 = [[1,-1,1],[1,2,4],[1,3,9]]
    b1 = [6,0,2]
    print(print_matrix(solve(M1,b1)))











