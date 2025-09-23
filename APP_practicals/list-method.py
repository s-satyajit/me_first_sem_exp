def demo_list_methods():
    a = [3, 1, 4]
    print("Initial:", a)

    a.append(5)
    print("append(5):", a)

    a.extend([9, 2])
    print("extend([9,2]):", a)

    a.insert(1, 8)
    print("insert(1,8):", a)

    a.remove(4)
    print("remove(4):", a)

    last = a.pop()
    print("pop() ->", last, ", list now:", a)
    idx_item = a.pop(2)
    print("pop(2) ->", idx_item, ", list now:", a)

    print("index of 3:", a.index(3))
    print("count of 3:", a.count(3))

    b = a.copy()
    print("copy b:", b)

    a.reverse()
    print("reverse():", a)
    a.sort()
    print("sort():", a)

    b.clear()
    print("clear() b ->", b)

if __name__ == "__main__":
    demo_list_methods()
