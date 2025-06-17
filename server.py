import os
import json
import threading
import platform
import atexit
from datetime import datetime
from flask import Flask, request


def setupGPIO():
    import RPi.GPIO as GPIO
    import serial
    ser = serial.Serial('/dev/serial0', 115200, timeout=1)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(17, GPIO.IN, pull_up_down=GPIO.PUD_UP)

    def send_UART_test(pin):
        exampleMessage = {
            '_id': 464367616,
            'image': 'pojgsoigj4903gjeogj9w0agjsrdgljdlsgjdgloj4903gjjsrgsdgjb87yt78346584INihgsihg98434',
            'isOpen': 0,
            'tempF': 68,
            'hubDate': datetime.now().isoformat(),
            'date': '2025-01-01T14:06:00Z',
            'nextCheckIn': 86400,
            'batteryV': 1.21
        }
        print("Sending UART message...")
        ser.write(json.dumps(exampleMessage).encode())
        # ser.close()
    GPIO.add_event_detect(
        17, GPIO.FALLING, callback=send_UART_test, bouncetime=200)
    atexit.register(GPIO.cleanup)


if platform.system() != 'Linux' or not platform.machine().startswith('arm'):
    print('Not running on a Pi. No GPIO available')
else:
    threading.Thread(target=setupGPIO, daemon=True).start()

app = Flask(__name__)

if os.getenv('ENV') == 'dev':
    app.run(debug=True)


@app.route('/')
def home():
    return 'You are connected to a server!'


@app.route('/upload', methods=['POST'])
def upload():
    data = request.get_data()
    print('received', data)
    parsed = json.loads(data)
    print('parsedImage', parsed['image'])
    return 'Got Post'
