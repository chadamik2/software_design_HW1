from dataclasses import dataclass
from protocols import IInventory


@dataclass(slots=True)
class Thing(IInventory):
    number: int
    name: str


@dataclass(slots=True)
class Computer(Thing):
    pass


@dataclass(slots=True)
class Table(Thing):
    pass
