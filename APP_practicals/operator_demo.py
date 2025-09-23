def demo_arithmetic():
    a, b = 15, 4
    print("ARITHMETIC OPERATORS")
    print(f"a = {a}, b = {b}")
    print("Addition: a + b =", a + b)
    print("Subtraction: a - b =", a - b)
    print("Multiplication: a * b =", a * b)
    print("Division (float): a / b =", a / b)
    print("Floor division: a // b =", a // b)
    print("Modulus: a % b =", a % b)
    print("Exponent: a ** b =", a ** b)
    print()

def demo_assignment():
    x = 10
    print("ASSIGNMENT OPERATORS")
    print("Initial x =", x)
    x += 5; print("x += 5 ->", x)
    x *= 2; print("x *= 2 ->", x)
    x -= 3; print("x -= 3 ->", x)
    x //= 4; print("x //= 4 ->", x)
    x **= 2; print("x **= 2 ->", x)
    print()

def demo_comparison():
    a, b = 7, 12
    print("COMPARISON OPERATORS")
    print(f"a = {a}, b = {b}")
    print("a == b ->", a == b)
    print("a != b ->", a != b)
    print("a > b  ->", a > b)
    print("a < b  ->", a < b)
    print("a >= b ->", a >= b)
    print("a <= b ->", a <= b)
    print()

def demo_logical():
    p, q = True, False
    print("LOGICAL OPERATORS")
    print("p =", p, ", q =", q)
    print("p and q ->", p and q)
    print("p or q  ->", p or q)
    print("not p   ->", not p)
    print()

def demo_bitwise():
    x, y = 5, 3   # 5 -> 0101, 3 -> 0011
    print("BITWISE OPERATORS")
    print(f"x = {x} (bin {x:04b}), y = {y} (bin {y:04b})")
    print("x & y ->", x & y, "(AND)")
    print("x | y ->", x | y, "(OR)")
    print("x ^ y ->", x ^ y, "(XOR)")
    print("~x    ->", ~x, "(NOT)")
    print("x << 1 ->", x << 1)
    print("y >> 1 ->", y >> 1)
    print()

def demo_membership_identity():
    s = "python"
    lst1 = [1, 2, 3]
    lst2 = [1, 2, 3]
    lst3 = lst1
    print("MEMBERSHIP & IDENTITY OPERATORS")
    print("'y' in s ->", 'y' in s)
    print("'z' not in s ->", 'z' not in s)
    print("lst1 == lst2 ->", lst1 == lst2, "(values equal)")
    print("lst1 is lst2 ->", lst1 is lst2, "(different objects)")
    print("lst1 is lst3 ->", lst1 is lst3, "(same object reference)")
    print()

def demo_precedence():
    print("OPERATOR PRECEDENCE (example)")
    expr1 = 2 + 3 * 4
    expr2 = (2 + 3) * 4
    print("2 + 3 * 4 =", expr1, "-> multiplication before addition")
    print("(2 + 3) * 4 =", expr2, "-> parentheses change order")
    print()

def main():
    print("=== Operator Demonstration: Advanced Python Programming (Experiment 1b) ===\n")
    demo_arithmetic()
    demo_assignment()
    demo_comparison()
    demo_logical()
    demo_bitwise()
    demo_membership_identity()
    demo_precedence()
    print("=== End of Demonstration ===")

if __name__ == '__main__':
    main()
