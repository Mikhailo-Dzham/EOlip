import sys
NMAX = 2*1000_00+3

def solve(array, n):
    suma = 0
    first_el = array[0]
    for el in array:
        suma+=int(el[-1])
    if suma % 2 == 0:
        print("YES")
        return
    pass


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    t = int(data[0])
    ind = 1
    array = [0] * NMAX
    for _ in range(t):
        n = int(data[ind])
        for i in range(n):
            array[i] = input()
        solve(array, n)
