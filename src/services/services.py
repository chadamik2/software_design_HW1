from software_design_HW1.src.domain.animals.animals import Animal
from software_design_HW1.src.domain.animals.herbivores import Herbivore
from software_design_HW1.src.domain.protocols import AnimalRepository, VetClinic, ThingRepository
from typing import List, Iterable
from software_design_HW1.src.domain.inventory import InventoryNumberRegistry

from software_design_HW1.src.domain.things import Thing


class AnimalService:
    def __init__(self, repo: AnimalRepository, clinic: VetClinic, number_registry: InventoryNumberRegistry):
        self.repo = repo
        self.clinic = clinic
        self.number_registry = number_registry

    def add_animal(self, animal: Animal) -> bool:
        if not self.clinic.is_healthy(animal):
            return False
        self.number_registry.reserve(animal.number)
        self.repo.add(animal)
        return True

    def list_animals(self) -> Iterable[Animal]:
        return self.repo.list()

    def get_animal(self, number: int) -> Animal:
        return self.repo.get(number)

    def total_food_kg_per_day(self) -> int:
        return sum(an.food_kg_per_day for an in self.repo.list())

    def list_animals_for_the_contact_zoo(self) -> List[Herbivore]:
        return [an for an in self.repo.list() if isinstance(an, Herbivore) and an.is_contact()]


class ThingService:
    def __init__(self, repo: ThingRepository, number_registry: InventoryNumberRegistry):
        self.repo = repo
        self.number_registry = number_registry

    def add_thing(self, thing: Thing) -> None:
        self.number_registry.reserve(thing.number)
        self.repo.add(thing)

    def list_things(self) -> Iterable[Thing]:
        return self.repo.list()

    def get_thing(self, number: int) -> Thing:
        return self.repo.get(number)
