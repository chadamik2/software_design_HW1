from typing import Optional


def read_int(text: str, min_v: Optional[int] = None, max_v: Optional[int] = None) -> Optional[int]:
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


def read_non_empty(text: str) -> str:
    while True:
        s = input(text).strip()
        if s:
            return s
        print("Поле не может быть пустым.")
