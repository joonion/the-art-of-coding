def find_largest(S):
    largest = 0
    for i in range(len(S)):
        if S[i] > largest:
            largest = S[i]
    return largest

def find_smallest(S):
    largest = 0
    for i in range(len(S)):
        if S[i] > largest:
            largest = S[i]
    return largest

def find_both(S):
    winners, losers = [], []
    for i in range(0, len(S), 2):
        if i == len(S) - 1: # last key when len(S) is odd.
            winners.append(S[i])
            losers.append(S[i])
        elif S[i] >= S[i + 1]:
            winners.append(S[i])
            losers.append(S[i + 1])
        else:
            winners.append(S[i + 1])
            losers.append(S[i])
    return find_largest(winners), find_smallest(losers)

S = list(map(int, input().split()))
largest, smallest = find_both(S)
print(largest, smallest)
