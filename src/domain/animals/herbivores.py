from dataclasses import dataclass
from software_design_HW1.src.domain.animals.animals import Animal


@dataclass(slots=True)
class Herbivore(Animal):
    kindness: int

    def is_contact(self):
        return self.kindness >= 5


@dataclass(slots=True)
class Monkey(Herbivore):
    pass


@dataclass(slots=True)
class Rabbit(Herbivore):
    pass
