def sum_of_integers3(n, s):
    if n == 0:
        return s
    else:
        return sum_of_integers3(n - 1, s + n)
 
n = int(input())
s = sum_of_integers3(n, 0)
print(s)
