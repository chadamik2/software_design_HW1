# Описание проекта
ERP система для московского зоопарка. Первое домашнее задание в рамках курса "Конструирование программного обеспечения". Код написан на языке Python.


## Инструкция по запуску проекта
1. Установите Python 3.12 и git
2. Склонируйте репозиторий 
Windows:
```
git clone https://github.com/chadamik2/software_design_HW1.git
cd software_design_HW1
```
macOS:
```
git clone https://github.com/chadamik2/software_design_HW1.git
cd software_design_HW1
```
3. Создать и активировать виртуальное окружение
Windows:
```
py -3.12 -m venv .venv
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
.\.venv\Scripts\Activate.ps1
```
macOS:
```
python3.12 -m venv .venv
source .venv/bin/activate
```
4. Запустить приложение 
```
cd ..
python -m software_design_HW1.src.app.cli
```
5. Включить тесты
```
pip install pytest pytest-cov
$env:PYTHONPATH = (Get-Item .).FullName
pytest software_design_HW1/tests -q --maxfail=1 --disable-warnings --cov=software_design_HW1/src
``` 