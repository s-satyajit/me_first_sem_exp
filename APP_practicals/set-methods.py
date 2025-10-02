def demo_set_methods():
    s1 = {1, 2, 3}
    s2 = set([3, 4, 5])
    print("s1:", s1)
    print("s2:", s2)
    s1.add(4)
    print("s1 after add(4):", s1)
    s1.discard(10)
    print("s1 after discard(10):", s1)
    try:
        s2.remove(5)
        print("s2 after remove(5):", s2)
    except KeyError:
        print("remove raised KeyError for missing element")
    popped = s1.pop()
    print("popped from s1:", popped, "now s1:", s1)
    print("union:", s1.union(s2))
    print("intersection:", s1.intersection(s2))
    print("difference s1 - s2:", s1.difference(s2))
    print("symmetric_difference:", s1.symmetric_difference(s2))
    print("is s1 subset of s2?", s1.issubset(s2))
    print("is s2 superset of s1?", s2.issuperset(s1))
    s3 = s2.copy()
    print("copy s3:", s3)
    s3.clear()
    print("after clear s3:", s3)

if __name__ == "__main__":
    demo_set_methods()
