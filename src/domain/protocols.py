from __future__ import annotations

from typing import Protocol, Optional, Iterable, TYPE_CHECKING

if TYPE_CHECKING:
    from software_design_HW1.src.domain.animals.animals import Animal
    from things import Thing


class IAlive(Protocol):
    food_kg_per_day: int
    name: str


class IInventory(Protocol):
    number: int


class AnimalRepository(Protocol):
    def add(self, animal: Animal) -> None: ...

    def list(self) -> Iterable[Animal]: ...

    def get(self, number: int) -> Optional[Animal]: ...


class ThingRepository(Protocol):
    def add(self, thing: Thing) -> None: ...

    def list(self) -> Iterable[Thing]: ...

    def get(self, number: int) -> Thing: ...


class VetClinic(Protocol):
    def is_healthy(self, animal: Animal) -> bool: ...
