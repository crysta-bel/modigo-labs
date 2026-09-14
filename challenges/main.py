def dedupe_preserve_order(items):
    # TODO: use a set to track seen values while building a new list
    # that preserves the original order of first appearances
    seen = set()
    result = []
    for item in items:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result