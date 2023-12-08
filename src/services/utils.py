from collections.abc import Iterable


def calculate_tax(data: Iterable) -> int:
    return int(sum(map(lambda x: x * 100, data)) * 0.87)
