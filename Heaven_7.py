"""Heaven_7.py — заезд №7."""
from Base import *


def run_7():
    """Заезд №7"""
    print_battery()

    set_heading(0)
    drive(300, start_speed=30, max_speed=60, end_speed=60, decel_mm=100, accel_rate=5)
    right_att_run(80, 180)
    wait(500)
    drive(-20, start_speed=30, max_speed=60, end_speed=30, decel_mm=0, accel_rate=5)
    drive(20, start_speed=30, max_speed=60, end_speed=30, decel_mm=0, accel_rate=5)
    drive(-20, start_speed=30, max_speed=60, end_speed=30, decel_mm=0, accel_rate=5)
    drive(20, start_speed=30, max_speed=60, end_speed=30, decel_mm=0, accel_rate=5)
    drive(-300, start_speed=30, max_speed=60, end_speed=30, decel_mm=100, accel_rate=5)


# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_7()
