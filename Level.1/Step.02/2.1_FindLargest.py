def find_largest(S):
    largest = S[0]
    for i in range(len(S)):
        if S[i] > largest:
            largest = S[i]
    return largest

S = list(map(int, input().split()))
largest = find_largest(S)
print(largest)
