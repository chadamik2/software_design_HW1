from __future__ import annotations


class InventoryNumberRegistry:
    def __init__(self) -> None:
        self._used: set[int] = set()

    def is_free(self, number: int) -> bool:
        return number not in self._used

    def reserve(self, number: int) -> None:
        if number in self._used:
            raise ValueError(f"Инвентарный номер {number} уже занят")
        self._used.add(number)

    def release(self, number: int) -> None:
        self._used.discard(number)
