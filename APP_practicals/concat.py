def concat_manual_plus(s1: str, s2: str) -> str:
    res = ""
    for ch in s1:
        res += ch
    for ch in s2:
        res += ch
    return res

def concat_manual_list(s1: str, s2: str) -> str:
    parts = []
    for ch in s1:
        parts.append(ch)
    for ch in s2:
        parts.append(ch)
    return "".join(parts)

def main():
    tests = [
        ("Hello", "World"),
        ("", "abc"),
        ("Data", ""),
        ("A", "B"),
    ]
    for a, b in tests:
        print("s1:", repr(a), "s2:", repr(b))
        print("Concat (plain loop):", concat_manual_plus(a, b))
        print("Concat (list+join)  :", concat_manual_list(a, b))
        print("---")

if __name__ == "__main__":
    main()
