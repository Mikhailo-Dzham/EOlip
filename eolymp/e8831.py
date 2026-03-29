x, y = [float(i) for i in input().split()]
result = 2 * (x ** 2) - (4 * x * y) + (3 * y ** 2) + ((x + y) / 7)
print(f"{result:.3f}")