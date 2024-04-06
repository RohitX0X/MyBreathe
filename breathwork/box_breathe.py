import winsound
import time

if(__name__ == "__main__"):

    while True:
        winsound.Beep(1000, 50)  # Beep with a frequency of 1000 Hz for 500 milliseconds
        time.sleep(3)  # Wait for 3 seconds before the next beep
