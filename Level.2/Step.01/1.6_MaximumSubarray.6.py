'''
[Input]
9
31 -41 59 26 -53 58 97 -93 -23 84
[Output]
187 2 6
'''

def solution6(n, S):
    cursum, maxsum = 0, 0
    for i in range(n):
        cursum = max(cursum + S[i], 0)
        maxsum = max(cursum, maxsum)
        print(cursum, maxsum)
    return maxsum

S = [31, -41, 59, 26, -53, 58, 97, -93, -23, 84]
n = len(S)

# n = int(input())
# S = list(map(int, input().split()))

maxs = solution6(n, S)
print(maxs)
