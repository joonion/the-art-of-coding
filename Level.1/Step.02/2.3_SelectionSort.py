def find_smallest(S):
    smallest, position = S[0], 0
    for i in range(len(S)):
        if S[i] < smallest:
            smallest, position = S[i], i
    return position

def selection_sort(S):
    sorted = []
    while len(S) > 0:
        position = find_smallest(S)
        smallest = S.pop(position)
        sorted.append(smallest)
    return sorted

S = list(map(int, input().split()))
sorted = selection_sort(S)
print(sorted)
print(sorted[0], sorted[-1])