import random
def tempMonitor():
 minRoomTemp=15
 maxRoomTemp=25 
 minRoomHum=30
 maxRoomHum=50
 temp = random.randint(14,26)
 humidity = random.randint(29,51)
 if ((temp>=minRoomTemp)and(temp<=maxRoomTemp) and (humidity>=minRoomHum) and (humidity<=maxRoomHum)):
   print("The temperature and humidity is optimum")
   tempMonitor()
 else:
   if(temp<minRoomTemp):
     print("The temperature is too cold:"+ str(temp))
   if(humidity<minRoomHum):
     print("The humidity is low:"+ str(humidity)) 
   if(temp>maxRoomTemp):
     print("The temperature is too hot:"+ str(temp))
   if(humidity>maxRoomHum):
     print(" ALERT: The humidity is high:"+ str(humidity))
 return
 
tempMonitor()
