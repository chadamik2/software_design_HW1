from software_design_HW1.src.domain.animals.herbivores import Herbivore
from software_design_HW1.src.services.services import AnimalService, ThingService
from software_design_HW1.src.data.data import ANIMAL_CLASSES, THING_CLASSES
from typing import Protocol, Optional
from input_processing import read_int, read_non_empty


class MenuAction(Protocol):
    key: str
    title: str

    def run(self) -> Optional[bool]: ...


class AddAnimalAction(MenuAction):
    key = "1"
    title = "Добавить животное"

    def __init__(self, animal_service: AnimalService) -> None:
        self.animal_service = animal_service

    def run(self) -> None:
        name = read_non_empty("Имя животного: ")
        print(f"Доступные виды: {', '.join(ANIMAL_CLASSES.keys())}")
        kind_key = read_non_empty("Вид: ").lower()
        if kind_key not in ANIMAL_CLASSES:
            print("Неизвестный вид.")
            return
        number = read_int("Инвентарный номер: ", min_v=0)
        food = read_int("Еда (кг/день): ", min_v=0)
        health = read_int("Здоровье (0-10): ", min_v=0, max_v=10)
        specie = ANIMAL_CLASSES[kind_key]
        if issubclass(specie, Herbivore):
            kindness = read_int("Доброта (0-10): ", min_v=0, max_v=10)
            animal = specie(number, food, name, health, kindness)
        else:
            animal = specie(number, food, name, health)
        try:
            if self.animal_service.add_animal(animal):
                print(f"{name} принят в зоопарк.")
            else:
                print(f"{name} не прошёл ветеринарный осмотр.")
        except ValueError as e:
            print(e)


class AddThingAction:
    key = "2"
    title = "Добавить вещь"

    def __init__(self, thing_service: ThingService) -> None:
        self.thing_service = thing_service

    def run(self) -> None:
        name = read_non_empty("Название вещи: ")
        print(f"Доступные типы: {', '.join(THING_CLASSES.keys())}")
        kind_key = read_non_empty("Тип: ").lower()
        if kind_key not in THING_CLASSES:
            print("Неизвестный тип.")
            return
        number = read_int("Инвентарный номер: ", min_v=0)
        cls = THING_CLASSES[kind_key]
        try:
            self.thing_service.add_thing(cls(number, name))
            print("Вещь добавлена.")
        except ValueError as e:
            print(e)


class ListAnimalsAction:
    key = "3"
    title = "Показать всех животных"

    def __init__(self, animal_service: AnimalService) -> None:
        self.animal_service = animal_service

    def run(self) -> None:
        animals = list(self.animal_service.list_animals())
        if not animals:
            print("Нет животных.")
            return
        for a in animals:
            extra = ""
            if hasattr(a, "kindness"):
                extra = f", доброта {getattr(a, 'kindness')}"
            print(f"{a.number}: {a.name} ({type(a).__name__}), еда {a.food_kg_per_day} кг/день{extra}")


class ListThingsAction:
    key = "4"
    title = "Показать все вещи"

    def __init__(self, thing_service: ThingService) -> None:
        self.thing_service = thing_service

    def run(self) -> None:
        things = list(self.thing_service.list_things())
        if not things:
            print("Нет вещей.")
            return
        for t in things:
            print(f"{t.number}: {t.name} ({type(t).__name__})")


class TotalFoodAction:
    key = "5"
    title = "Сколько всего еды нужно в день?"

    def __init__(self, animal_service: AnimalService) -> None:
        self.animal_service = animal_service

    def run(self) -> None:
        print(f"Всего нужно {self.animal_service.total_food_kg_per_day()} кг еды в день.")


class ContactZooAction:
    key = "6"
    title = "Животные для контактного зоопарка"

    def __init__(self, animal_service: AnimalService) -> None:
        self.animal_service = animal_service

    def run(self) -> None:
        lst = self.animal_service.list_animals_for_the_contact_zoo()
        if not lst:
            print("Пока никого нет.")
            return
        for a in lst:
            print(f"{a.number}: {a.name} ({type(a).__name__}), доброта {a.kindness}")


class ExitAction:
    key = "0"
    title = "Выход"

    def run(self) -> bool:
        print("До свидания!")
        return True
