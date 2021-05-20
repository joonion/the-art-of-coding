'''
[Input]
9
31 -41 59 26 -53 58 97 -93 -23 84
[Output]
187 2 6
'''

def solution7(n, S):
    cursum, maxsum, maxi, maxj = 0, 0, -1, -1
    print(cursum, maxsum, maxi, maxj)
    for i in range(n):
        cursum += S[i]
        if cursum <= 0: # reset start position
            cursum, maxi = 0, i + 1
        elif cursum > maxsum:
            maxsum, maxj = cursum, i
        print(cursum, maxsum, maxi, maxj)
    return maxsum, maxi, maxj

# S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
# n = len(S)

n = int(input())
S = list(map(int, input().split()))

maxs, maxi, maxj = solution7(n, S)
print(maxs, maxi, maxj)
