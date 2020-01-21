from typing import Any, List, Sequence

from .StalinList import StalinList

def sort(seq: Sequence[Any]) -> Sequence[Any]:
    sl = StalinList(seq)
    sl.sort()
    return seq.__class__(sl)
