# sum of cubes
def my_function(n):
    total = 0
    for i in range(1, n+1):
        total += i**3
    return total

print(my_function(5))


def my_function2(n):
    res = (n**2*(n+1)**2)/4
    return res

print(my_function2(5))


def check_sum(n):
    if my_function(n) == my_function2(n):
        return True
    else:
        return False

print(check_sum(2))


def check_sums_up_to_n(N):
    for i in range(1,N+1):
        if check_sum(i) == False:
            return False
    else:
        return True

print(check_sums_up_to_n(100))



def pi_function(n):
    total = 0
    for i in range(0,n+1):
        total += (-1)**i/(2*i+1)
    total *= 4
    return total

print(pi_function(1000))