"""Heaven_1.py — заезд №1."""
from Base import *


def run_1():
    """Заезд №1 — Миссия с деревом"""
    print_battery()

    right_att_run(50, 540, block=False)
    left_att_run(50, 180, block=False)
    drive(468, start_speed=40, max_speed=60, end_speed=40, decel_mm=55, accel_rate=3)
    drive(-200, start_speed=40, max_speed=80, end_speed=40, decel_mm=80, accel_rate=3)
    turn_by(45, max_power=60)
    drive(350, start_speed=40, max_speed=60, end_speed=40, decel_mm=100, accel_rate=3)
    turn_by(-47, max_power=80)
    left_att_run(100, -130, block=False)
    drive(337, start_speed=30, max_speed=60, end_speed=30, decel_mm=24, accel_rate=3)
    turn_by(40, max_power=30)
    left_att_dc(100, 360)
    turn_by(-40, max_power=40)
    drive(-190, start_speed=30, max_speed=60, end_speed=30, decel_mm=62, accel_rate=3)
    right_att_run(100, -540, block=False)
    turn_by(-50, max_power=60)
    drive(180, start_speed=20, max_speed=40, end_speed=20, decel_mm=0, accel_rate=3)
    right_att_run(100, 200)
    drive(-200, start_speed=30, max_speed=60, end_speed=30, decel_mm=80, accel_rate=3)
    turn_by(45, max_power=80)
    drive(-200, start_speed=50, max_speed=100, end_speed=50, decel_mm=80, accel_rate=3)
    turn_by(35, max_power=80)
    drive(-400, start_speed=50, max_speed=100, end_speed=50, decel_mm=180, accel_rate=3)


# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_menu()
