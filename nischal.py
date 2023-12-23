from mail import email_sender
from main import distance_sensor_reader  # Import distance_sensor_reader from main
from camara import webcam_controller

try:
    while True:
        One = distance_sensor_reader.distance_value  # Access distance_value attribute

        if One >= 0.25:
            Two = email_sender
            Trd = webcam_controller
            print("Warning")
            break
        else:
            print("Nothing found")

except Exception as e:
    print(f"There is some error: {e}")
