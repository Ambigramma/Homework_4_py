def blueberry():
    n = int(input())
    lst = list()
    for i in range(n):
        lst.append(int(i+1))
    blueberry = list()
    for i in range(len(lst) - 1 ):
        blueberry.append(lst[i-1] + lst[i] + lst[i+1])
    blueberry.append(lst[-2] + lst[-1] + lst[0])
    print(max(blueberry))

    