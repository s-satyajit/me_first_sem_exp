procedure FORWARD_CHAINING(KB, facts, goal):
    while goal not in facts:
        applied = false
        for each rule in KB:
            if rule.premises ⊆ facts and rule.conclusion ∉ facts:
                add rule.conclusion to facts
                print("Derived:", rule.conclusion)
                applied = true
        if not applied:
            return "Goal not derivable"
    return "Goal derived"
