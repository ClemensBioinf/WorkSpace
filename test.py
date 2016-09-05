str = "hallo"

def f(a):
    print(1, a)
    a += " Welt"
    print(2, a)
    return a

str = (f(str))
print(3, str)

print("-----")

a = [1,2,3,4]
del a[2]
print(a)

print("-----")

def func(a):
    b = 2
    c = 3
    def subfunc():
        nonlocal b
        print(b)
        print(c)
        print(a)

    subfunc()

func(1)