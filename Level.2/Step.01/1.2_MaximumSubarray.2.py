'''
[Input]
9
31 -41 59 26 -53 58 97 -93 -23 84
[Output]
187 2 6
'''

def solution2(n, S):
    maxs, maxi, maxj = 0, -1, -1
    for i in range(n):
        s = 0
        for j in range(i, n):
            s += S[j]
            print(i, j, s)
            if s > maxs:
                maxs, maxi, maxj = s, i, j
    return maxs, maxi, maxj

S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
n = len(S)

# n = int(input())
# x = list(map(int, input().split()))

maxs, maxi, maxj = solution2(n, S)
print(maxs, maxi, maxj)
