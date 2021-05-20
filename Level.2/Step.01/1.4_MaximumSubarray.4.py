'''
[Input]
9
31 -41 59 26 -53 58 97 -93 -23 84
[Output]
187 2 6
'''

def max_to_left(mid, low, S):
    lmax, lsum = 0, 0
    for i in range(mid, low - 1, -1):
        lsum += S[i]
        lmax = max(lmax, lsum)
    return lmax

def max_to_right(mid, high, S):
    rmax, rsum = 0, 0
    for i in range(mid, high + 1):
        rsum += S[i]
        rmax = max(rmax, rsum)
    return rmax

def solution4(low, high, S):
    print(low, high)
    if low > high: 
        return 0
    elif low == high: 
        return max(0, S[low])
    else:
        mid = (low + high) // 2
        lmax = max_to_left(mid, low, S)
        rmax = max_to_right(mid + 1, high, S)
        return max(lmax + rmax, \
               solution4(low, mid, S), \
               solution4(mid + 1, high, S))

S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
n = len(S)

# n = int(input())
# S = list(map(int, input().split()))

maxs = solution4(0, n - 1, S)
print(maxs)
