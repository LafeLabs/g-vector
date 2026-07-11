import time
import board
import adafruit_lsm6ds.lsm6ds3trc

i2c = board.I2C()
sensor = adafruit_lsm6ds.lsm6ds3trc.LSM6DS3TRC(i2c)

while True:
    g_x, g_y, g_z = sensor.acceleration
    print(f"({g_x:.2f}, {g_y:.2f}, {g_z:.2f})")
    time.sleep(0.020)
