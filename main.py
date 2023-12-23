# main.py

from signal import signal, SIGTERM, SIGHUP, pause
from time import sleep
from threading import Thread
from gpiozero import DistanceSensor

class DistanceSensorReader:
    def __init__(self, echo_pin=20, trigger_pin=21):
        self.reading = True
        self.sensor = DistanceSensor(echo=echo_pin, trigger=trigger_pin)
        self.distance_value = 0  # Initialize distance_value attribute

    def safe_exit(self, signum, frame):
        self.reading = False
        exit(1)

    def read_distance(self):
        while self.reading:
            distance_value = round(self.sensor.value, 2)
            message = f"Distance: {distance_value} m"
            self.distance_value = distance_value  # Assign the value to an instance variable
            print(message)
            sleep(0.1)

    def start_reading(self):
        signal(SIGTERM, self.safe_exit)
        signal(SIGHUP, self.safe_exit)

        reader = Thread(target=self.read_distance, daemon=True)
        reader.start()

        pause()

if __name__ == "__main__":
    distance_sensor_reader = DistanceSensorReader()
    distance_sensor_reader.start_reading()
