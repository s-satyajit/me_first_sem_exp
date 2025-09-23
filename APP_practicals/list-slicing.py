def demo_slicing():
    a = [0,1,2,3,4,5,6,7,8,9]
    print("Original:", a)
    print("a[2:6] ->", a[2:6])
    print("a[:5]  ->", a[:5])
    print("a[5:]  ->", a[5:])
    print("a[::2] ->", a[::2])
    print("a[1:8:3] ->", a[1:8:3])
    print("a[-3:] ->", a[-3:])
    print("a[::-1] ->", a[::-1], "(reversed)")
    b = a.copy()
    b[3:6] = [30,31]
    print("After b[3:6] = [30,31] ->", b)
    c = a[:]
    print("Copy via slice c == a ?", c == a, "and is c a ?", c is a)

if __name__ == "__main__":
    demo_slicing()
