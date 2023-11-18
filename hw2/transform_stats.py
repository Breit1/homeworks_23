"""Module with the helper that can transform object's statistics to percents."""

from functools import reduce
from typing import Optional


class SumCountEqualsZero(Exception):
    message: str = f'The sum of count from transform_stats cannot be equal a zero!'

    def __init__(self) -> None:
        super().__init__(self.message)


def transform_stats(stats: dict[str, int], sum_count: Optional[int] = None) -> dict[str, float]:
    """Transform object's statistics to percents.

    Args:
        stats (dict[str, int]): The dict that has object's statistics.
        sum_count (Optional[int]): \
            The sum of the count of every object's element,
            if it's a None, it will be calculated automatic.

    Returns:
        dict[str, float]: object's statistics in percents.
    """
    if sum_count is None:
        sum_count = reduce(lambda start, current: start + current[1], stats.items(), 0)

    if sum_count == 0:
        raise SumCountEqualsZero()

    return {
        key: (count / sum_count) * 100 for (key, count) in stats.items()
    }
