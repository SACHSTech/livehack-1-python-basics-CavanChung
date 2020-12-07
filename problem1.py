'''
-------------------------------------------------------------------------------
Name:	problem1.py

Purpose: Take the users fahrenheit as input and outputs celcius

Author: Chung.C

Created: 07/12/2020
------------------------------------------------------------------------------
'''

#Input the celius
celsius = float(input("Enter temperature in Celsius: "))

#Using the celsius convert to fahrenheit
fahrenheit = (celsius * (9/5)) + 32

#Ouput the converted temperature
print("Temperature in Fahrenheit is: " + str(fahrenheit))
