from typing import Type, Dict
from software_design_HW1.src.domain.animals.herbivores import Monkey, Rabbit
from software_design_HW1.src.domain.animals.predators import Tiger, Wolf
from software_design_HW1.src.domain.things import Computer, Table

ANIMAL_CLASSES: Dict[str, Type] = {
    "monkey": Monkey,
    "rabbit": Rabbit,
    "tiger": Tiger,
    "wolf": Wolf,
}
THING_CLASSES: Dict[str, Type] = {
    "computer": Computer,
    "table": Table,
}
