from rapidfuzz import fuzz

SIM_THRESHOLD = 80   # 0-100 Levenshtein similarity (80 ≈ ≤20 % edits)

SYNONYMS = {
    "Picanha Steak":        ["steak", "picanha", "picanha steak"],
    "Spaghetti Bolognese":  ["spaghetti", "spaghetti bolognese"],
    "French Fries":         ["french fries", "fries"],
    "Fettucine Carbonara":  ["fettucine", "carbonara", "fettucine carbonara"],
    "Grilled Salmon":       ["grilled salmon", "salmon"],
    "Chocolate Brownie":    ["brownie", "chocolate brownie"],
    "Iced Coffee":          ["coffee", "iced coffee"],
    "Iced Tea":             ["iced tea", "tea"],
}

_LOOKUP = [
    (canon, syn.lower()) for canon, syns in SYNONYMS.items() for syn in syns
]

def extract_mentions(text: str) -> list[str]:
    txt = text.lower()
    found = set()

    for canon, syn in _LOOKUP:
        if canon in found:
            continue

        if syn in txt:
            found.add(canon)
            continue

        if fuzz.partial_ratio(syn, txt) >= SIM_THRESHOLD:
            found.add(canon)

    return list(found)
