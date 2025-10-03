from ..domain.animals import Animal
from ..domain.protocols import VetClinic


class SimpleVetClinic(VetClinic):
    def is_healthy(self, animal: Animal) -> bool:
        return animal.health_bar >= 7
