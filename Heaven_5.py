"""Heaven_5.py — заезд №5."""
from Base import *


def run_5():
    """Заезд №5"""
    print_battery()

    right_att_run(50, 40, block=False)
    drive(690, start_speed=10, max_speed=80, end_speed=30, decel_mm=100, accel_rate=5)
    turn_by(-90, max_power=40)
    drive(370, start_speed=10, max_speed=80, end_speed=30, decel_mm=100, accel_rate=5)
    turn_by(133, max_power=40)
    drive(195, start_speed=10, max_speed=40, end_speed=30, decel_mm=50, accel_rate=5)
    right_att_run(100, 220)
    drive(90, start_speed=20, max_speed=30, end_speed=40, decel_mm=0, accel_rate=5)
    drive(-140, start_speed=20, max_speed=80, end_speed=60, decel_mm=50, accel_rate=5)
    turn_by(43, max_power=60)
    right_att_run(80, -260, block=False)
    drive(480, start_speed=30, max_speed=80, end_speed=30, decel_mm=50, accel_rate=5)
    drive(-100, start_speed=10, max_speed=30, end_speed=30, decel_mm=0, accel_rate=5)
    turn_by(-25, max_power=30)
    right_att_run(80, 200, block=False)
    drive(80, start_speed=30, max_speed=50, end_speed=30, decel_mm=40, accel_rate=5)
    left_att_run(20, 520)
    left_att_run(100, -400, block=False)
    drive(-15, start_speed=30, max_speed=50, end_speed=50, decel_mm=0, accel_rate=5)
    turn_by(30, max_power=80)
    drive(-25, start_speed=30, max_speed=50, end_speed=50, decel_mm=0, accel_rate=5)
    turn_by(-95, max_power=80)
    drive(-700, start_speed=30, max_speed=100, end_speed=100, decel_mm=10, accel_rate=5)


# Тестовый запуск: работает только если запустить ИМЕННО этот файл
# (из mainHeaven.py этот блок не выполняется).
if __name__ == "__main__":
    set_heading(0)  # задаём нулевой курс перед стартом, как это делает меню
    run_5()
