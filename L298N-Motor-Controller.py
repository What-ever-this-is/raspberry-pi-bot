import RPi.GPIO as GPIO
import time as t
GPIO.setmode(GPIO.BOARD)
in1 = 11
in2 = 12
in3 = 15
in4 = 16
ena = 13
enb = 18
GPIO.setup(in1,GPIO.out)
GPIO.setup(in2,GPIO.out)
GPIO.setup(in3,GPIO.out)
GPIO.setup(in4,GPIO.out)
GPIO.setup(ena,GPIO.out)
GPIO.setup(enb,GPIO.out)
motorASpeed = GPIO.PWM(ena,1000)
motorBSpeed = GPIO.PWM(enb,1000)
motorASpeed.start(0)
motorBSpeed.start(0)
def setMotorAdirection(forward):
    if forward:
        GPIO.output(in1,GPIO.HIGH)
        GPIO.output(in2,GPIO.LOW)
    else:
        GPIO.output(in1,GPIO.LOW)
        GPIO.output(in2,GPIO.HIGH)
def setMotorBdirection(forward):
    if forward:
        GPIO.output(in3,GPIO.HIGH)
        GPIO.output(in4,GPIO.LOW)
    else:
        GPIO.output(in3,GPIO.LOW)
        GPIO.output(in4,GPIO.HIGH)
def setMotorAspeed(speed):
    if speed>100:
        speed = 100
    elif speed<0:
        speed = 0
    motorASpeed.ChangeDutyCycle(speed*10)
def setMotorBspeed(speed):
    if speed>100:
        speed = 100
    elif speed<0:
        speed = 0
    motorBSpeed.ChangeDutyCycle(speed*10)
setMotorAdirection(1)
setMotorBdirection(1)
setMotorAspeed(50)
setMotorBspeed(100)
t.sleep(5)
motorASpeed.stop()
motorBSpeed.stop()
GPIO.cleanup()
