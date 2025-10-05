from dataclasses import dataclass
from software_design_HW1.src.domain.protocols import IInventory


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
