def show_ranges():
    print("range(stop) -> range(5):", list(range(5)))
    print("range(start, stop) -> range(2, 7):", list(range(2, 7)))
    print("range(start, stop, step) -> range(1, 10, 2):", list(range(1, 10, 2)))
    print("Negative step -> range(5, 0, -1):", list(range(5, 0, -1)))

def iterate_example():
    print("\nIterate with for-loop:")
    for i in range(3):
        print(" i =", i)
    r = range(2, 10, 3)
    print("\nrange object r:", r)
    print("Length of r (count of elements):", len(r))
    print("Elements of r via iteration:", [x for x in r])

def main():
    print("=== range() function demo ===\n")
    show_ranges()
    iterate_example()
    print("\n=== End ===")

if __name__ == "__main__":
    main()