from software_design_HW1.src.container import Container
from software_design_HW1.src.app.menu_actions import *
from typing import List, Dict


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
