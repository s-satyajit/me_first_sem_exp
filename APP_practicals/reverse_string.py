def reverse_manual(s: str) -> str:
    rev = ""
    i = len(s) - 1
    while i >= 0:
        rev += s[i]
        i -= 1
    return rev

def reverse_with_list(s: str) -> str:
    chars = []
    for i in range(len(s) - 1, -1, -1):
        chars.append(s[i])
    return "".join(chars)

def main():
    inputs = ["hello", "A", "", "racecar", "Advanced"]
    for s in inputs:
        print("Input :", repr(s))
        print("Reversed (manual concat):", reverse_manual(s))
        print("Reversed (list+join)  :", reverse_with_list(s))
        print("---")

if __name__ == "__main__":
    main()
