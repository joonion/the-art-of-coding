def insertion_sort(S):
    for i in range(1, len(S)):
        x = S[i]
        j = i - 1
        while (j > 0 and S[j] > x):
            S[j + 1] = S[j]
            j -= 1
        S[j + 1] = x

S = list(map(int, input().split()))
sorted = insertion_sort(S)
print(sorted)
print(sorted[0], sorted[-1])