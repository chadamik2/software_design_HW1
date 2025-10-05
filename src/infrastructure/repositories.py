from software_design_HW1.src.domain.protocols import AnimalRepository, ThingRepository
from software_design_HW1.src.domain.animals.animals import Animal
from software_design_HW1.src.domain.things import Thing
from typing import Dict, Iterable, Optional


class InMemoryAnimalRepository(AnimalRepository):
    def __init__(self) -> None:
        self._by_number: Dict[int, Animal] = {}

    def add(self, animal: Animal) -> None:
        self._by_number[animal.number] = animal

    def list(self) -> Iterable[Animal]:
        return self._by_number.values()

    def get(self, animal_number: int) -> Optional[Animal]:
        return self._by_number.get(animal_number)


class InMemoryThingRepository(ThingRepository):
    def __init__(self) -> None:
        self._by_number: Dict[int, Thing] = {}

    def add(self, thing: Thing) -> None:
        self._by_number[thing.number] = thing

    def list(self) -> Iterable[Thing]:
        return self._by_number.values()

    def get(self, thing_number: int) -> Optional[Thing]:
        return self._by_number.get(thing_number)
