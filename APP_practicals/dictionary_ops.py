def demo_dict_ops():
    data = {"a": 1, "b": 2, "c": 3}
    print("Initial:", data)
    print("Traverse keys:")
    for k in data:
        print(k, "->", data[k])
    print("\nTraverse items:")
    for k, v in data.items():
        print(k, v)
    data["d"] = 4
    print("\nAfter add d:", data)
    data["b"] = 20
    print("After update b:", data)
    data.update({"e": 5, "a": 10})
    print("After update dict:", data)
    val = data.pop("c")
    print("Popped c ->", val, ", now:", data)
    del data["d"]
    print("After del d:", data)
    x = data.setdefault("f", 100)
    print("After setdefault f:", data, "returned:", x)
    data.clear()
    print("After clear:", data)

if __name__ == "__main__":
    demo_dict_ops()
