procedure BACKWARD_CHAINING(KB, facts, goal):
    if goal in facts:
        return true
    for each rule in KB:
        if rule.conclusion == goal:
            if all(BACKWARD_CHAINING(KB, facts, premise) for premise in rule.premises):
                return true
    return false
