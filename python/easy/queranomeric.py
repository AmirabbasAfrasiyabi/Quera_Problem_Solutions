from typing import List

def queranumeric(order: List[str], words: List[str]) -> List[str]:
    """
    order: list of unique characters specifying priority (first = highest priority)
    words: list of strings to sort according to the queranumeric order
    returns: new list of words sorted by the custom order
    """
    base = len(order)

    rank = {ch: i for i, ch in enumerate(order)}

    def key_func(word: str):

        return tuple(rank.get(ch, base + ord(ch)) for ch in word)

    return sorted(words, key=key_func)