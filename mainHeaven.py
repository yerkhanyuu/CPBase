"""
mainHeaven.py — ГЛАВНЫЙ ФАЙЛ. Запускать нужно его.

Показывает на дисплее хаба номер заезда:
  ЛЕВАЯ / ПРАВАЯ кнопка — выбрать заезд, ЦЕНТР — запустить.
Выбранный номер запоминается в памяти хаба.
"""
from pybricks.parameters import Button, Color
from pybricks.tools import wait, Matrix

from Base import *
from Heaven_1 import run_1
from Heaven_2 import run_2
from Heaven_3 import run_3
from Heaven_4 import run_4
from Heaven_5 import run_5
from Heaven_6 import run_6
from Heaven_7 import run_7
from Heaven_8 import run_8
from Heaven_9 import run_9

# ==============================================================================
# ИКОНКИ ДЛЯ ДИСПЛЕЯ ХАБА (цифры заездов, «поехали», «готово»)
# ==============================================================================
DIGITS_5x3 = [
    # 1
    Matrix([
        [0, 0, 100, 0, 0],
        [0, 100, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [0, 0, 100, 0, 0],
        [0, 100, 100, 100, 0]
    ]),
    # 2
    Matrix([
        [0, 100, 100, 100, 0],
        [0, 0, 0, 100, 0],
        [0, 100, 100, 100, 0],
        [0, 100, 0, 0, 0],
        [0, 100, 100, 100, 0]
    ]),
    # 3
    Matrix([
        [0, 100, 100, 100, 0 ],
        [0, 0, 0, 100, 0],
        [0, 100, 100, 100, 0],
        [0, 0, 0, 100, 0],
        [0, 100, 100, 100, 0]
    ]),
    # 4
    Matrix([
        [0, 100, 0, 100, 0],
        [0, 100, 0, 100, 0],
        [0, 100, 100, 100, 0],
        [0, 0, 0, 100, 0],
        [0, 0, 0, 100, 0]
    ]),
    # 5
    Matrix([
        [0, 100, 100, 100, 0],
        [0, 100, 0, 0, 0],
        [0, 100, 100, 100, 0],
        [0, 0, 0, 100, 0],
        [0, 100, 100, 100, 0]
    ]),
    # 6
    Matrix([
        [0, 100, 100, 100, 0],
        [0, 100, 0, 0, 0],
        [0, 100, 100, 100, 0],
        [0, 100, 0, 100, 0],
        [0, 100, 100, 100, 0]
    ]),
    # 7
    Matrix([
        [0, 100, 100, 100, 0],
        [0, 0, 0, 100, 0],
        [0, 0, 0, 100, 0],
        [0, 0, 0, 100, 0],
        [0, 0, 0, 100, 0]
    ]),
    # 8
    Matrix([
        [0, 100, 100, 100, 0],
        [0, 100, 0, 100, 0],
        [0, 100, 100, 100, 0],
        [0, 100, 0, 100, 0],
        [0, 100, 100, 100, 0]
    ]),
    # 9
    Matrix([
        [0, 100, 100, 100, 0],
        [0, 100, 0, 100, 0],
        [0, 100, 100, 100, 0],
        [0, 0, 0, 100, 0],
        [0, 100, 100, 100, 0]
    ])
]

ICON_GO = Matrix([
    [0, 100, 0, 0, 0],
    [0, 100, 100, 0, 0],
    [0, 100, 100, 100, 0],
    [0, 100, 100, 0, 0],
    [0, 100, 0, 0, 0]
])

ICON_OK = Matrix([
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 100],
    [0, 0, 0, 100, 0],
    [100, 0, 100, 0, 0],
    [0, 100, 0, 0, 0]
])

runs = [run_1, run_2, run_3, run_4, run_5, run_6, run_7, run_8, run_9]

# ==============================================================================
# ИНТЕРАКТИВНОЕ МЕНЮ ЗАЕЗДОВ
# ==============================================================================
def run_menu():
    max_index = len(runs) - 1

    # ИЗМЕНЕНИЕ 1: Убрали чтение старой памяти. Теперь при запуске программы 
    # всегда будет выбираться индекс 0 (что соответствует цифре 1)
    current_index = 0

    hub.light.on(Color.BLUE)

    while True:
        hub.display.icon(DIGITS_5x3[current_index])

        pressed = set()
        while not pressed:
            pressed = hub.buttons.pressed()
            wait(30)

        # ВЛЕВО: предыдущий заезд
        if Button.LEFT in pressed:
            current_index = (current_index - 1) % len(runs)
            try:
                hub.system.storage(0, bytes([current_index]))
            except Exception:
                pass
            while any(hub.buttons.pressed()):
                wait(10)

        # ВПРАВО: следующий заезд
        elif Button.RIGHT in pressed:
            current_index = (current_index + 1) % len(runs)
            try:
                hub.system.storage(0, bytes([current_index]))
            except Exception:
                pass
            while any(hub.buttons.pressed()):
                wait(10)

        # ЦЕНТР: запуск выбранного заезда
        elif Button.CENTER in pressed:
            while any(hub.buttons.pressed()):
                wait(10)

            set_heading(0)

            hub.light.on(Color.MAGENTA)
            hub.display.icon(ICON_GO)
            wait(100)

            try:
                runs[current_index]()
                stop_motors()
                hub.light.on(Color.GREEN)
                hub.display.icon(ICON_OK)
                wait(200)

                # ИЗМЕНЕНИЕ 2: Автоматический переход к следующему заезду после финиша
                current_index = (current_index + 1) % len(runs)
                try:
                    # Записываем новый номер в память
                    hub.system.storage(0, bytes([current_index]))
                except Exception:
                    pass

            except Exception as e:
                stop_motors()
                print("ОШИБКА В ЗАЕЗДЕ:", e)
                hub.light.on(Color.RED)
                wait(1000)

            hub.light.on(Color.BLUE)
# ==============================================================================
# ТОЧКА ВХОДА
# ==============================================================================
if __name__ == "__main__":
    run_menu()
