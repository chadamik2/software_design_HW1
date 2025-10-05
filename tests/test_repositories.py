from software_design_HW1.src.infrastructure.repositories import InMemoryThingRepository, InMemoryAnimalRepository
from software_design_HW1.src.domain.animals.herbivores import Rabbit
from software_design_HW1.src.domain.things import Table
import pytest


def test_animal_repository():
    repo = InMemoryAnimalRepository()
    a = Rabbit(number=1, name="Denis", food_kg_per_day=20, health_bar=8, kindness=7)
    repo.add(a)
    assert list(repo.list()) == [a]
    assert repo.get(a.number) == a
    assert repo.get(1) == a
    assert repo.get(2) is None


def test_thing_repository():
    repo = InMemoryThingRepository()
    a = Table(number=1, name="SKD")
    repo.add(a)
    assert list(repo.list()) == [a]
    assert repo.get(a.number) == a
    assert repo.get(1) == a
    assert repo.get(2) is None
