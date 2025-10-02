def main():
    student = {"name": "Satyajit", "uid": "25MAI14011", "marks": [95, 92, 96]}
    print("Student dict (literal):", student)
    emp = dict([("id", 14011), ("name", "Satyajit"), ("dept", "AI")])
    print("Employee dict (constructor):", emp)
    settings = {"volume": 7, ("screen", "res"): "1920x1080", "prefs": {"theme": "dark", "autosave": True}}
    print("Settings (mixed keys):", settings)
    print("Student name (index):", student["name"])
    print("Employee dept (get):", emp.get("dept"))
    print("Nonexistent key with default:", emp.get("salary", "Not Defined"))

if __name__ == "__main__":
    main()
