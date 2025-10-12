# Описание проекта
ERP система для московского зоопарка.
- Учебный проект по конструированию ПО на Python.
- Цель: смоделировать домен зоопарка, соблюдая принципы SOLID и использовав DI-контейнер.
- Приложение ведёт учёт животных и инвентаря, учитывает потребление еды, и определяет животных для контактного зоопарка.

## Функции приложения
1. Добавить животное
2. Добавить вещь
3. Показать всех животных
4. Показать все вещи
5. Сколько всего еды нужно в день?
6. Животные для контактного зоопарка

## Инструкция по запуску проекта
1. Установите Python 3.12 и git
2. Склонируйте репозиторий 
- Windows:
```
git clone https://github.com/chadamik2/software_design_HW1.git
cd software_design_HW1
```
- macOS:
```
git clone https://github.com/chadamik2/software_design_HW1.git
cd software_design_HW1
```
3. Создать и активировать виртуальное окружение
- Windows:
```
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
- macOS:
```
python3.12 -m venv .venv
source .venv/bin/activate
```
4. Запустить приложение 
```
cd ..
python -m software_design_HW1.src.app.cli
```
5. Установка корня(для тестов)
```
pip install pytest pytest-cov
```
- Windows - PowerShell
```
$env:PYTHONPATH = (Get-Item .).FullName
```
- Windows - cmd.exe
```
set PYTHONPATH=..
```
- macOS/Linux
```
export PYTHONPATH=..
```
6. Запуск тестов
```
pytest software_design_HW1/tests -q --maxfail=1 --disable-warnings --cov=software_design_HW1/src
```
## Структура проекта:
```
software_design_HW1/
├── src/
│ ├── app/
│ │ ├── cli.py
│ │ ├── input_processing.py
│ │ └── menu_actions.py
│ │
│ ├── data/
│ │ └── data.py
│ │
│ ├── domain/
│ │ ├── animals/
│ │ │ ├── animals.py
│ │ │ ├── herbivores.py
│ │ │ └── predators.py
│ │ ├── inventory.py
│ │ ├── protocols.py
│ │ └── things.py
│ │
│ ├── infrastructure/
│ │ ├── repositories.py
│ │ └── vetclinic.py
│ │
│ └── services/
│ ├── container.py
│ └── services.py
│
├── tests/
│ ├── test_container.py
│ ├── test_inventory.py
│ ├── test_repositories.py
│ ├── test_services.py
│ └── test_vetclinic.py
│
├── .gitignore
└── README.md
```
## Применение ООП и SOLID
1. S - Single responsibility principle
   - domain/*.py — только модель/контракты домена.
   - infrastructure/repositories.py — только хранение в памяти.
   - services/services.py — бизнес-правила (приём животных, списки, суммирование).
   - app/cli.py — только ввод/вывод и оркестрация команд.
2. O - Open-closed principle
   - При добавлении новых животных, нужно унаследовать их от Herbivore/Predator.
   - При добавлении новых предметов, нужно унаследовать их от Thing.
   - При добавлении новых типов животных, нужно унаследовать их от Animal.
   - При добавлении новых пунктов меню, нужно добавить новый класс-команду.
3. L - Liskov substitution principle
   - Подклассы могут быть заменены базовыми классами.
   - Любой Herbivore/Predator подставим вместо Animal.
   - SimpleVetClinic подставима вместо VetClinic.
4. I - Interface segregation principle
   - IAlive - интерфейс для живых существ, содержащий поле food.
   - IInventory - интерфейс для живых существ и предметов, содержащий поле number.
5. D - Dependency inversion principle
   - services зависит от абстракций AnimalRepository, ThingRepository, VetClinic.
   - container.py связывает абстракции с реализациями.
   - В cli.py команды получают зависимости через конструктор, а не тянут их через контейнер.
  
## Архитектурные решения
  - DI-контейнер (container.py) управляет временем жизни объектов (singleton): общие in-memory репозитории и реестр номеров разделяются всеми сервисами.
  - Единый реестр инвентарных номеров (domain/inventory.py): гарантирует глобальную уникальность number для животных и вещей.
  - Бизнес-правило "животное принимаем только если здорово" реализовано в AnimalService.add_animal через VetClinic.
