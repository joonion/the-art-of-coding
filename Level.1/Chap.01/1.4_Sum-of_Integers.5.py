def sum_of_integers5(n, m):
    return (m * (m + 1) - n * (n - 1)) // 2
 
n, m = map(int, input().split())
s = sum_of_integers5(n, m)
print(s)
