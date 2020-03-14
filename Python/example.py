# MPL3115A2
import smbus
import time
import MPL
import Si7021
import MS5637
#from termcolor import colored

sensor = MPL
sensorSi = Si7021
sensorMS = MS5637


Date = time.strftime("%a, %d %b %Y %H:%M:%S")

printDate = "\033[1;30;47m Today is : %s" %Date
print(printDate)
print("\033[1;31;40m========================================================")
print("MPL31152 Reading")
print("Pressure : %.2f mbar" %sensor.pressure)
print("Altitude : %.2f m" %sensor.altitude)
print("Temperature in Celsius : %.2f" u'\xb0' "C" %sensor.cTemp)
print("Temperature in Fahrenheit : %.2f" u'\xb0' "F" %sensor.fTemp)
print("========================================================")
print("")
print("\033[1;32;40m========================================================")
print("Si7021 Reading")
print("Humidity %%RH: %.2f%%" %sensorSi.humidity)
print("Temperature Celsius: %.2f" u'\xb0' "C"  %sensorSi.cTemp)
print("Temperature Fahrenheit: %.2f"  u'\xb0' "F" %sensorSi.fTemp)
print("========================================================")
print("")
print("\033[1;36;40m========================================================")
print("MS5637 Reading")
print("Pressure : %.2f mbar" %sensorMS.pressure)
print("Temperature in Celsius    : %.2f" u'\xb0' "C"  %sensorMS.cTemp)
print("Temperature in Fahrenheit : %.2f" u'\xb0' "F" %sensorMS.fTemp)
print("========================================================")
print("")
