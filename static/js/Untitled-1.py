import RPi.GPIO as GPIO
import time
import paho.mqtt.client as mqtt
from datetime import datetime

GPIO.setmode(GPIO.BOARD)
btn1=12
btn2=13
led1=7
led2=11
f=open("Datos.dat","a")
f.write("Datos recolectados\n")
f.close()

def on_message(client,obj,msg):
    print(msg.topic+" "+str(msg.qos)+" "+msg.payload.decode('utf-8'))

def main():
    bot1=0
    bot2=0
    mqttc=mqtt.Client()
    mqttc.on_message=on_message
    mqttc.username_pw_set("jomsk@hotmail.com","Jomsk4all1996")
    mqttc.connect("maqiatto.com",1883)
    mqttc.subscribe("jomsk@hotmail.com/IoT1",0)
    GPIO.setup(led1,GPIO.OUT)
    GPIO.setup(led2,GPIO.OUT)
    GPIO.setup(btn1,GPIO.IN)
    GPIO.setup(btn2,GPIO.IN)
    nbtn=0
    while(1):
        mqttc.loop()
        bot1=GPIO.input(btn1)
        bot2=GPIO.input(btn2)
        f=open("Datos.dat","a")
        fecha=datetime.now()
        fechaAc=str(fecha).split(".")[0]
        if(bot1==1):
            
            GPIO.output(led1,1)
            f.write(fechaAc+"  Boton1 Presionado\n")
            f.close()
            time.sleep(1)
            GPIO.output(led1,0)
            nbtn=1
            mqttc.publish("jomsk@hotmail.com/IoT",str(nbtn))
            
        if(bot2==1):
            
            GPIO.output(led2,1)
            f.write(fechaAc+"  Boton2 Presionado\n")
            f.close()
            time.sleep(1)
            GPIO.output(led2,0)
            nbtn=2
            mqttc.publish("jomsk@hotmail.com/IoT",str(nbtn))
            
   
            