"""Heaven_1.py — заезд №1."""
from Base import *


def run_1():
    """Заезд №1 — Миссия с деревом"""
    print_battery()

    set_heading(0)
    left_att_run(100, 155, block=False)
    right_att_run(100, 180, block=False)
    drive(470, start_speed=30, max_speed=60, end_speed=50, decel_mm=70, accel_rate=3)
    drive(-300, start_speed=50, max_speed=80, end_speed=80, decel_mm=0, accel_rate=5)
    wait(2000)
    set_heading(0)
    right_att_run(100, -135, block=True)
    drive(865, start_speed=30, max_speed=60, end_speed=30, decel_mm=100, accel_rate=5)
    turn_by(40, max_power=30)
    right_att_dc(100, 400)
    turn_by(-40, max_power=30)
    turn_by(-30, max_power=30)
    drive(50, start_speed=30, max_speed=60, end_speed=30, decel_mm=100, accel_rate=5)
    left_att_run(10, -230)
    wait(2000)
    left_att_run(10, 180)
    turn_by(30, max_power=30, pivot=LEFT)

    drive(-800, start_speed=20, max_speed=100, end_speed=100, decel_mm=0, accel_rate=5)
# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_1()
