"""Heaven_1.py — заезд №1."""
from Base import *


def run_1():
    """Заезд №1 — Миссия с деревом"""
    print_battery()

    right_att_run(80, 540, block=False)
    left_att_run(80, 180, block=False)
    drive(470, start_speed=20, max_speed=80, end_speed=70, decel_mm=400, accel_rate=3)
    drive(-200, start_speed=50, max_speed=80, end_speed=50, decel_mm=0, accel_rate=3)
    turn_by(45, max_power=80)
    drive(350, start_speed=50, max_speed=80, end_speed=50, decel_mm=0, accel_rate=3)
    turn_by(-50, max_power=80)
    left_att_run(100, -140, block=False)
    drive(356, start_speed=40, max_speed=80, end_speed=40, decel_mm=300, accel_rate=3)
    turn_by(50, max_power=50)
    left_att_dc(100, 420)
    turn_by(-45, max_power=50)
    drive(-177, start_speed=40, max_speed=60, end_speed=40, decel_mm=150, accel_rate=3)
    right_att_run(100, -500, block=False)
    turn_by(-50, max_power=80)
    drive(150, start_speed=30, max_speed=50, end_speed=30, decel_mm=0, accel_rate=3)
    right_att_run(100, 240)
    drive(-100, start_speed=40, max_speed=60, end_speed=40, decel_mm=0, accel_rate=3)
    turn_by(50, max_power=80)
    drive(-725, start_speed=50, max_speed=80, end_speed=50, decel_mm=0, accel_rate=3)
# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_1()
