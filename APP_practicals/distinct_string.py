def demo_string_methods(s):
    print("Original:", repr(s))
    print("Length:", len(s))
    print("Lower:", s.lower())
    print("Upper:", s.upper())
    print("Title:", s.title())
    print("Capitalize:", s.capitalize())
    print("Strip (trim):", repr(s.strip()))
    print("Replace 'AI'->'ML':", s.replace("AI", "ML"))
    print("Find 'day':", s.find("day"), "(returns -1 if not found)")
    try:
        print("Index 'day':", s.index("day"))
    except ValueError:
        print("Index 'day': not found (raises ValueError)")
    print("Count 'a':", s.count("a"))
    print("Starts with 'Adv':", s.startswith("Adv"))
    print("Ends with 'ing':", s.endswith("ing"))
    print("Is alpha:", s.isalpha())
    print("Is alnum:", s.isalnum())
    print("Split by spaces:", s.split())
    print("Join example (join with '-'):", "-".join(["advanced", "python"]))

def main():
    sample = "  Advanced Python Programming  "
    demo_string_methods(sample)
    s2 = "CS50"
    print("\nExtra checks on", s2)
    print("isdigit:", s2.isdigit(), "isalpha:", s2.isalpha(), "isalnum:", s2.isalnum())

if __name__ == "__main__":
    main()
