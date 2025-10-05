from typing import Callable, TypeVar, Dict, Any
from software_design_HW1.src.services.services import AnimalService, ThingService
from software_design_HW1.src.infrastructure.repositories import (InMemoryAnimalRepository,
                                                                 InMemoryThingRepository, )
from software_design_HW1.src.infrastructure.vetclinic import SimpleVetClinic
from software_design_HW1.src.domain.inventory import InventoryNumberRegistry

T = TypeVar("T")


class _SingletonProvider:
    def __init__(self, factory: Callable[[], T]) -> None:
        self.factory = factory
        self._instance: T | None = None

    def get(self) -> T:
        if self._instance is None:
            self._instance = self.factory()
        return self._instance


class Container:
    def __init__(self) -> None:
        self._providers: Dict[str, _SingletonProvider] = {}

        self.register_singleton("animal_repo", InMemoryAnimalRepository)
        self.register_singleton("thing_repo", InMemoryThingRepository)
        self.register_singleton("vet_clinic", SimpleVetClinic)
        self.register_singleton("number_registry", InventoryNumberRegistry)

        self.register_singleton("animal_service", lambda: AnimalService(repo=self.resolve("animal_repo"),
                                                                        clinic=self.resolve("vet_clinic"),
                                                                        number_registry=self.resolve(
                                                                            "number_registry")),

                                )
        self.register_singleton("thing_service", lambda: ThingService(repo=self.resolve("thing_repo"),
                                                                      number_registry=self.resolve(
                                                                          "number_registry")))

    def register_singleton(self, name: str, factory: Callable[[], Any]) -> None:
        self._providers[name] = _SingletonProvider(factory)

    def resolve(self, name: str) -> Any:
        provider = self._providers.get(name)
        if not provider:
            raise KeyError(f"Такой зависимости нет в контейнере")
        return provider.get()
