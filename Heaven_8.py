"""Heaven_8.py — заезд №8."""
from Base import *


def run_8():
    """Заезд №8"""
    print_battery()
    drive(640, start_speed=50, max_speed=100, end_speed=50, decel_mm=0, accel_rate=2)
    turn_by(-45, max_power=60, pivot=LEFT)
    drive(65, start_speed=30, max_speed=60, end_speed=30, decel_mm=0, accel_rate=2)
    right_att_run(100, -230, block=True)
    drive(-120, start_speed=30, max_speed=60, end_speed=30, decel_mm=0, accel_rate=2)
    turn_by(50, max_power=60, pivot=LEFT)
    right_att_run(100, 270, block=False)
    drive(-625, start_speed=50, max_speed=100, end_speed=50, decel_mm=0, accel_rate=2)



# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_8()
