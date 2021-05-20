def sum_of_integers2(n):
    if n == 1:
        return 1
    else:
        return n + sum_of_integers2(n - 1)
 
n = int(input())
s = sum_of_integers2(n)
print(s)
