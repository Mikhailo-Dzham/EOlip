import sys
#NMAX = 2*1000_00+3

def solve(array, n):
    suma = 0
    first_el = array[0]
    for el in array:
        first_num = el[0]
        for num in el:
            if int(num) % 2 != int(first_num) % 2:
                print("YES")
                return

        suma+=int(el[-1])
    if suma % 2 == 0:
        print("YES")
        return
    print("No")
    return


if __name__ == "__main__":
    data = sys.stdin.read().split("\n")
    t = int(data[0])

    for test in range(1,t*2+1, 2):
        n = data[test]
        case = data[test+1].split()

        solve(case, n)



    # ind = 1
    # array = [0] * NMAX
    # for _ in range(t):
    #     n = int(data[ind])
    #     for i in range(n):
    #         array[i] = input()
    #     solve(array, n)
