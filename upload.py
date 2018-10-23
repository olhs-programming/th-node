import Adafruit_DHT as dht
import time

SENSOR_ID = "test1"
INTERVAL = 30

with open(SENSOR_ID + ".csv", "a+", 0) as f: 
    with open(SENSOR_ID + ".min.csv", "a+", 0) as f2: 
        counter_time = 0
        sum_temp = 0
        sum_hum = 0
        divide = 0

        while True:
            h,t = dht.read(dht.DHT22, 4)
            if h is not None and t is not None:
                print "Temp={0:0.1f}C  Humidity={1:0.1f}%".format(t, h)
                f.write(str(int(time.time())) + "," + str(round(t, 2)) + "," + str(round(h, 2)) + "\n")

                counter_time += 3
                sum_temp += t
                sum_hum += h
                divide += 1

                if counter_time >= INTERVAL:
                    if divide > 0:
                        f2.write(str(int(time.time())) + "," + str(round(sum_temp / divide, 2)) + "," + str(round(sum_hum / divide, 2)) + "\n")
                    counter_time = 0
                    sum_temp = 0
                    sum_hum = 0
                    divide = 0
                
                time.sleep(3)
            else:
                counter_time += 5
                time.sleep(5)