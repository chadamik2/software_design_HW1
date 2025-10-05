from software_design_HW1.src.infrastructure.vetclinic import SimpleVetClinic
from software_design_HW1.src.domain.animals.predators import Tiger
import pytest


def test_vet_clinic():
    clinic = SimpleVetClinic()
    tiger = Tiger(number=1, name="Bro", food_kg_per_day=12, health_bar=8)
    assert clinic.is_healthy(tiger) is True
    sick_tiger = Tiger(number=2, name="Who", food_kg_per_day=12, health_bar=4)
    assert clinic.is_healthy(sick_tiger) is False
