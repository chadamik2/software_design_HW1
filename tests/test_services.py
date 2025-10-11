import pytest

from software_design_HW1.src.domain.animals.herbivores import Rabbit
from software_design_HW1.src.domain.animals.predators import Tiger
from software_design_HW1.src.domain.things import Table
from software_design_HW1.src.infrastructure.repositories import InMemoryThingRepository, InMemoryAnimalRepository
from software_design_HW1.src.services.services import AnimalService, ThingService
from software_design_HW1.src.domain.inventory import InventoryNumberRegistry
from software_design_HW1.src.infrastructure.vetclinic import SimpleVetClinic


@pytest.fixture
def reg():
    return InventoryNumberRegistry()


@pytest.fixture
def animal_service(reg):
    return AnimalService(InMemoryAnimalRepository(), SimpleVetClinic(), reg)


@pytest.fixture
def thing_service(reg):
    return ThingService(InMemoryThingRepository, reg)


def test_add_animal(animal_service):
    a = Rabbit(1, 2, "Bunny", 8, 6)
    assert animal_service.add_animal(a) is True
    assert animal_service.get_animal(1) is a


def test_add_unhealthy_animal(animal_service):
    a = Rabbit(2, 2, "Bunny", 3, 3)
    assert animal_service.add_animal(a) is False
    assert animal_service.get_animal(2) is None


def test_total_food(animal_service):
    a = Rabbit(3, 2, "Bunny", 8, 6)
    b = Tiger(4, 4, "Denis", 9)
    animal_service.add_animal(a)
    animal_service.add_animal(b)
    assert animal_service.total_food_kg_per_day() == 6


def test_contact_zoo(animal_service):
    animal_service.add_animal(Rabbit(5, 2, "kind", 8, 6))
    animal_service.add_animal(Tiger(6, 4, "predator", 9))
    animal_service.add_animal(Rabbit(7, 2, "unkind", 8, 4))
    assert [a.name for a in animal_service.list_animals_for_the_contact_zoo()] == ["kind"]


def test_conflict_inventory_number(animal_service, thing_service):
    animal_service.add_animal(Rabbit(10, 2, "Bunny", 8, 6))
    with pytest.raises(ValueError):
        thing_service.add_thing(Table(10, "ShouldNotExist"))
