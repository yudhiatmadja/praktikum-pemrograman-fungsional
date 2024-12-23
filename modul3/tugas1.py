from functools import reduce

def aritmetika_geometri(a, d, r, n):
    if n == 1:
        return a  
    else:
        return (a + (n - 1) * d) * (r ** (n - 1))

def generate_series(a, d, r, n):
    return [aritmetika_geometri(a, d, r, i) for i in range(1, n + 1)]

def add(x, y):
    return x + y

def sum_series(a, d, r, n):
    series = generate_series(a, d, r, n)
    return reduce(add, series) 

a = 2  
d = 3  
r = 2  
n = 5  

series = generate_series(a, d, r, n)
total = sum_series(a, d, r, n)

print("Barisan Aritmetika-Geometri:", series)
print("Jumlah Deret:", total)
