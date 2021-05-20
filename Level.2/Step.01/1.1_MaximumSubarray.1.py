'''
[Input]
9
31 -41 59 26 -53 58 97 -93 -23 84
[Output]
187 2 6
'''

def solution1(n, S):
    maxs, maxi, maxj = 0, -1, -1
    for i in range(n):
        for j in range(i, n):
            s = 0
            for k in range(i, j + 1):
                s += S[k]
            print(i, j, s)
            if s > maxs:
                maxs, maxi, maxj = s, i, j
    return maxs, maxi, maxj

S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
n = len(S)

# n = int(input())
# S = list(map(int, input().split()))

maxs, maxi, maxj = solution1(n, S)
print(maxs, maxi, maxj)
