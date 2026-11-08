"""Heaven_3.py — заезд №3."""
from Base import *


def run_3():
    """Заезд №3"""
    print_battery()
    drive(500, start_speed=30, max_speed=80, end_speed=30, decel_mm=100, accel_rate=5)
    turn_by(70, max_power=80, pivot=RIGHT)
    drive(200, start_speed=20, max_speed=80, end_speed=30, decel_mm=100, accel_rate=5)
    turn_by(-70, max_power=50, pivot=LEFT)
    right_att_run(100, 45)
    drive(325, start_speed=40, max_speed=60, end_speed=80, decel_mm=0, accel_rate=5)
    right_att_run(60, 135)
    drive(-20, start_speed=20, max_speed=40, end_speed=20, decel_mm=0, accel_rate=5)
    drive(20, start_speed=20, max_speed=40, end_speed=20, decel_mm=0, accel_rate=5)
    drive(-20, start_speed=20, max_speed=40, end_speed=20, decel_mm=0, accel_rate=5)
    turn_by(30, max_power=80, pivot=LEFT)
    drive(-800, start_speed=30, max_speed=100, end_speed=300, decel_mm=0, accel_rate=5)

# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_3()
