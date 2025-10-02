def count_pos_neg(arr):
    counts = {"positive": 0, "negative": 0, "zero": 0}
    for x in arr:
        if x > 0:
            counts["positive"] += 1
        elif x < 0:
            counts["negative"] += 1
        else:
            counts["zero"] += 1
    return counts

def main():
    tests = [
        [1, -2, 3, 0, -5, 6],
        [-1, -2, -3],
        [0, 0, 0],
        [10, 20, 30]
    ]
    for i, arr in enumerate(tests, 1):
        print(f"Test #{i} Input:", arr)
        print("Counts:", count_pos_neg(arr))
        print("---")

if __name__ == "__main__":
    main()
