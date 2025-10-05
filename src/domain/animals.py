from dataclasses import dataclass
from software_design_HW1.src.domain.protocols import IInventory, IAlive


@dataclass(slots=True)
class Animal(IAlive, IInventory):
    number: int
    food_kg_per_day: int
    name: str
    health_bar: int


@dataclass(slots=True)
class Herbivore(Animal):
    kindness: int

    def is_contact(self):
        return self.kindness >= 5


@dataclass(slots=True)
class Predator(Animal):
    pass


@dataclass(slots=True)
class Monkey(Herbivore):
    pass


@dataclass(slots=True)
class Rabbit(Herbivore):
    pass


@dataclass(slots=True)
class Tiger(Predator):
    pass


@dataclass(slots=True)
class Wolf(Predator):
    pass
