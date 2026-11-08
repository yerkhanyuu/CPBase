"""Heaven_4.py — заезд №4."""
from Base import *


def run_4():
    """Заезд №4"""
    print_battery()

    set_heading(0)
    left_att_run(50, -180, block=False)
    drive(250, start_speed=30, max_speed=60, end_speed=50, decel_mm=0, accel_rate=5)
    turn_by(-90, max_power=80)
    drive(-500, start_speed=30, max_speed=80, end_speed=60, decel_mm=0, accel_rate=5)
    turn_by(-30, max_power=80, pivot=LEFT)
    drive(-150, start_speed=40, max_speed=80, end_speed=40, decel_mm=0, accel_rate=5)
    turn_by(30, max_power=80)
    drive(-220, start_speed=30, max_speed=80, end_speed=60, decel_mm=50, accel_rate=5)
    turn_by(93, max_power=50, pivot=RIGHT)
    drive(63, start_speed=10, max_speed=30, end_speed=30, decel_mm=0, accel_rate=5)
    turn_by(45, max_power=80, pivot=LEFT)
    turn_by(-40, max_power=80)
    drive(-200, start_speed=20, max_speed=40, end_speed=40, decel_mm=20, accel_rate=5)
    turn_by(90, max_power=80)
    drive(300, start_speed=20, max_speed=40, end_speed=20, decel_mm=50, accel_rate=5)
    turn_by(-30, max_power=80)
    left_att_run(50, 180)
    turn_by(-30, max_power=80)
    turn_by(45, max_power=80)
    drive(400, start_speed=20, max_speed=80, end_speed=80, decel_mm=0, accel_rate=5)
    turn_by(-120, max_power=100)

# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_4()
