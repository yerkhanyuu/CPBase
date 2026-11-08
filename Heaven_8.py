"""Heaven_8.py — заезд №8."""
from Base import *


def run_8():
    """Заезд №8"""
    print_battery()
    set_heading(0)
    left_att_run(100, 180, block=False)
    right_att_run(100, 45, block=True)
    drive(865, start_speed=30, max_speed=60, end_speed=30, decel_mm=100, accel_rate=5)
    turn_by(40, max_power=30)
    right_att_dc(100, 400)
    turn_by(-40, max_power=30)
    turn_by(-30, max_power=30)
    drive(50, start_speed=30, max_speed=60, end_speed=30, decel_mm=100, accel_rate=5)
    left_att_run(10, -200)
    wait(2000)
    left_att_run(10, 180)
    turn_by(30, max_power=30, pivot=LEFT)

    drive(-800, start_speed=20, max_speed=100, end_speed=100, decel_mm=0, accel_rate=5)


# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_8()
