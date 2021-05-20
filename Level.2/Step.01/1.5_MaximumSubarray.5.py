'''
[Input]
9
31 -41 59 26 -53 58 97 -93 -23 84
[Output]
187 2 6
'''

def maxpos(left, mid, right):
    if left > mid:
        return -1 if left > right else 0 if mid > right else 1
    else:
        return 0 if mid > right else 1

def max_to_left(mid, low, S):
    lmax, lsum, lpos = 0, 0, -1
    for i in range(mid, low, -1):
        lsum += S[i]
        if lsum > lmax:
            lmax, lpos = lsum, i
    return lmax, lpos

def max_to_right(mid, high, S):
    rmax, rsum, rpos = 0, 0, -1
    for i in range(mid, high + 1):
        rsum += S[i]
        if rsum > rmax:
            rmax, rpos = rsum, i
    return rmax, rpos

def solution5(low, high, S):
    print(low, high)
    if low > high: 
        return 0, -1, -1
    elif low == high: 
        return max(0, S[low]), low, high
    else:
        mid = (low + high) // 2
        left, li, lj= solution5(low, mid, S)
        lmax, lpos = max_to_left(mid, low, S)
        rmax, rpos = max_to_right(mid + 1, high, S)
        right, ri, rj = solution5(mid + 1, high, S)
        pos = maxpos(left, lmax + rmax, right)
        if pos == -1: # max is in the left
            return left, li, lj
        elif pos == 0: # max is in the middle (crossing)
            return lmax + rmax, lpos, rpos
        elif pos == 1: # max is in the right
            return right, ri, rj


S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
n = len(S)

# n = int(input())
# S = list(map(int, input().split()))

maxs, maxi, maxj = solution5(0, n - 1, S)
print(maxs, maxi, maxj)
