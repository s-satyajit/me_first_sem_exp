KB = {
    ("A", "B"): "C",
    ("C",): "D",
    ("D", "E"): "F"
}
facts = {"A", "B", "E"}

def forward_chaining(KB, facts, goal):
    while goal not in facts:
        added = False
        for premises, conclusion in KB.items():
            if set(premises).issubset(facts) and conclusion not in facts:
                facts.add(conclusion)
                print("Derived:", conclusion)
                added = True
        if not added:
            return False
    return True

def backward_chaining(KB, facts, goal):
    if goal in facts:
        return True
    for premises, conclusion in KB.items():
        if conclusion == goal:
            return all(backward_chaining(KB, facts, p) for p in premises)
    return False

print("Forward:", forward_chaining(KB, facts.copy(), "F"))
print("Backward:", backward_chaining(KB, facts.copy(), "F"))
