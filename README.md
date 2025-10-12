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
- macOS/Linux:
```
git clone https://github.com/chadamik2/software_design_HW1.git
cd software_design_HW1
```
3. Создать и активировать виртуальное окружение
- Windows - PowerShell:
```
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
- Windows - cmd.exe
```
py -3.12 -m venv .venv
.\.venv\Scripts\Activate.ps1
```
- macOS/Linux:
```
python3.12 -m venv .venv
source .venv/bin/activate
```
4. Запустить приложение
Если вы находитесь в папке проекта
```
cd ..
```
Запуск
```
python -m software_design_HW1.src.app.cli
```
5. Установка корня(для тестов)
Если вы находитесь в папке проекта
```
cd ..
```
```
pip install pytest pytest-cov
```
- Windows - PowerShell
```
$env:PYTHONPATH = (Get-Item .).FullName
```
- Windows - cmd.exe
```
set PYTHONPATH=.
```
- macOS/Linux
```
export PYTHONPATH=.
```
6. Запуск тестов
```
pytest software_design_HW1/tests -q --maxfail=1 --disable-warnings --cov=software_design_HW1/src
```
### Альтернатива - запуск в PyCharm
1. Установите Python 3.12 и git
2. Склонируйте репозиторий 
- Windows:
```
git clone https://github.com/chadamik2/software_design_HW1.git
cd software_design_HW1
```
- macOS/Linux:
```
git clone https://github.com/chadamik2/software_design_HW1.git
cd software_design_HW1
```
#### Открыть проект
1. **File → Open…** → выберите папку репозитория `software_design_HW1`.
2. Дождитесь индексации проекта.

#### Настроить интерпретатор (виртуальное окружение)

1. **File → Settings → Project → Python Interpreter**
2. Нажмите **⚙ → Add… → Add Local Interpreter → Virtualenv**.
3. Выберите существующее `.venv` в корне проекта или создайте новое.
4. Примените настройки (OK).


#### Запуск приложения

**Run → Edit Configurations… → + → Python** и заполните поля:

* **Name:** `Zoo CLI`
* **Run:** `Module name`
* **Module name:**

  ```
  software_design_HW1/src/app/cli.py
  ```
* **Working directory:** (родитель папки проекта)

  ```
  $PROJECT_DIR$/..
  ```
* **Environment variables:** добавьте

  ```
  PYTHONPATH=$PROJECT_DIR$/..
  ```
* ☑ **Add content roots to PYTHONPATH**
* ☑ **Add source roots to PYTHONPATH**
* **Python interpreter:** выберите ваше `.venv`

Сохраните и запускайте зелёной кнопкой ▶.

#### Запуск тестов в PyCharm

1. **Run → Edit Configurations… → + → pytest**.
2. Поля:

   * **Name:** `Tests`
     ```
     $PROJECT_DIR$/../software_design_HW1/tests
     ```
   * **Working directory:**

     ```
     $PROJECT_DIR$/..
     ```
   * **Environment variables:**

     ```
     PYTHONPATH=$PROJECT_DIR$/..
     ```
   * **Additional Arguments:**

     ```
     -q --maxfail=1 --disable-warnings --cov=software_design_HW1/src
     ```
   * ☑ **Add content roots…**, ☑ **Add source roots…**
   * **Interpreter:** ваше `.venv`

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
│ └── services.py
│
| ├── container.py
|
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
