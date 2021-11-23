import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

trig = 3
echo = 2
led = 17
threshold = 200

GPIO.setup(led, GPIO.OUT)
pwm = GPIO.PWM(led, threshold)
GPIO.setup(trig, GPIO.OUT)
GPIO.setup(echo, GPIO.IN)

GPIO.output(trig, False)
pwm.start(0)
time.sleep(2)

def Distance():
    GPIO.output(trig, True)
    time.sleep(0.0001)
    GPIO.output(trig, False)

    while (GPIO.input(echo) == 0):
        start = time.time()

    while (GPIO.input(echo) == 1):
        end = time.time()
        
    dur = end - start
    dist = dur*17150
    dist = round(dist, 2)
    return dist

d1 = Distance()

pwm.ChangeDutyCycle(100 - (d1*2))
print("Initial distance:", d1, "cm")

try:
    while True:
        d2 = Distance()
        if (d2 > 400):
            print("Distance is going beyond limit")
        elif (d2 > 50):
            pwm.ChangeDutyCycle(0)
            print("Distance is :", d2, "cm")
        else:
            pwm.ChangeDutyCycle(100 - (d1*2))
            print("Distance:", d2, "cm")
            d1 = d2
        time.sleep(1)

except:
    print("An error has occured.")

finally:
    GPIO.cleanup()