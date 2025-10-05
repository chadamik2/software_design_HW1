from dataclasses import dataclass
from software_design_HW1.src.domain.protocols import IInventory, IAlive


@dataclass(slots=True)
class Animal(IAlive, IInventory):
    number: int
    food_kg_per_day: int
    name: str
    health_bar: int
