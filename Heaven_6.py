"""Heaven_6.py — заезд №6."""
from Base import *


def run_6():
    """Заезд №6"""
    print_battery()

    set_heading(0)
    drive(300, start_speed=30, max_speed=60, end_speed=40, decel_mm=50, accel_rate=5)
    left_att_run(40, 90)
    right_att_run(50, 90)
    drive(-150, start_speed=30, max_speed=60, end_speed=40, decel_mm=50, accel_rate=5)
    right_att_run(50, -70, block=False)
    turn_by(15, max_power=30)
    right_att_run(50, -40, block=False)
    drive(-200, start_speed=30, max_speed=80, end_speed=80, decel_mm=0, accel_rate=5)


# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_6()
