import Adafruit_DHT as dht
import time

while True:
    h,t = dht.read(dht.DHT22, 4)
    print "Temp={0:0.1f}C  Humidity={1:0.1f}%".format(t, h)
    time.sleep(2.15)