from software_design_HW1.src.domain.animals.animals import Animal
from software_design_HW1.src.domain.protocols import VetClinic


class SimpleVetClinic(VetClinic):
    def is_healthy(self, animal: Animal) -> bool:
        return animal.health_bar >= 5
