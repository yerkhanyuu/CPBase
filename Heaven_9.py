"""Heaven_9.py — заезд №9."""
from Base import *


def run_9():
    """Заезд №9 (пока пустой)"""
    print_battery()

    drive(200, start_speed=30, max_speed=50, end_speed=50, decel_mm=0, accel_rate=5)
    turn_by(90, max_power=100)
    turn_by(-180, max_power=100)
    turn_by(-180, max_power=100)
    drive(200, start_speed=30, max_speed=50, end_speed=50, decel_mm=0, accel_rate=5)
    drive(-400, start_speed=30, max_speed=50, end_speed=50, decel_mm=0, accel_rate=5)
    turn_by(180, max_power=100)
    drive(-200, start_speed=30, max_speed=50, end_speed=50, decel_mm=0, accel_rate=5)
    turn_by(90, max_power=100)
    drive(-200, start_speed=30, max_speed=50, end_speed=50, decel_mm=0, accel_rate=5)


if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_9()
