def demo_tuple_ops():
    t = (5, 1, 7, 3, 3)
    print("Tuple t:", t)
    print("len(t):", len(t))
    print("max(t):", max(t))
    print("min(t):", min(t))
    print("sum(t):", sum(t))
    print("t.count(3):", t.count(3))
    print("t.index(7):", t.index(7))
    t2 = (10, 20)
    print("t + t2 ->", t + t2)
    print("t * 2 ->", t * 2)
    a, b, *rest = t
    print("Unpacked a,b,rest ->", a, b, rest)
    nested = (1, (2, 3), (4, (5, 6)))
    print("Nested:", nested)
    print("nested[2][1][0] ->", nested[2][1][0])

if __name__ == "__main__":
    demo_tuple_ops()
