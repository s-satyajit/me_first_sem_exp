from collections import Counter

def compare_lists(a, b):
    print("A:", a)
    print("B:", b)
    print("A == B ?", a == b)
    print("A != B ?", a != b)
    try:
        print("A < B ?", a < b)
        print("A > B ?", a > b)
    except TypeError:
        print("Lexicographic comparison not supported for these lists' element types")
    print("Same elements (sorted)?", sorted(a) == sorted(b))
    print("Same multiset (Counter)?", Counter(a) == Counter(b))
    min_len = min(len(a), len(b))
    eq_positions = [i for i in range(min_len) if a[i] == b[i]]
    print("Positions with equal elements (common index):", eq_positions)
    print("Unique elements of A subset of B?", set(a).issubset(set(b)))
    print("-" * 40)

def main():
    compare_lists([1,2,3], [1,2,3])
    compare_lists([1,3,2], [1,2,3])
    compare_lists([1,2,2], [2,1,2])
    compare_lists(["a", "b"], ["a", "b", "c"])

if __name__ == "__main__":
    main()
