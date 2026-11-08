"""Heaven_2.py — заезд №2."""
from Base import *


def run_2():
    """Заезд №2"""
    print_battery()

    turn_by(40, max_power=80)
    drive(480, start_speed=20, max_speed=80, end_speed=20, decel_mm=35, accel_rate=3)
    left_att_run(20, 180)
    drive(-400, start_speed=10, max_speed=100, end_speed=100, decel_mm=80, accel_rate=3)
    turn_by(50, max_power=80)
    drive(680, start_speed=40, max_speed=50, end_speed=40, decel_mm=330, accel_rate=3)
    turn_by(-45, max_power=50)
    drive(45, start_speed=40, max_speed=50, end_speed=40, decel_mm=0, accel_rate=3)
    turn_by(-40, max_power=50)
    drive(-50, start_speed=40, max_speed=80, end_speed=40, decel_mm=0, accel_rate=3)
    turn_by(45, max_power=80)
    turn_by(45, max_power=80)
    drive(-800, start_speed=40, max_speed=80, end_speed=40, decel_mm=680, accel_rate=3)


# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_2()
