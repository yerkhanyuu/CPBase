"""Heaven_2.py — заезд №2."""
from Base import *


def run_2():
    """Заезд №2"""
    print_battery()

    set_heading(0)
    drive(670, start_speed=20, max_speed=80, end_speed=60, decel_mm=100, accel_rate=5)
    right_att_run(50, -80, block=False)
    turn_by(-45, max_power=80)
    drive(100, start_speed=30, max_speed=40, end_speed=30, decel_mm=50, accel_rate=5)
    right_att_run(80, -200)
    drive(-150, start_speed=30, max_speed=60, end_speed=30, decel_mm=0, accel_rate=5)
    turn_by(45, max_power=80)
    drive(-670, start_speed=20, max_speed=80, end_speed=60, decel_mm=50, accel_rate=5)

    turn_by(35, max_power=80)
    drive(480, start_speed=20, max_speed=50, end_speed=30, decel_mm=50, accel_rate=5)
    left_att_run(100, 180)
    drive(-400, start_speed=20, max_speed=50, end_speed=40, decel_mm=0, accel_rate=5)

    turn_by(55, max_power=80)
    drive(580, start_speed=20, max_speed=80, end_speed=50, decel_mm=50, accel_rate=5)
    turn_by(-90, max_power=100, pivot=LEFT)
    turn_by(90, max_power=100, pivot=LEFT)
    drive(-650, start_speed=20, max_speed=80, end_speed=80, decel_mm=0, accel_rate=5)

# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_2()
