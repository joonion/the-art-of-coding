def find_both(S):
    largest, smallest = S[0], S[0]
    for i in range(1, len(S)):
        if S[i] > largest:
            largest = S[i]
        if S[i] < smallest:
            smallest = S[i]
    return largest, smallest

S = list(map(int, input().split()))
largest, smallest = find_both(S)
print(largest, smallest)
