'''
[Input]
9
31 -41 59 26 -53 58 97 -93 -23 84
[Output]
187 2 6
'''

def solution3(n, S):
    csum = S[:]
    for i in range(1, n):
        csum[i] += csum[i - 1]
    maxs, maxi, maxj = 0, -1, -1
    for i in range(n):
        for j in range(i, n):
            s = csum[j] - csum[i - 1] if i != 0 else csum[j]
            print(i, j, s)
            if s > maxs:
                maxs, maxi, maxj = s, i, j
    return maxs, maxi, maxj

S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
n = len(S)

# n = int(input())
# S = list(map(int, input().split()))

maxs, maxi, maxj = solution3(n, S)
print(maxs, maxi, maxj)
