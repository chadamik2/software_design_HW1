from typing import Protocol, Dict, Type, List, Optional
from software_design_HW1.src.container import Container
from software_design_HW1.src.domain.animals import Monkey, Rabbit, Tiger, Wolf, Herbivore, Animal
from software_design_HW1.src.domain.things import Computer, Table, Thing
from software_design_HW1.src.services.services import AnimalService, ThingService

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


def _read_int(text: str, min_v: Optional[int] = None, max_v: Optional[int] = None) -> Optional[int]:
    while True:
        try:
            val = int(input(text))
            if min_v is not None and val < min_v:
                print(f"Значение должно быть ≥ {min_v}")
                continue
            if max_v is not None and val > max_v:
                print(f"Значение должно быть ≤ {max_v}")
                continue
            return val
        except ValueError:
            print("Введите целое число.")


def _read_non_empty(text: str) -> str:
    while True:
        s = input(text).strip()
        if s:
            return s
        print("Поле не может быть пустым.")


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
        name = _read_non_empty("Имя животного: ")
        print(f"Доступные виды: {', '.join(ANIMAL_CLASSES.keys())}")
        kind_key = _read_non_empty("Вид: ").lower()
        if kind_key not in ANIMAL_CLASSES:
            print("Неизвестный вид.")
            return
        number = _read_int("Инвентарный номер: ", min_v=0)
        food = _read_int("Еда (кг/день): ", min_v=0)
        health = _read_int("Здоровье (0-10): ", min_v=0, max_v=10)
        specie = ANIMAL_CLASSES[kind_key]
        if issubclass(specie, Herbivore):
            kindness = _read_int("Доброта (0-10): ", min_v=0, max_v=10)
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
        name = _read_non_empty("Название вещи: ")
        print(f"Доступные типы: {', '.join(THING_CLASSES.keys())}")
        kind_key = _read_non_empty("Тип: ").lower()
        if kind_key not in THING_CLASSES:
            print("Неизвестный тип.")
            return
        number = _read_int("Инвентарный номер: ", min_v=0)
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


def build_actions(c: Container) -> List[MenuAction]:
    animal_service = c.resolve("animal_service")
    thing_service = c.resolve("thing_service")
    return [
        AddAnimalAction(animal_service),
        AddThingAction(thing_service),
        ListAnimalsAction(animal_service),
        ListThingsAction(thing_service),
        TotalFoodAction(animal_service),
        ContactZooAction(animal_service),
        ExitAction(),
    ]


def pause(text="\nНажмите Enter для продолжения..."):
    input(text)


def main() -> None:
    container = Container()
    actions = build_actions(container)
    actions_by_key: Dict[str, MenuAction] = {a.key: a for a in actions}
    while True:
        print("\n=== Московский Зоопарк ===")
        for a in actions:
            print(f"{a.key}. {a.title}")
        choice = input("Выберите пункт меню: ").strip()
        action = actions_by_key.get(choice)
        if not action:
            print("Неверный выбор.")
            continue
        should_exit = action.run()
        if should_exit:
            break
        pause()


if __name__ == "__main__":
    main()
