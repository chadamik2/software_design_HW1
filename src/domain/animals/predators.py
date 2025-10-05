from dataclasses import dataclass
from software_design_HW1.src.domain.animals.animals import Animal


@dataclass(slots=True)
class Predator(Animal):
    pass


@dataclass(slots=True)
class Tiger(Predator):
    pass


@dataclass(slots=True)
class Wolf(Predator):
    pass
