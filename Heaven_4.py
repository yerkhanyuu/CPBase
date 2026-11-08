"""Heaven_4.py — заезд №4."""
from Base import *


def run_4():
    """Заезд №4"""
    print_battery()

    drive(250, start_speed=30, max_speed=60, end_speed=30, decel_mm=150, accel_rate=3)
    turn_by(-90, max_power=60)
    drive(-500, start_speed=40, max_speed=80, end_speed=40, decel_mm=120, accel_rate=3)
    turn_by(-30, max_power=80, pivot=LEFT)
    drive(-150, start_speed=40, max_speed=80, end_speed=40, decel_mm=100, accel_rate=3)
    turn_by(30, max_power=80)
    drive(-220, start_speed=40, max_speed=80, end_speed=40, decel_mm=100, accel_rate=3)
    turn_by(93, max_power=60, pivot=RIGHT)
    drive(63, start_speed=10, max_speed=30, end_speed=30, decel_mm=30, accel_rate=3)
    drive(-10, start_speed=20, max_speed=40, end_speed=20, decel_mm=30, accel_rate=3)
    turn_by(40, max_power=80, pivot=LEFT)
    turn_by(20, max_power=80, pivot=LEFT)
    right_att_run(100, 520)
    turn_by(-39, max_power=80)
    right_att_run(100, 60)
    drive(-200, start_speed=20, max_speed=40, end_speed=20, decel_mm=30, accel_rate=3)


# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_4()
