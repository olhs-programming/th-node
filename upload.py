import Adafruit_DHT as dht
import time

SENSOR_ID = "test1"
with open(SENSOR_ID + ".csv", "a+") as f: 
    while True:
        h,t = dht.read(dht.DHT22, 4)
        print "Temp={0:0.1f}C  Humidity={1:0.1f}%".format(t, h)

        if h is not None:
            f.write(str(int(time.time())) + "," + str(round(t, 2)) + "," + str(round(h, 2)))

        time.sleep(2.15)