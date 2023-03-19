
def Foo():
    n = int(input())
    m = int(input())
    lst1 = set()
    lst2 = set()
    for i in range(n):
        lst1.add(int(input()))
    for i in range(m):
        lst2.add(int(input()))
    print(f'{lst1}')
    print(f'{lst2}')
    lst1.intersection_update(lst2)
    print(f'{lst1}')
    

Foo()