def demo_index_slice():
    t = ('a', 'b', 'c', 'd', 'e')
    print("Tuple:", t)
    print("t[0] ->", t[0])
    print("t[-1] ->", t[-1])
    print("t[1:4] ->", t[1:4])
    print("t[::2] ->", t[::2])
    nested = (0, ('x','y','z'), 9)
    print("nested[1][2] ->", nested[1][2])
    s = t[2:]
    print("t[2:] is tuple?", isinstance(s, tuple), "value:", s)
    try:
        t[1] = 'B'
    except TypeError as e:
        print("Attempting t[1] = 'B' -> TypeError:", e)

if __name__ == "__main__":
    demo_index_slice()
