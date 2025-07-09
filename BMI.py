# Author: Dmitriy.S - Dhotspot.dev
# Date  : 07/08/25
# Version: First Rel
# About : This BMI calculator is written to be used by those who are unfamiliar with their mass in KG, and height in CM, instead, I used formulas to convert automatically weight to Kilograms, and height in feet to Centimeters.
# The running_time is another feature that I found to be interesting for those interested people out there.

# Source used to list categories of BMI : https://www.cdc.gov/bmi/adult-calculator/bmi-categories.html

"""Please note, this program is in no way making anyone profit, and is open source.
   You may do whatever, however, but I would like to see this being used for studies or in classrooms for learning.
    If you can think of any other features for this program, please open a new issue."""

import time

def bmicalc():
    
    feet = float(input("Please input your height in feet : "))
    lbs = float(input("Please enter your weight in LBS : "))

    height = (feet * 30.48)
    weight = (lbs * 0.45359237)
    bmi = weight/(height/100)**2
    print("Your BMI is %.1f" % bmi)
    if bmi < 18.5:
        print("Underweight")
    if bmi >= 18.5 and bmi < 25:
        print("You are of healthy BMI!")
    if bmi >= 25 and bmi < 30:
        print("You are overweight")
    if bmi > 30:
        print("You are obese")
    if bmi >= 30 and bmi < 35:
        print("Class one obesity.")
    if bmi >= 35 and bmi < 40:
        print("Class two obesity.")
    if bmi >= 40:
        print("Class three obesity. Severe.")

def running_time(): # This function times the programs running time, and stops once the numbers have reached the end.
         start_time = time.time()
         bmicalc()
         end_time = time.time()
         print("This programs running time in s: %s" % (end_time - start_time))

if __name__ == "__main__":
    running_time()