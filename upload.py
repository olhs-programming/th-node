import Adafruit_DHT as dht
import time

SENSOR_ID = "test1"
with open(SENSOR_ID + ".csv", "a+", 0) as f: 
    while True:
        h,t = dht.read(dht.DHT22, 4)
        if h is not None and t is not None:
            print "Temp={0:0.1f}C  Humidity={1:0.1f}%".format(t, h)
            f.write(str(int(time.time())) + "," + str(round(t, 2)) + "," + str(round(h, 2)) + "\n")
            time.sleep(3)
        else:
            time.sleep(5)